# AromaSommelier™

An AI-powered recommendation engine that understands your unique taste preferences and provides personalized coffee recommendations. This project features a quiz-based interface that allows users to discover their ideal coffee based on their preferences for acidity, flavor notes, and body.

---

## Features

- **Taste Quiz**: Users answer three simple questions about their coffee preferences:
  - How do you like your coffee's acidity?
  - What flavor notes appeal to you most?
  - How do you prefer your coffee body?
- **Personalized Recommendations**: Based on the user's answers, the app provides:
  - Coffee Name
  - Description (e.g., flavor notes and roast details)
  - Price
  - Roast Type

---

## Technology Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **Dataset**: CSV file with coffee profiles containing attributes such as acidity, flavor notes, body, price, and roast type.

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (3.8 or later)
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/aromasommelier.git
   cd aromasommelier
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## File Structure

```
AromaSommelier/
|
├── app.py                  # Main Flask application script
├── AromaSommelier_dataset_large.csv  # Coffee dataset file
├── templates/              # HTML templates
│   ├── index.html          # Quiz interface
│   ├── result.html         # Recommendation display
├── static/                 # Static assets (CSS, JS, images)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## Dataset

The dataset includes the following columns:

- `Coffee_Name`: Name of the coffee.
- `Acidity_Level`: Acidity preferences (e.g., Bright, Balanced, Subtle).
- `Flavor_Notes`: Coffee flavor profiles (e.g., Fruity and floral, Nutty and chocolate).
- `Body`: Coffee body (e.g., Light, Medium, Full).
- `Price`: Price of the coffee.
- `Roast_Type`: Type of roast (e.g., Light, Medium, Dark).

---

## Deployment

The project is deployed on **Vercel** for hosting. Simply visit the deployment link to try the application.

---

## How to Use

1. Open the app in your browser.
2. Answer the three questions in the quiz about your coffee preferences.
3. Submit your answers to receive a personalized coffee recommendation.

---

## Acknowledgments

Special thanks to open-source libraries and tools that made this project possible:

- Flask
- Pandas
- Vercel

