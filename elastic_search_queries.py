from elasticsearch import Elasticsearch 


es=Elasticsearch([{'host':'localhost','port':9200}])

q4 = {'query':{'match':{'first_name':'abhay'}}}

q5 = {'query':{'bool':{'must':[{'match':{'first_name':'abhay'}}]}}}

q6 = {
        'query':{
            'bool':{
                'must':{
                    'match':{
                        'first_name':'abhay'
                    }
                },
                "filter":{
                    "range":{
                        "age":{
                            "gt":25
                        }
                    }
                }
            }
        }
    }

q7 = {
        'query':{
            'match':{
                "about":"play cricket"
            }
        }
    }

q8 = {
        'query':{
            'match_phrase':{
                "about":"play cricket"
            }
        }
    }
q9 = {
    "aggs": {
        "all_interests": {
        "terms": { "field": "interests.keyword" }
        }
    }
}

q10 = {
   "query":{
      "multi_match" : {
         "query": "paprola",
         "fields": [ "city", "state" ]
      }
   }
}
q11 = {"query":{
      "query_string":{
         "query":"play"
      }
   }
}

q12 = {
   "query":{
      "term":{"zip":"176115"}
   			}
	}


def search_queries(query_dic,index):
	output = es.search(index=index,body=query_dic)
	for hit in output['hits']['hits']:
		result = hit['_source']
	print('result =  ',result)
	print('******************************************')




output1=es.get(index='company',id=3)
print('dic of employee with id 3',output1)
print('source_dict/actaul_doc',output1['_source'])
# outut2=es.delete(index='company',id=2)
print('******************************************')
output4= es.search(index='company',body=q4)
print('doc with first name matching:  ',output4['hits']['hits'])
print('******************************************')
output5= es.search(index='company',body=(q5))
print("boll_search:   ",output5['hits']['hits'])
print('******************************************')
output6 = es.search(index='company',body=(q6))
print("search with filter:   ",output6['hits']['hits'])
print('******************************************')
output7= es.search(index='company',body=(q7))
print("full text search: ")
for hit in output7['hits']['hits']:
    print(hit['_source']['about']) 
    print(hit['_score'])
    print('**********************')






search_queries(q8,'company')
search_queries(q9,'company')
search_queries(q10,'company')
search_queries(q11,'company')
search_queries(q12,'company')

