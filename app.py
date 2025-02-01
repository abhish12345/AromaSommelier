from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import random

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
 
# Load the dataset
def load_dataset():
    """Load the AromaSommelier dataset."""
    file_path = "AromaSommelier_dataset_large.csv"  # Replace with your dataset path
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Dataset file not found. Ensure the file path is correct.")
        return None

# Recommendation logic
def recommend_coffee(preferences, dataset):
    """Find the best coffee match based on user preferences."""
    # Filter dataset based on preferences
    matches = dataset[
        (dataset["Acidity_Level"] == preferences["Acidity_Level"]) &
        (dataset["Flavor_Notes"] == preferences["Flavor_Notes"]) &
        (dataset["Body"] == preferences["Body"])
    ]

    # If multiple matches, pick one randomly
    if not matches.empty:
        recommendation = matches.sample(1).iloc[0]
    else:
        # Fallback to a random coffee if no perfect match
        recommendation = dataset.sample(1).iloc[0]

    return recommendation

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Form-based recommendation route
@app.route('/recommend', methods=['POST'])
def recommend():
    dataset = load_dataset()
    if dataset is None:
        return "Dataset not found. Please upload the dataset."

    # Get user inputs from the form
    acidity = request.form.get("acidity")
    flavor = request.form.get("flavor")
    body = request.form.get("body")

    preferences = {
        "Acidity_Level": acidity,
        "Flavor_Notes": flavor,
        "Body": body
    }

    # Get recommendation
    recommendation = recommend_coffee(preferences, dataset)

    return render_template('result.html', coffee_name=recommendation['Coffee_Name'], 
                           description=f"{recommendation['Flavor_Notes']} with {recommendation['Acidity_Level']} acidity",
                           price=recommendation['Price'],
                           roast_type=recommendation['Roast_Type'])

# New JSON-based recommendation route
@app.route('/getrecommendation', methods=['GET'])
def get_recommendation_json():
    dataset = load_dataset()
    if dataset is None:
        return jsonify({"error": "Dataset not found. Please upload the dataset."}), 500

    # Get user preferences from query parameters
    acidity = request.args.get("acidity", default="")
    flavor = request.args.get("flavor", default="")
    body = request.args.get("body", default="")

    preferences = {
        "Acidity_Level": acidity,
        "Flavor_Notes": flavor,
        "Body": body
    }

    # Get recommendation
    recommendation = recommend_coffee(preferences, dataset)

    # Return JSON response
    return jsonify({
        "coffee_name": recommendation['Coffee_Name'],
        "description": f"{recommendation['Flavor_Notes']} with {recommendation['Acidity_Level']} acidity",
        "price": recommendation['Price'],
        "roast_type": recommendation['Roast_Type']
    })

if __name__ == '__main__':
    app.run(debug=True)
