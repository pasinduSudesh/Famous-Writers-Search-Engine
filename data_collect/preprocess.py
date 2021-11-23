import json,re,os
import codecs

CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

book_writer_raw_data = json.load(codecs.open(CURRENT_FOLDER+'/book_writers_raw_data.json','r', 'utf-8-sig'))


# print(book_writer_raw_data)

for writer in book_writer_raw_data["writers"]:
    # Preprocess writer name
    if 'writer_name' in writer:
        writer["writer_name"] = writer["writer_name"].strip()
    else:
        writer["writer_name"] = None
    
    # Preprocess writer Date of Birth
    if 'writer_name_eng' in writer:
        writer["writer_name_eng"] = writer["writer_name_eng"].strip()
    else:
        writer["writer_name_eng"] = None

            # Preprocess writer Date of Birth
    if 'writer_dob' in writer:
        writer["writer_dob"] = writer["writer_dob"].strip()
    else:
        writer["writer_dob"] = None

    # Preprocess writer birth place
    if 'writer_birth_place' in writer:
        writer["writer_birth_place"] = writer["writer_birth_place"].strip()
    else:
        writer["writer_birth_place"] = None

    # Preprocess writer birth place
    if 'writer_birth_place_eng' in writer:
        writer["writer_birth_place_eng"] = writer["writer_birth_place_eng"].strip()
    else:
        writer["writer_birth_place_eng"] = None

    # Preprocess writer birth education details
    if 'education' in writer:
        writer["education"] = list(map(str.strip,writer["education"].strip().split(",")))
    else:
        writer["education"] = []

    # Preprocess writer wrote book list
    if 'book_list' in writer:
        writer["book_list"] = list(map(str.strip,writer["book_list"].strip().split(",")))
    else:
        writer["book_list"] = []
  
    # Preprocess writer language
    if 'writtern_language' in writer:
        writer["writtern_language"] = list(map(str.strip,writer["writtern_language"].strip().split(",")))
    else:
        writer["writtern_language"] = []

    # Preprocess writer wrote book categories
    if 'wrote_categories' in writer:
        writer["wrote_categories"] = list(map(str.strip,writer["wrote_categories"].strip().split(",")))
    else:
        writer["wrote_categories"] = []

    # Preprocess writer LIFE STORY
    if 'writer_life_story' in writer:
        writer["writer_life_story"] = writer["writer_life_story"].strip()
    else:
        writer["writer_life_story"] = None

with open(CURRENT_FOLDER+'/../data/book_writers.json', 'w', encoding='utf-8') as f:
    json.dump(book_writer_raw_data, f,ensure_ascii=False) 


