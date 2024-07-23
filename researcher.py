import requests
from bs4 import BeautifulSoup
from googlesearch import search

class Researcher:
    def __init__(self, company_name):
        self.company_name = company_name
        self.log_file = f"{company_name}_actions_log.txt"
        self.report_file = f"{company_name}_research_report.txt"
        self.log_actions(f"Initialized researcher for {company_name}")

    def log_actions(self, action):
        with open(self.log_file, 'a', encoding='utf-8') as log:
            log.write(f"{action}\n")

    def google_search(self, query, num_results=10):
        search_results = []
        self.log_actions(f"Searching Google for: {query}")
        for result in search(query, num_results=num_results):
            search_results.append(result)
        self.log_actions(f"Found {len(search_results)} results")
        return search_results

    def get_news_from_url(self, url):
        headers = {'User-Agent': 'Mozilla/5.0'}
        self.log_actions(f"Fetching news from URL: {url}")
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            return ' '.join([paragraph.get_text() for paragraph in paragraphs])
        return None

    def gather_data(self):
        query = f"{self.company_name} stock news"
        search_results = self.google_search(query)
        news_articles = []
        for url in search_results:
            article = self.get_news_from_url(url)
            if article:
                news_articles.append(article)
        return news_articles

    def create_report(self):
        self.log_actions(f"Creating report for {self.company_name}")
        news_articles = self.gather_data()
        with open(self.report_file, 'w', encoding='utf-8') as report:
            report.write(f"Research Report for {self.company_name}\n\n")
            for i, article in enumerate(news_articles, start=1):
                report.write(f"Article {i}:\n{article}\n\n")
        self.log_actions(f"Report created: {self.report_file}")

# Przykład użycia:
# researcher = Researcher("Apple Inc")
# researcher.create_report()
