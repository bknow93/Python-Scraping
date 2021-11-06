from bs4 import BeautifulSoup
#Download BeautifulSoup library at later date

#home.html is example page, fill in later
with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())