import re

# Extracting valid URLs from messages using a regular expression
def extract_urls_from_messages(messages):

    # List of the extracted URLs
    urls = []

    # Removing duplicates URLs
    duplicates_dict = set()

    # A valid URL pattern that starts with 'www.', is followed by at least one non-whitespace character, and ends with '.com'
    url_pattern = re.compile(r'www\.\S+\.com')

    # Iterating over each message to extract the URL from the 'url' key in the 'link' object
    for message in messages:
        # Check if the message contains '_source' and 'message' keys
        if '_source' in message and 'message' in message['_source']:
            # Loop through each message inside the 'message' list
            for message in message['_source']['message']:
                # Check if the 'link' and 'url' fields exist in the message
                if 'link' in message and 'url' in message['link']:
                    url = message['link']['url']
                    # Ensure the URL is not empty
                    if url:
                        # Apply the regular expression to match valid URL
                        match = url_pattern.search(url)    
                        if match:  
                            # Extract the matched URL part
                            extracted_url = match.group(0)
                            # Prepend 'https://' to the extracted URL to make it complete
                            final_url = 'https://' + extracted_url
                            # Ensure the URL is not already in the duplicates set
                            if final_url not in duplicates_dict:
                                duplicates_dict.add(final_url)
                                urls.append(final_url)

    return urls

def enrich_urls_to_data(urls, data):
    enrich_list = []
    
    # Iterate over each URL in the extracted URLs list
    for url in urls:
        # For each URL, search the data entries
        for entry in data:
            # If URL matches the entry's URL field
            if url == entry['url']:
                # Create a dictionary of the enriched data
                temp = {
                    'url': entry['url'],
                    'name': entry['name'],
                    'est_emp': entry['est_emp'],
                    'industry': entry['industry'],
                    'annual_rev': entry['annual_rev'],
                    'country': entry['country']
                }
                # Add the enriched entry to the list
                enrich_list.append(temp)
                # break
    
    # Return the enriched list
    return enrich_list