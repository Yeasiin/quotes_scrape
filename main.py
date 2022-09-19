import requests
import bs4 

author_list = set()
quotes_list = []
tags_list = set()

page = 1

while True:
    response = requests.get(f'http://quotes.toscrape.com/page/{page}/')
    soap = bs4.BeautifulSoup(response.text,'lxml')
    page += 1

    if 'No quotes found!' in soap.text:
        break

    for author in soap.select('.author'):
        author_list.add(author.text +'\n') 

    for quote in soap.select('.quote > span.text'):
        quotes_list.append(quote.text +'\n') 

    for tag in soap.select('.tag-item > .tag'):
        tags_list.add(tag.text +'\n')

    
    

with open('./file/authors.txt','w') as t:
    t.write("".join(author_list))

with open('./file/quotes.txt','w',encoding='utf-8') as t:
    t.write("".join(quotes_list))

with open('./file/tags.txt','w') as t:
    t.write("".join(tags_list))
