import json

with open('./documents.json', 'rt') as f_in:
    documents_file = json.load(f_in)

documents = []

for course in documents_file:
    course_name = course['course']

    for doc in course['documents']:
        doc['course'] = course_name
        documents.append(doc)

print(len(documents))