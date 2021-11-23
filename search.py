from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import json,re,os
import queries

client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'famous-writers'

def search(search_query):

    writer_synonyms_sin = ['රචකයා', 'ගත්කරු', 'රචිත', 'ලියූ', 'ලියපු', 'ලියන්නා', 'රචිත', 'රචනාකල']
    writer_synonyms_eng = ['writer', 'wrote', 'auther','litterateur' ]

    dob_synonyms_sin = ['උපන්', 'ඉපදුනු', 'දීඋපන්', 'උපන්න', 'ඉපදී']
    dob_synonyms_eng = ['born', 'date', 'birth']

    education_synonyms = ['ඉගෙනගත්', 'අධ්‍යාපනය ලැබූ']

    book_synonyms = ['පොත්', 'පොත', 'ග්‍රන්ථය', 'ග්‍රන්ථ','පොතේ']

    language_synonyms = ['භාශාව', 'භාෂාව', 'බස', 'බසින්']

    search_fields= []
    all_search_fields = ['writer_name','writer_name_eng', 'writer_dob', 'writer_birth_place','writer_birth_place_eng', 'education','book_list', 'writtern_language', 'wrote_categories', 'writer_life_story']
    search_query_copy = search_query
    for writer_synonym in writer_synonyms_sin + writer_synonyms_eng:
        if writer_synonym in search_query:
            search_fields.append('writer_name')
            search_fields.append('writer_name_eng')
            search_query = search_query.replace(writer_synonym,'')
    
    for dob_synoymn in dob_synonyms_sin + dob_synonyms_eng:
        if dob_synoymn in search_query:
            search_fields.append('writer_dob')
            search_fields.append('writer_birth_place')
            search_fields.append('writer_birth_place_eng')
            search_query = search_query.replace(dob_synoymn,'')
    
    for education_synonym in education_synonyms:
        if education_synonym in search_query:
            search_fields.append('education')
            search_query = search_query.replace(education_synonym,'')

    for book_synonym in book_synonyms:
        if book_synonym in search_query:
            search_fields.append('book_list')
            search_query = search_query.replace(book_synonym,'')
    
    for language_synonym in language_synonyms:
        if language_synonym in search_query:
            search_fields.append('writtern_language')
            search_query = search_query.replace(language_synonym,'')
    

    if len(search_fields)>0:
        # has synonyms
        search_field_for_query=[]
        print("SELECTED SEARCH FIELDS", search_fields)
        print("SELECTED SEARCH QUERY", search_query)
        for field in all_search_fields:
            if field in search_fields:
                search_field_for_query.append(field+"^5")
            else:
                search_field_for_query.append(field)
        query = queries.multi_match_corss_fields(search_query, search_field_for_query)
    else:
        #no synonyms
        query = queries.multi_match_phrase_prefix(search_query, all_search_fields)
        print("NOT SELECTED FIELDS")

    result = client.search(index=INDEX, body=query)

    return result