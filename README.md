# Web-Scraper-using-Python

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
