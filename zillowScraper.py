import requests
from bs4 import BeautifulSoup

# Set the URL of the Zillow page you want to scrape
url = "https://www.zillow.com/boston-ma/sold/"

# Send an HTTP GET request to the URL
response = requests.get(url)
print(response.content)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the relevant elements containing the data you want to scrape
results = soup.find_all("article", class_="property-card-data")
print(results)

# Loop through each result and extract the desired information
for result in results:
    # Extract the bedroom information
    bedrooms = result.find("ul", class_="list-card-details").find("li").text.strip()

    # Extract the square footage
    square_footage = result.find("ul", class_="list-card-details").find_all("li")[1].text.strip()

    # Extract the price
    price = result.find("div", class_="list-card-price").text.strip()

    # Print the scraped data
    print("Bedrooms:", bedrooms)
    print("Square Footage:", square_footage)
    print("Price:", price)
    print()

"""
import requests
from bs4 import BeautifulSoup

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', 'referer':'https://www.zillow.com/homes/Missoula,-MT_rb/'}

data = requests.get('https://www.zillow.com/boston-ma/sold/', headers=header)

data = requests.get('https://www.zillow.com/boston-ma/sold/')
soup = BeautifulSoup(data.text, "lxml")

size = [elem.find("strong").text for elem in soup.find_all("span", {'data-testid': 'bed-bath-item'})[:2]]

sz=[]
for result in size:
    sz.append(sz.text)

print(sz)
"""