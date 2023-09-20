import requests
from bs4 import BeautifulSoup

# URL of the page you want to scrape
url = 'https://www.chainabuse.com/chain/SOL?page=1'  # Replace with the actual URL

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all div elements with the specified class name
    div_elements = soup.find_all('div', class_='create-ResponsiveAddress__text')

    # Iterate through each div element and extract the text
    for div in div_elements:
        text = div.get_text()
        print(text)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
