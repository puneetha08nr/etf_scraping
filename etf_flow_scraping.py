import csv
import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://farside.co.uk/?p=1321'

# Make an HTTP GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the data you want to scrape (this will vary depending on the structure of the website)
    # For example, let's say we want to scrape a table with `id` attribute 'data-table'
    table = soup.find('table', {'class': 'etf'})

    # Find all rows in the table (assuming the first row contains headers)
    rows = table.find_all('tr')

    # Open a CSV file for writing
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Write the headers to the CSV file
        headers = [header.text for header in rows[0].find_all('th')]
        csvwriter.writerow(headers)

        # Write the data to the CSV file
        for row in rows[2:]:  # Skip the header row
            data = [cell.text for cell in row.find_all('td')]
            csvwriter.writerow(data)

    print('Data has been written to output.csv')
else:
    print(f'Failed to retrieve webpage: status code {response.status_code}')
