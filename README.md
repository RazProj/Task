taboola-task/
│
├── static/
│   ├── css/
│   │   └── styles.css               # Contains the styles for the webpage
│   ├── js/
│   │   └── script.js                # Contains the JavaScript logic to dynamically load and render data into the HTML page
│   └── sorted_enriched_data.json    # The enriched data that will be displayed on the webpage
│
├── templates/
│   └── index.html                   # The HTML template for the webpage
│
├── app.py                           # The main application file that runs Flask and handles the backend logic
│
├── extract_and_match_URLs.py        # Module to extract URLs from messages and match them with enriched data
│
├── fetch_json.py                    # Module to fetch JSON data from remote URLs
│
├── organize_and_sort_data.py        # Module to sort and group the enriched data by country and employee
│
└── README.md                        # Project documentation

Installing Requirements
* Python 3
* Flask 
* Requests 

How To Run
* Insure you installed the requirements
* Open the project on VScode or navigate throught the CMD to the main folder
* On VScode open the 'app.py' file and run as usual
* Through the CMD write ' python app.py '


