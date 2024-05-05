# Import required libraries
import requests
from bs4 import BeautifulSoup
import time
import re

# Define the Twitter accounts to scrape
twitter_accounts = [
    "https://twitter.com/Mr_Derivatives",
    "https://twitter.com/warrior_0719",
    "https://twitter.com/ChartingProdigy",
    "https://twitter.com/allstarcharts",
    "https://twitter.com/yuriymatso",
    "https://twitter.com/TriggerTrades",
    "https://twitter.com/AdamMancini4",
    "https://twitter.com/CordovaTrades",
    "https://twitter.com/Barchart",
    "https://twitter.com/RoyLMattox"
]

# Define the stock symbol to look for
stock_symbol = "$TSLA"

# Define the time interval for scraping (in seconds)
time_interval = 5

# Function to scrape Twitter page
def scrape_twitter_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tweets = soup.find_all('div', {'class': 'tweet'})
    mentions = []
    for tweet in tweets:
        text = tweet.find('p', {'class': 'tweet-text'}).text
        mentions.extend(re.findall(r'\$[A-Z]{3,4}', text))
    return mentions

# Function to count mentions of stock symbol
def count_mentions(mentions, stock_symbol):
    return mentions.count(stock_symbol)

# Main function
def main():
    while True:
        mentions = []
        for account in twitter_accounts:
            mentions.extend(scrape_twitter_page(account))
        count = count_mentions(mentions, stock_symbol)
        print(f"'{stock_symbol}' was mentioned '{count}' times in the last '{time_interval}' seconds.")
        time.sleep(time_interval)  # sleep for X seconds

if __name__ == "__main__":
    main()