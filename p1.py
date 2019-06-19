import requests
from  bs4 import BeautifulSoup


def download_page(url=None):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("请求错误!")
        return None


def parse_page(text=None):
    if text:
        soup = BeautifulSoup(text,features="lxml")
        lst = [ link for link in soup.find_all('a')]
        dct = {}
        for l in lst:
            dct[l.get('href')] = l.get_text()
        for k,v in dct.items():
            print(f"{k}------>>>>>>>:{v}")
        return dct
    else:
        print("待解析文件为空!")
        return None



if __name__ == "__main__":
    baseUrl = "https://www.gushiwen.org/index.aspx"
    text = download_page(baseUrl)
    if text:
        dct = parse_page(text)
    else:
        print("待解析文件为空!")
    