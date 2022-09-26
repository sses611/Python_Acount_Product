# 모든 금융사 상품의 상품명, 금리, 기간, 이자율을 탐색하여 적합한 조건의 상품 검색 프로젝트
from requests import get
from bs4 import BeautifulSoup

URL = "https://www.kebhana.com/cont/mall/mall08/mall0805/index.jsp?_menuNo=62608"

response = get(URL)

if response.status_code != 200:
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.find_all("ul", class_='product-list')
    for product in products:
        contents = product.select('li', reclusive=False)
        for content in contents:
            print(content)
            print("//////////////////////////\n")
