import excel2json
import json,re,os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
print(THIS_FOLDER)

# excel2json.convert_from_file(THIS_FOLDER+'/book_writers.xlsx')

with open(THIS_FOLDER+'/Sheet1.json', encoding="utf-8") as f:
    data = json.load(f)
    # json.dumps(data, indent=4, ensure_ascii=False).encode('utf8')

print(data[0])


# with open('data.json', 'w') as outfile:
#     str = json.dumps(data, indent=4, ensure_ascii=False).decode('utf8')
#     outfile.write(bytes(str,'utf-8'))
#     outfile.close()




# print(data[0]["Name "])

