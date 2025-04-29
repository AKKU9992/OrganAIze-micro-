# utils.py
import requests

# API endpoint and key (Make sure you keep this key private)
GEMINI_API_KEY = 'AIzaSyD3_uag_gmdRVvwL3sx4jXLUrBZbgMQcAw'
GEMINI_API_ENDPOINT = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

def generate_subtasks_from_api(task_name):
    """
    This function interacts with the Gemini API to generate subtasks.
    The API expects a task name, and will return subtasks with their estimated time.
    """
    # Prepare the request body with task name
    payload = {
        "input": task_name
    }
    
    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json"
    }

    # Call the Gemini API
    response = requests.post(GEMINI_API_ENDPOINT, json=payload, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        response_data = response.json()
        # Parse and return the subtasks from the response
        subtasks = response_data.get('subtasks', [])
        return subtasks
    else:
        # If API call fails, print error and return an empty list
        print("Error in API request:", response.status_code, response.text)
        return []
