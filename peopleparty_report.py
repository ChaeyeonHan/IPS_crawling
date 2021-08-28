from bs4 import BeautifulSoup
import requests

url = ['https://peopleparty.kr/press?sca=%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C']

for i in range(2, 5):
    url.append(
        'https://peopleparty.kr/press?sca=%EB%B3%B4%EB%8F%84%EC%9E%90%EB%A3%8C&page=' + str(i))
finallist = []

for j in range(0, 4):
    req = requests.get(url[j])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('.tit')

    for i in title:
        titleList = []
        titleList.append(i.a.text)
        titleList.append(i.a.attrs['href'])
        finallist.append(titleList)