from bs4 import BeautifulSoup
import requests

url = ['http://www.justice21.org/newhome/board/board.html?page=1&bbs_code=JS44']

for i in range(2, 5):
    url.append('http://www.justice21.org/newhome/board/board.html?page=' +
               str(i) + '&bbs_code=JS44')

briefinglist = []
reportlist = []

for j in range(0, 4):
    req = requests.get(url[j])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('td.subject')

    for i in title:
        titlelist = []
        titlelist.append(i.a.text)
        titlelist.append(
            'http://www.justice21.org/newhome/board/' + i.a.attrs['href'])
        if titlelist[0].find('보도자료') != -1:
            reportlist.append(titlelist)
        else:
            briefinglist.append(titlelist)