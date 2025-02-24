Fitness Tracker Microservice
A Flask-based microservice that analyzes fitness trends, provides personalized workout suggestions, and aggregates user activity data.

Features
-Receives user activity data (running, walking, cycling, etc.).
-Calculates fitness trends (calories burned, steps taken).
-Provides personalized fitness suggestions.
-Returns JSON responses for easy integration.

Project Structure
fitness-tracker-microservice
 ├── microservice.py        # Flask API handling requests
 ├── test_client.py         # Client script to send fitness data
 ├── README.md              # Documentation

Installation & Setup
1. Install Dependencies
Ensure you have Python 3 installed, then install required packages:
-pip install flask requests

2. Run the Microservice
Start the Flask server:
- python microservice.py
 
It will run at:
-http://127.0.0.1:5000/api/fitness_trends

3.Run the Client
Execute the test client to send sample data:
python test_client.py

API Usage
Endpoint: /api/fitness_trends
Method: POST
Content-Type: application/json

Request Example:
{
    "user_id": "user_1",
    "date_range": {
        "start_date": "2025-02-01",
        "end_date": "2025-02-10"
    },
    "activity_data": [
        {"activity": "running", "duration": 30, "intensity": "high"},
        {"activity": "walking", "duration": 60, "intensity": "medium"},
        {"activity": "cycling", "duration": 45, "intensity": "low"}
    ]
}

Response Example
{
    "fitness_trends": {
        "calories_burned": {
            "current_week": 3500,
            "previous_week": 2900,
            "change": "+20%"
        },
        "steps": {
            "current_week": 70000,
            "previous_week": 68000,
            "change": "+3%"
        }
    },
    "suggestions": [
        "Increase running time by 10%.",
        "Try brisk walking for 10 more minutes."
    ],
    "aggregated_statistics": {
        "total_steps": 135000,
        "total_calories": 6400,
        "hours_exercised": 12
    }
}

