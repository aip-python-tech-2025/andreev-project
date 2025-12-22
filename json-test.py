import json

f = open('books.json', 'r', encoding='utf-8')
data = json.load(f)
f.close()

print(data['count'])
print(data['results'][0]['title'])

data['results'][0]['title'] = 'Франкенштейн'

f = open('books-updated.json', 'w', encoding='utf-8')
json.dump(data, f, indent=2, ensure_ascii=False)
f.close()
