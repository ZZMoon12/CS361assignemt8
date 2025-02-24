from flask import Flask, request, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# Sample function to generate fitness trends
def generate_fitness_trends(activity_data):
    trends = {
        "calories_burned": {
            "current_week": random.randint(300, 400),
            "previous_week": random.randint(200, 300),
            "change": f"{random.randint(5, 20)}%"
        },
        "steps": {
            "current_week": random.randint(600, 800),
            "previous_week": random.randint(500, 700),
            "change": f"{random.randint(3, 15)}%"
        }
    }
    return trends

# Sample function to generate personalized suggestions
def generate_suggestions(activity_data):
    suggestions = []
    for activity in activity_data:
        if activity["activity"] == "running":
            suggestions.append("Increase your running distance by 10%.")
        elif activity["activity"] == "walking":
            suggestions.append("Try brisk walking for 10 more minutes.")
        elif activity["activity"] == "cycling":
            suggestions.append("Increase cycling speed for better endurance.")
    return suggestions if suggestions else ["Maintain your current routine."]

# Sample function to calculate aggregated statistics
def calculate_aggregated_statistics(activity_data):
    total_steps = sum(random.randint(500, 1000) for _ in activity_data)
    total_calories = sum(random.randint(200, 500) for _ in activity_data)
    hours_exercised = sum(activity["duration"] for activity in activity_data) / 60
    return {
        "total_steps": total_steps,
        "total_calories": total_calories,
        "hours_exercised": round(hours_exercised, 2)
    }

@app.route('/api/fitness_trends', methods=['POST'])
def fitness_trends():
    try:
        data = request.get_json()
        
        # Validate request data
        if "user_id" not in data or "date_range" not in data or "activity_data" not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
        user_id = data["user_id"]
        date_range = data["date_range"]
        activity_data = data["activity_data"]

        # Validate date range
        if "start_date" not in date_range or "end_date" not in date_range:
            return jsonify({"error": "Invalid date range format"}), 400

        start_date = datetime.strptime(date_range["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(date_range["end_date"], "%Y-%m-%d")
        
        if start_date > end_date:
            return jsonify({"error": "Start date cannot be after end date"}), 400

        # Generate response data
        response_data = {
            "fitness_trends": generate_fitness_trends(activity_data),
            "suggestions": generate_suggestions(activity_data),
            "aggregated_statistics": calculate_aggregated_statistics(activity_data)
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
