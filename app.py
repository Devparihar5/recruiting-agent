from flask import Flask, render_template, request,jsonify
from flask_cors import CORS
import pandas as pd

from markupsafe import Markup
import markdown as md
from utils.resume_matcher import ResumeMatcher
from utils.mail import EmailGenerator


app = Flask(__name__)
CORS(app)  # This enables CORS for all routes


@app.template_filter('markdown')
def markdown_filter(text):
    return Markup(md.markdown(text))

# home page
@app.route("/")
def index():
    return render_template("index.html")

# results page
@app.route("/results", methods=["GET", "POST"])
def results():
    if request.method == "POST":
        try:
            position_name = request.form.get("position_name")
            job_description = request.form.get("jd")

            if not position_name or not job_description:
                return render_template("results.html", candidates=[], error="Missing input fields.")

            try:
                df = pd.read_csv("data/resume_data.csv")
            except Exception as e:
                return render_template("results.html", candidates=[], error=f"Error loading resume data: {str(e)}")

            try:
                result = ResumeMatcher.match(df, position_name, job_description)
                return render_template("results.html", candidates=result)
            except Exception as e:
                return render_template("results.html", candidates=[], error=f"Error processing candidates: {str(e)}")

        except Exception as e:
            return render_template("results.html", candidates=[], error=f"Unexpected error: {str(e)}")

    return render_template("results.html", candidates=[])


@app.route("/generate_mail", methods=["POST"])
def generate_mail():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No input received"}), 400

        resume = data.get("resume")
        position_name = data.get("position_name")

        if not resume or not position_name:
            return jsonify({"error": "Missing resume or position_name"}), 400

        try:
            email = EmailGenerator.generate(resume=resume, position_name=position_name)
            return jsonify({"email": email})
        except Exception as e:
            return jsonify({"error": f"Email generation failed: {str(e)}"}), 500

    except Exception as e:
        return jsonify({"error": f"Unexpected server error: {str(e)}"}), 500

# if __name__ == "__main__":
#     app.run()
