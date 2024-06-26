# -*- coding: utf-8 -*-
"""Organic Result Scraper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WlCXonQrcLPpbXl47QayfS65GnaKnSqt
"""

import time
import requests
from bs4 import BeautifulSoup
import csv
import random
import re
from urllib.parse import urlparse, parse_qs, urlunparse


user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.0.0',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1',
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
]

def format_keywords_from_csv(file_name):
    keywords = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            keywords.append(row[0])
    return keywords

def clean_url(url):
    return re.split('&sa=|\?hl=|/url\?q=|#:~:', url)[0]

def find_next_heading(soup, current_heading):
    next_heading = current_heading.find_next('h3')
    if not next_heading:
        raise ValueError("No more headings found in the page")
    return next_heading

def write_to_csv(file_name, data):
    with open(file_name, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Keyword', 'Cleaned URL'])
        for row in data:
            csvwriter.writerow(row)

def find_valid_link(soup, heading_object):
    while True:
        parent_a_tag = heading_object.find_parent('a')
        if parent_a_tag and parent_a_tag.has_attr('href'):
            return parent_a_tag.get('href')

        try:
            heading_object = find_next_heading(soup, heading_object)
        except ValueError:
            raise ValueError("No valid link found for any heading")

def main():
    file_name = 'keywords.csv'
    keywords = format_keywords_from_csv(file_name)

    output_data = []

    for query in keywords:
        try:
            headers = {'User-Agent': random.choice(user_agents)}
            url = f"https://www.google.com/search?q={query}"
            response = requests.get(url, headers=headers)

            # Check if response was successful
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            heading_object = soup.find('h3')
            if not heading_object:
                raise ValueError("No heading found in page")

            href = find_valid_link(soup, heading_object)
            cleaned_link = clean_url(href)

            # Check if the cleaned link ends with "/url?esrc=s&q=&rct=j" or starts with "search?"
            while cleaned_link.endswith("/url?esrc=s&q=&rct=j") or cleaned_link.startswith("/search?"):
                # Find the next heading
                heading_object = find_next_heading(soup, heading_object)
                href = find_valid_link(soup, heading_object)
                cleaned_link = clean_url(href)

            output_data.append([query, cleaned_link])
            print(f"SUCCESS: {query}")  # Print success message
        except requests.exceptions.HTTPError as http_err:
            status_code = http_err.response.status_code
            if status_code == 429:  # Rate limit error
                retry_after = http_err.response.headers.get("Retry-After")
                wait_time = int(retry_after) if retry_after else 10  # Default to 10 seconds if not specified
                print(f"Rate limited. Waiting for {wait_time} seconds.")
                time.sleep(wait_time)
            else:
                print(f"HTTP error occurred: {http_err}")
        except requests.exceptions.ConnectionError:
            print("Failed to connect to the server.")
        except requests.exceptions.Timeout:
            print("Request timed out.")
        except ValueError as ve:
            print(f"Scraping error for query '{query}': {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            write_to_csv('output.csv', output_data)
            time.sleep(2)  # Fixed 2-second delay after each query

if __name__ == '__main__':
    main()