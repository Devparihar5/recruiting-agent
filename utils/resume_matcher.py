import os
from config.configs import Configs
from config.consts import Consts
from langchain_chroma import Chroma
from langchain.chains import LLMChain
from langchain.docstore.document import Document
from concurrent.futures import ThreadPoolExecutor, as_completed
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.resume import ResumePreprocessor


class ResumeMatcher:
    vectorizer = TfidfVectorizer(stop_words='english')

    @staticmethod
    def preprocess_profiles(df):
        """
        Generate full and processed profile columns from DataFrame.
        """
        df["full_profile"] = df.apply(ResumePreprocessor.preprocess_resume, axis=1)
        df["processed_profile"] = df["full_profile"].apply(
            lambda x: " ".join(ResumePreprocessor.preprocess_text(x))
        )
        return df

    @staticmethod
    def get_similarity_scores(df, position_name):
        """
        Compute cosine similarity between job title and resumes.
        """
        tfidf_matrix = ResumeMatcher.vectorizer.fit_transform(df["processed_profile"])
        query_vec = ResumeMatcher.vectorizer.transform([position_name])
        df["similarity"] = cosine_similarity(query_vec, tfidf_matrix).flatten()
        return df

    @staticmethod
    def build_or_load_vectordb(filtered_df):
        """
        Build or load the Chroma vector store.
        """
        if os.path.exists(Configs.persist_dir):
            return Chroma(persist_directory=Configs.persist_dir, embedding_function=Configs.embedding_model)
        else:
            documents = [
                Document(page_content=text, metadata={"index": i})
                for i, text in enumerate(filtered_df["processed_profile"])
            ]
            return Chroma.from_documents(documents, Configs.embedding_model, persist_directory=Configs.persist_dir)

    @staticmethod
    def process_candidate(doc, job_description):
        llm_chain = Consts.prompt_template_to_score_resume | Configs.openai_client
        input_data = {
            'job_description': job_description,
            'resume': doc.page_content
        }
        return llm_chain.invoke(input_data).content

    @staticmethod
    def match(df, position_name, job_description):
        top_candidates = []

        df = ResumeMatcher.preprocess_profiles(df)
        df = ResumeMatcher.get_similarity_scores(df, position_name)

        # Filter resumes based on a minimum similarity threshold
        filtered_df = df[df["similarity"] > 0.3].sort_values(by="similarity", ascending=False)

        vectordb = ResumeMatcher.build_or_load_vectordb(filtered_df)

        embedded_job_description = Configs.embedding_model.embed_query(job_description)
        docs_and_scores = vectordb.similarity_search_by_vector_with_relevance_scores(embedded_job_description, k=5)

        with ThreadPoolExecutor() as executor:
            future_to_doc = {
                executor.submit(ResumeMatcher.process_candidate, doc, job_description): (doc, score)
                for doc, score in docs_and_scores
            }

            for future in as_completed(future_to_doc):
                doc, score = future_to_doc[future]
                try:
                    explanation = future.result().strip()
                    top_candidates.append({
                        "resume": doc.page_content,
                        "score": score,
                        "explanation": explanation
                    })
                except Exception as e:
                    print(f"Error processing document: {e}")

        top_candidates = sorted(top_candidates, key=lambda x: x["score"], reverse=True)[:3]
        return {
            "position_name": position_name,
            "top_candidates": top_candidates
        }
