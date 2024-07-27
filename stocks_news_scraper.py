# Import Libraries
import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, tag, class_, max_headlines=20):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Initialize a counter variable
        count = 1

        # Use a for loop to extract and print the headlines
        for headline in soup.find_all(tag, class_=class_):
            print(f"{count}. {headline.text.strip()}")
            count += 1

            # Break out of the loop after printing the desired number of headlines
            if count > max_headlines:
                break

    else:
        print(f"Failed to retrieve the page for {url}. Status code: {response.status_code}")

# Define sources
sources = [
    {'name': 'CNBC', 'url': 'https://www.cnbc.com/latest/', 'tag': 'a', 'class': 'Card-title'},
    {'name': 'ZeroHedge', 'url': 'https://www.zerohedge.com/', 'tag': 'h2', 'class': 'Article_title___TC6d Article_lineClamp__yljIN'},
    {'name': 'CoinDesk', 'url': 'https://www.coindesk.com/livewire/','tag': 'div', 'class': 'card-title'},
    {'name': 'Yahoo Crypto', 'url': 'https://finance.yahoo.com/topic/crypto/', 'tag': 'h3', 'class': 'Mb(5px)'}
]

# Loop through sources and scrape headlines
for source in sources:
    print(f"\n{source['name']} headlines:")
    scrape_headlines(source['url'], source['tag'], source['class'])
