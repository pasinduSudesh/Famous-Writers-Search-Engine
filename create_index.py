from elasticsearch import Elasticsearch, helpers
from elasticsearch_dsl import Index
import codecs
import json,re,os

client = Elasticsearch(HOST="http://localhost",PORT=9200)
INDEX = 'famous-writers'


def create_index():
    settings = {
        "settings": {
            "index":{
                "number_of_shards": "1",
                "number_of_replicas": "1"
            },
            "analysis" :{
                "analyzer":{
                    "sinhala-analyzer":{
                        "type": "custom",
                        "tokenizer": "icu_tokenizer",
                        "filter":["edge_ngram_custom_filter"]
                    }
                },
                "filter" : {
                    "edge_ngram_custom_filter":{
                        "type": "edge_ngram",
                        "min_gram" : 2,
                        "max_gram" : 50,
                        "side" : "front"
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                    "writer_name": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "writer_name_eng": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "writer_dob": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "writer_birth_place": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "writer_birth_place_eng": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "education": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "book_list": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "writtern_language": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                        "analyzer" : "sinhala-analyzer",
                        "search_analyzer": "standard"
                    },
                    "wrote_categories": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    },
                    "writer_life_story": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        },
                    }
            }
        }
    }

    result = client.indices.create(index=INDEX , body=settings)
    print (result)


def get_book_writers():
    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
    book_writers = json.load(codecs.open(CURRENT_FOLDER+'/data/book_writers.json','r', 'utf-8-sig'))
    return book_writers["writers"]


# Generate data from the json file
def generate_data(writers_list):
    for writer in writers_list:

        writer_name = writer["writer_name"]
        writer_name_eng = writer["writer_name_eng"]
        writer_dob = writer["writer_dob"]
        writer_birth_place = writer["writer_birth_place"]
        writer_birth_place_eng = writer["writer_birth_place_eng"]

        education = writer["education"]
        book_list = writer["book_list"]
        writtern_language = writer["writtern_language"]
        wrote_categories = writer["wrote_categories"]

        writer_life_story = writer["writer_life_story"] 

        

        yield {
            "_index": INDEX,
            "_source": {
                "writer_name": writer_name,
                "writer_name_eng": writer_name_eng,
                "writer_dob": writer_dob,
                "writer_birth_place": writer_birth_place,
                "writer_birth_place_eng": writer_birth_place_eng,
                "education": education,
                "book_list": book_list,
                "writtern_language": writtern_language,
                "wrote_categories": wrote_categories,
                "writer_life_story": writer_life_story
            },
        }


create_index()
book_writers = get_book_writers()
helpers.bulk(client,generate_data(book_writers))