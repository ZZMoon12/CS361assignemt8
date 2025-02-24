import requests
import json  # Import json for formatting

url = "http://127.0.0.1:5000/api/fitness_trends"

request_data = {
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

response = requests.post(url, json=request_data)

if response.status_code == 200:
    # Parse JSON response and print it in a readable format
    response_data = response.json()

    print("\n=== Fitness Trends ===")
    for key, value in response_data["fitness_trends"].items():
        print(f"{key.capitalize()}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key.replace('_', ' ').capitalize()}: {sub_value}")

    print("\n=== Suggestions ===")
    for suggestion in response_data["suggestions"]:
        print(f"- {suggestion}")

    print("\n=== Aggregated Statistics ===")
    for key, value in response_data["aggregated_statistics"].items():
        print(f"{key.replace('_', ' ').capitalize()}: {value}")

else:
    print(f"Error: {response.status_code}, {response.text}")

