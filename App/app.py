from flask import Flask, render_template, request
import requests
import json
import pickle
import os
import re
import string
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

# Download stopwords if not available
nltk.download('stopwords')

# Initialize Flask app
app = Flask(__name__)

# Define the models directory
MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")

# Function to load models safely
def load_model(file_name):
    try:
        with open(os.path.join(MODELS_DIR, file_name), 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"⚠ Error: {file_name} not found.")
        return None

# Load email spam detection model & vectorizer
email_model = load_model('email_spam_model.pkl')
vectorizer = load_model('email_vectorizer.pkl')

# URLScan.io API Key (Replace with your actual API key)
API_KEY = "cbe02dea-79c3-46b3-9fd0-6be9e6916fd5"

# Function to preprocess email text
def preprocess_email(email_text):
    if not isinstance(email_text, str):
        return ""

    STOPWORDS = set(stopwords.words('english'))
    
    email_text = email_text.lower()
    email_text = BeautifulSoup(email_text, 'html.parser').get_text()  # Remove HTML
    email_text = re.sub(f"[{string.punctuation}]", "", email_text)  # Remove punctuation
    email_text = " ".join(word for word in email_text.split() if word not in STOPWORDS)  # Remove stopwords
    
    return email_text

# Function to detect spam in emails using ML model
def detect_email_spam(email_text):
    processed_email = preprocess_email(email_text)
    email_vector = vectorizer.transform([processed_email])  # Convert to feature vector
    prediction = email_model.predict(email_vector)  # Predict spam or not
    return "Spam" if prediction[0] == 1 else "Not Spam"

# Function to scan URLs using URLScan.io
def check_urlscan(url):
    headers = {
        "API-Key": API_KEY,
        "Content-Type": "application/json"
    }
    
    data = {
        "url": url,
        "visibility": "public"
    }
    
    response = requests.post("https://urlscan.io/api/v1/scan/", headers=headers, data=json.dumps(data))
    
    # Debugging: Print the raw response
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        scan_result = response.json()
        if "result" in scan_result:
            return scan_result["result"]  # Extract scan URL
        return "Error: Could not retrieve scan result."
    else:
        return f"Error retrieving scan results: {response.text}"

# Function to check if input is an email or URL
def is_email(input_text):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, input_text)

@app.route("/", methods=["GET", "POST"])
def index():
    website_result = website_error = None
    email_result = email_error = None

    if request.method == "POST":
        user_input = request.form.get("user_input")

        if is_email(user_input):
            email_result = detect_email_spam(user_input)
        else:
            scan_result = check_urlscan(user_input)
            if "Error" in scan_result:
                website_error = scan_result
            else:
                website_result = scan_result  # URLScan.io result

    return render_template("index.html", website_result=website_result, email_result=email_result, website_error=website_error, email_error=email_error)

if __name__ == "__main__":
    app.run(debug=True)
