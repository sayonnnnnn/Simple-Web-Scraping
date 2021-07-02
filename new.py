from bs4 import BeautifulSoup 
import requests

html_text = requests.get('https://internshala.com/internships/matching-preferences').text
soup = BeautifulSoup(html_text, 'lxml')
internships = soup.find_all('div', id='internship_list_container_1')
# for internship in internships:
# 	print(internship.text.replace(' ',''))

companies = soup.find_all('div', class_='heading_6 company_name')
profiles = soup.find_all('div', class_='heading_4_5 profile')

print('Companies that are providing internships are as follows:- \n')
for company in companies:
	print(company.text.replace(' ',''))



