import json
import re

slugs = ["bankruptcy", "concordat"]

PATTERN_BEFORE = r"(?:VKN|[Vv]ergi|VERGİ|VD)[^\d]{0,40}(?<!\d)(\d{10})(?!\d)"
PATTERN_AFTER = r"(?<!\d)(\d{10})(?!\d)\s{0,3}(?:VKN|[Vv]ergi|VERGİ|VD)"
vkn_numbers = []


for slug in slugs:
    with open(f"raw_html/{slug}_details.json", "r", encoding="utf-8") as f:
        details = json.load(f)

    for ad in details:

        matches_before = re.findall(PATTERN_BEFORE, ad["content"])
        matches_after = re.findall(PATTERN_AFTER, ad["content"])
        vkn_numbers.append({"id": ad["id"], "category": slug,"vkn_list": list(set(matches_before + matches_after))})

for r in vkn_numbers:
    print(r)

json.dump(vkn_numbers, open("vkn_numbers.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    