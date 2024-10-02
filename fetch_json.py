import requests

def fetch_json_data(url):
    try:
        # Attempt to fetch the data from the given URL with a 15-second timeout
        response = requests.get(url, timeout=15)
        # Raise an exception if the HTTP response status indicates an error
        response.raise_for_status()
        # Parse the response data
        json_data = response.json()
        return json_data
    except requests.exceptions.RequestException as e:
        # Print an error message if there was an issue with the request
        print(f"Error fetching data: {e}")
        # Return None to indicate that data couldn't be fetched
        return None
