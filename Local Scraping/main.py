from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
	content = html_file.read()
	soup = BeautifulSoup(content, 'lxml')
	
	
	print(soup.prettify())

	tags = soup.find_all('p')
	for tag in tags:
		print(tag.text) 

	div_tags = soup.find_all('div', class_='container')
	for div_tag in div_tags:
		print(div_tag)
		print('********')
		print(div_tag.h2)
		print('********')
		# print(div_tags.h4) # Gives error as there are no H4 tags under a div called container!!
		h2_content = div_tag.h2.text
		print(h2_content)
		print('********')

