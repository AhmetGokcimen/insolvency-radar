import requests
import truststore
truststore.inject_into_ssl()
import os

category_list = [
    {"name": "İflas Hukuku Davaları", "url": "https://www.ilan.gov.tr/ilan/kategori/50/iflas-ve-tasfiye-ilanlari", "slug": "bankruptcy"},
    {"name": "Konkordato ve Mühlet", "url": "https://www.ilan.gov.tr/ilan/kategori/51/konkordato-ve-muhlet", "slug": "concordat"}
]

print(os.getcwd()) 
for category in category_list:
    response = requests.get(category['url'])
    print(f"Category Name: {category['name']}, URL: {category['url']}, Status Code: {response.status_code}")

    with open(f"raw_html/{category['slug']}.html", "w", encoding="utf-8") as f:
        f.write(response.text)
        print(os.path.abspath(f"raw_html/{category['slug']}.html"))