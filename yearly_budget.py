import os
import requests
import datetime
import pandas as pd
from requests_html import HTML

BASE_DIR = os.path.dirname(__file__)

def read_url(url, name, save=False):
	r = requests.get(url)
	if r.status_code == 200:
		html_text = r.text
		if save:
			with open(f"world-{name}.html", 'w') as f:
				f.write(html_text)
		return html_text

	return ""

def parse_and_extract(url, name):
	r_txt = read_url(url, name)
	r_html = HTML(html=r_txt)
	table_class = '.imdb-scroll-table'
	r_table = r_html.find(table_class)

	table_data = []
	header_names = []
	if len(r_table) == 1:
		parsed_table = r_table[0]
		rows = parsed_table.find("tr")
		header_row = rows[0]
		header_cols = header_row.find('th')
		header_names = [x.text for x in header_cols]
		for row in rows[1:]:
			cols = row.find("td")
			row_data = []
			for i, col in enumerate(cols):
				row_data.append(col.text)

			table_data.append(row_data)
	
	df = pd.DataFrame(table_data, columns=header_names)
	path = os.path.join(BASE_DIR, 'data')
	os.makedirs(path, exist_ok=True)
	filepath = os.path.join('data', f"world-{name}.csv")
	df.to_csv(filepath, index=False)



if __name__ == "__main__":
	year = 2016
	url = f'https://www.boxofficemojo.com/year/world/{year}/'

	parse_and_extract(url, year)
