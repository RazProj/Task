import json
from collections import defaultdict

def sort_data_by_country_and_fix_est_emp(data):

    invalid_est_emp = {}

    # Iterate through each entry in the data list
    for entry in data:
        # Check if the 'est_emp' key is missing, or if the value of 'est_emp' is not an integer, or if it is a negative integer
        if 'est_emp' not in entry or not isinstance(entry['est_emp'], int) or entry['est_emp'] < 0:

            # Handles values that are digits in a form of string 
            if isinstance(entry['est_emp'], str):
                if entry['est_emp'].isdigit():
                    entry['est_emp'] = int(entry['est_emp'])
                    continue

            # Print a message indicating that the 'est_emp' value for this entry is invalid, and set the field to 0 for the sorting operation.
            invalid_est_emp[entry['name']] = entry['est_emp']
            entry['est_emp'] = 0 

    # Sort the data list by the 'country' field in alphabetical order, ignoring case sensitivity
    sorted_data = sorted(data, key=lambda x: (x['country'].lower()))

    return sorted_data, invalid_est_emp

def grouping_by_country_sorting_by_employees(data):

    # Create a dictionary where the key is the country and the value is a list of entries for that country
    country_dict = defaultdict(list)
    
    # Group the data by country, adding each entry to its corresponding country in the dictionary
    for entry in data:
        country = entry['country'].lower()
        country_dict[country].append(entry)
    
    # Sort the entries within each country by the number of employees ('est_emp') in descending order
    for country, country_list in country_dict.items():
        country_dict[country] = sorted(country_list, key=lambda x: x['est_emp'], reverse=True)

    # Convert the dictionary into a list of lists, where each sublist contains all the entries for a particular country
    organized_data = [country_list for country_list in country_dict.values()]
    
    return organized_data

def sorting_grouping_data(data, output_file):

    # Correct any invalid 'est_emp' values, sort the data by country, and return the processed data.
    # Also, collect and return entries with invalid 'est_emp' values for later display.
    sorted_data, invalid_est_emp = sort_data_by_country_and_fix_est_emp(data)
    
    # Group the data by the country and sort the groups by the number of employees
    sorted_data = grouping_by_country_sorting_by_employees(sorted_data)
    
    # Restore the original invalid 'est_emp' values from the invalid_est_emp dictionary
    for group in sorted_data:
        for entry in group:
            if entry['name'] in invalid_est_emp:
                entry['est_emp'] = invalid_est_emp[entry['name']]

    try:
        # Write the organized data into a JSON file
        with open(output_file, 'w') as file:
            json.dump(sorted_data, file, indent=4)
        print(f"Reorganized data saved to {output_file}")

    except IOError as e:
        print(f"Error saving data to {output_file}: {e}")
