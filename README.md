# Recruiting Agent

A smart recruiting assistant that matches job descriptions with candidate resumes and generates personalized email communications.

## Overview

This application helps recruiters streamline their candidate selection process by:
1. Matching job descriptions with candidate resumes using AI
2. Ranking candidates based on their fit for specific positions
3. Generating personalized email communications for selected candidates

## Features

- **Resume Matching**: Analyzes resumes against job descriptions to find the best matches
- **Candidate Ranking**: Scores and ranks candidates based on their qualifications
- **Email Generation**: Creates personalized emails for candidate communication
- **Web Interface**: User-friendly interface for inputting job descriptions and viewing results

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Processing**: Pandas, NLTK
- **Machine Learning**: 
  - TF-IDF Vectorization
  - Cosine Similarity
  - LangChain
  - OpenAI Models (GPT and Embeddings)
- **Vector Database**: ChromaDB

## Model Choice and Preprocessing

### Model Architecture

The application uses a hybrid approach combining traditional NLP techniques with modern AI:

1. **Initial Filtering with TF-IDF and Cosine Similarity**:
   - TF-IDF vectorization converts resume text into numerical representations
   - Cosine similarity measures the relevance between job titles and resumes
   - This provides an efficient first-pass filter to identify potentially relevant candidates

2. **Semantic Search with Embeddings**:
   - OpenAI's text-embedding-3-small model creates dense vector representations
   - ChromaDB stores and enables similarity search on these embeddings
   - This captures deeper semantic relationships beyond keyword matching

3. **Detailed Analysis with LLM**:
   - OpenAI's GPT-4o model performs in-depth analysis of top candidates
   - Evaluates candidates on multiple dimensions (experience, skills, education, etc.)
   - Provides detailed explanations of candidate strengths and weaknesses

### Preprocessing Steps

1. **Resume Structuring**:
   - Combines various resume fields (career objective, skills, experience, education) into a structured text format
   - Creates a standardized representation for consistent processing

2. **Text Cleaning**:
   - Converts text to lowercase for case-insensitive matching
   - Removes punctuation, special characters, and extra whitespace
   - Splits text on commas to handle list-like content

3. **Stopword Removal**:
   - Filters out common English stopwords using NLTK
   - Improves signal-to-noise ratio in the text representation

4. **Vectorization**:
   - Creates TF-IDF vectors for initial similarity scoring
   - Generates dense embeddings for semantic search

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/Devparihar5/recruiting-agent.git
   cd recruiting-agent
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.sample` to `.env`
   - Add your OpenAI API key and configure model names

5. Run the application:
   ```
   gunicorn app:app --threads=4
   ```

6. Access the web interface at `http://localhost:8000`

## Usage

1. Enter the position name and job description on the home page
2. Submit the form to process and match resumes
3. View the top matching candidates with their scores and explanations
4. Generate personalized emails for selected candidates

## Docker Support

The application includes Docker support for containerized deployment:

```
docker build -t recruiting-agent .
docker run -p 5000:5000 recruiting-agent
```

## Project Structure

- `/app.py` - Main Flask application
- `/utils/` - Utility modules
  - `resume_matcher.py` - Core matching logic
  - `resume.py` - Resume preprocessing functions
  - `mail.py` - Email generation functionality
- `/config/` - Configuration files
  - `configs.py` - Application configuration
  - `consts.py` - Constants and prompt templates
- `/templates/` - HTML templates
- `/data/` - Resume data (CSV format)
- `/chroma_db/` - Vector database storage

## Future Improvements

- Add user authentication and role-based access
- Implement resume parsing from PDF/DOCX files
- Add interview scheduling functionality
- Expand email templates for different communication scenarios
- Implement feedback loop to improve matching accuracy over time
