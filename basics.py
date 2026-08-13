import requests
import truststore
truststore.inject_into_ssl()
import os
import json

API_URL = "https://www.ilan.gov.tr/api/api/services/app/Ad/AdsByFilter"
category_list = [
    {"name": "İflas Hukuku Davaları", "url": "https://www.ilan.gov.tr/ilan/kategori/50/iflas-ve-tasfiye-ilanlari", "slug": "bankruptcy", "tax_id": 50},
    {"name": "Konkordato ve Mühlet", "url": "https://www.ilan.gov.tr/ilan/kategori/49/konkordato-ve-muhlet-iik-288inci-md", "slug": "concordat", "tax_id": 49}
]

print(os.getcwd()) 
for category in category_list:
    payload ={"keys": {"txv": [category['tax_id']]}, "skipCount": 0, "maxResultCount": 20}
    response = requests.post(API_URL, json=payload)
    print(f"Category Name: {category['name']}, URL: {category['url']}, Status Code: {response.status_code}")
    data = response.json()

    with open(f"raw_html/{category['slug']}.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        print(os.path.abspath(f"raw_html/{category['slug']}.json"))