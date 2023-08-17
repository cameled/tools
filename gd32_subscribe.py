import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta

def resource_check(since, url, name):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'html.parser')
	# Get total page number from 'pagination' class.
	pagination_text = soup.find('ul', class_='pagination')
	last_page_text = pagination_text.find('li', class_="last")
	total_page_num = last_page_text.find('a')['href'].split('/')[-1]

	for i in range(0, int(total_page_num)):
		page_url = url + "/p/" + str(i + 1)
		response = requests.get(page_url)
		soup = BeautifulSoup(response.text, 'html.parser')
		# Get resources list from 'sheet-data' class.
		sheet_data = soup.find('ul', class_='sheet-data')

		for li in sheet_data.find_all('li', class_='cl'):
			data_time = li.find('dd', class_='data-time')
			data_name = li.find('dd', class_='data-name')
			data_version = li.find('dd', class_='data-version')

			# Ignored if name not match.
			if name not in data_name.text:
				continue

			if since < datetime.strptime(data_time.text, '%Y-%m-%d').date():
				print("{}    v{}    {}".format(data_name.text, data_version.text, data_time.text))
			else:
				return

def main():
	current = datetime.today().date()

	# Default resource check time, 1 month.
	since = current - relativedelta(months=1)

	resource_check(since, 'https://www.gd32mcu.com/en/download/5', 'Datasheet')
	resource_check(since, 'https://www.gd32mcu.com/en/download/6', 'User Manual')
	resource_check(since, 'https://www.gd32mcu.com/en/download/7', 'Firmware Library')

if __name__ == '__main__':
	main()

