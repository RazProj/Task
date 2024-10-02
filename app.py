from flask import Flask, render_template, send_from_directory
from fetch_json import fetch_json_data
from extract_and_match_URLs import extract_urls_from_messages, enrich_urls_to_data
from organize_and_sort_data import sorting_grouping_data
import threading
import webbrowser
import os

app = Flask(__name__)

# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to serve the JSON data
@app.route('/data')
def serve_data():
    return send_from_directory('static', 'sorted_enriched_data.json')

def open_browser():
    # Open the browser to the Flask server URL
    webbrowser.open_new("http://127.0.0.1:5000/")
    # Optionally shut down the server after some time (not necessary for development)
    threading.Timer(5, shutdown_server).start()

def shutdown_server():
    print("Shutting Down")
    os._exit(0)

if __name__ == '__main__':
    # Ensure we don't re-run the server when in reloader mode
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        messages_url = 'https://cdn.taboola.com/mobile-config/home-assignment/messages.json'
        data_url = 'https://cdn.taboola.com/mobile-config/home-assignment/data.json'

        # Fetch, extract, and enrich data
        messages = fetch_json_data(messages_url)
        data = fetch_json_data(data_url)
        extracted_urls = extract_urls_from_messages(messages)
        enriched_data = enrich_urls_to_data(extracted_urls, data)

        # Save sorted and grouped data to the JSON file
        output_file = os.path.join('static', 'sorted_enriched_data.json')
        sorting_grouping_data(enriched_data, output_file)

        # Start a thread to open the browser after the server starts
        threading.Timer(1, open_browser).start()

    # Run the Flask app
    app.run(debug=True)
