import csv
import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = []
labels = []
labeled_list = []

with open("training_data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        labeled_list.append({"id": row["id"], "title": row["title"], "label": row["label"]})

with open("raw_html/concordat_details.json", "r", encoding="utf-8") as f:
    details = json.load(f)

content_lookup = {ad["id"]: ad["content"] for ad in details}

for item in labeled_list:
    content_lookup[item["id"]] = re.sub(r"<[^>]+>", " ", content_lookup[item["id"]])
    texts.append(item["title"] + " " + content_lookup[item["id"]])
    labels.append(item["label"])


# print(labeled_list[0])
# print(content_lookup[labeled_list[0]["id"]][:100])
# print(texts[0])
# print(labels[0])

vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(x, labels)

new_texts = ["Konkordato süresinin arttırılmasına dair karar"]
new_X = vectorizer.transform(new_texts)
prediction = model.predict(new_X)
print(prediction)

probs = model.predict_proba(new_X)
for label, prob in zip(model.classes_, probs[0]):
    print(label, round(prob, 2))

vocab = vectorizer.vocabulary_
idf = vectorizer.idf_

for word in ["konkordato", "uzatılmasına", "arttırılmasına"]:
    if word in vocab:
        print(word, "IDF:", round(idf[vocab[word]], 2))
    else:
        print(word, "not found in vocabulary")