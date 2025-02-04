import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape
url = "https://quotes.toscrape.com"

# Send an HTTP request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all quotes
    quotes = soup.find_all("div", class_="quote")

    # Open a CSV file to save data
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author"])  # Header row

        # Loop through quotes and save them
        for quote in quotes:
            text = quote.find("span", class_="text").text.strip()
            author = quote.find("small", class_="author").text.strip()
            writer.writerow([text, author])  # Write to CSV

    print("Quotes saved to quotes.csv")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")

