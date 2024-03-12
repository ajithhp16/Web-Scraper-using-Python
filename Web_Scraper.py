import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import csv


class Web_Scraper:

	"""
	Create object for this class.
	
	web_scraper_urls => CSV file containing three fields:
						1. Name
						3. URL
						3. Parser
	scraper_tags	 => CSV file containing two fields:
						1. Tags like div, p, h1,.. whose data to be scraped.
						2. Class name of the tag whose data to be scraped.
						
	Call web_scrape_results(web_scraper_urls, scraper_tags).
		Result will be in 'self.results' variable, columns=['Name', 'Metadata', 'Content'].
		
	Call scraped_results_to_csv(filename) to store the 'self.results' data into the CSV file.
		Columns=['Name', 'Metadata', 'Content'].
	"""
	
	def complete_scrape(self, repo_link, parser):
		res = requests.get(repo_link)
		repo_soup = BeautifulSoup(res.content, parser)
		return repo_soup
		
	def tag_scraper(self, repo, tag, cl):
		ls = []
		for i in repo.findAll(tag, class_=cl):
			a = i.text.strip()
			header = a.split("\n")[0].split(".")[0]
			content = re.sub(r"\n+", "\n", a.replace("  ", ""))
			ls.append([header, content])
		return ls
		
	def scraper_results(self, scraper_tags, repo_soup, name):
		tags_data = pd.read_csv(scraper_tags)
		header = []
		content = ""
		for index, row in tags_data.iterrows():
			res = self.tag_scraper(repo_soup, row["tag"], row["class_of_tag"])
			if len(res) > 0:
				for scr in res:
					header.append(scr[0].strip())
					content += "\n" + scr[1].strip()
					final_header = " || ".join(header)
		return [name, final_header, content]
		
	def web_scrape_results(self, web_scraper_urls, scraper_tags):
		final_results = []
		web_urls = pd.read_csv(web_scraper_urls)
		for index, row in web_urls.iterrows():
			name = row["name"]
			repo_soup = self.complete_scrape(row["web_url"], row["parser"])
			final_results.append(self.scraper_results(scraper_tags, repo_soup, name))
		self.results = final_results
		
	def scraped_results_to_csv(self, filename):
		results_df = pd.DataFrame(self.results, columns=["Name", "Metadata", "Content"])
		results_df.to_csv(filename, index=False)