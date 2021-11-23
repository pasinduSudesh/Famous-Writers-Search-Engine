import json


#cross_filds
def multi_match_corss_fields(query, fields=['writer_name']):
	print ("=== QUERY FIELDS ===")
	print (fields)
	es_query = {
		"size": 104,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "cross_fields"
			}
		},
		"aggs":{
			"Name Filter": {
				"terms": {
					"field": "writer_name.keyword",
					"size": 10
				}
			}
		}
	}

	es_query = json.dumps(es_query)
	return es_query

#phrase prefix
def multi_match_phrase_prefix(query, fields=['writer_name']):
	print ("=== QUERY FIELDS ===")
	print (fields)
	es_query = {
		"size": 104,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": 'or',
				"type": "phrase_prefix"
			}
		},
		"aggs":{
			"Name Filter": {
				"terms": {
					"field": "writer_name.keyword",
					"size": 10
				}
			}
		}
	}

	es_query = json.dumps(es_query)
	return es_query

