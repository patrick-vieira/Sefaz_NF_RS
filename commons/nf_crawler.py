import requests
from bs4 import BeautifulSoup


def hello():
    req = requests.get("http://httpbin.org/get")
    return req


def get_data(nf_url):

    source_code = requests.get(nf_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    conteudo = "#iframeConteudo"

    for obj in soup.select(conteudo):
        a = obj.get('src')

    return second_req(a)


def second_req(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    nf_data = []
    nf_data_struct = []

    for td in soup.find_all('td', {'class':'borda-pontilhada-botton'}):
        nf_data.append(td.text)
        nf_data_struct.append(td)

    return nf_data_struct
