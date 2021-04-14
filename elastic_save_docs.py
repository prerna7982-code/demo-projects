from elasticsearch import Elasticsearch 


es=Elasticsearch([{'host':'localhost','port':9200}], timeout=30)

print(es,"elastic search connected")

# e1={
#     "first_name":"abhay",
#     "last_name":"singh",
#     "age": 27,
#     "about": "Love to play cricket",
#     "interests": ['sports','music'],
# }

# e2={
#     "first_name" :  "Jane",
#     "last_name" :   "Smith",
#     "age" :         32,
#     "about" :       "I like to collect rock albums",
#     "interests":  [ "music" ]
# }
# e3={
#     "first_name" :  "Douglas",
#     "last_name" :   "Fir",
#     "age" :         35,
#     "about":        "I like to build cabinets",
#     "interests":  [ "forestry" ]
# }

# e4={
#     "first_name":"asd",
#     "last_name":"pafdfd",
#     "age": 27,
#     "about": "Love to play football",
#     "interests": ['sports','music'],
# }

e5={
    "first_name":"mohhammad",
    "last_name":"aslam",
    "age": 25,
    "about": "Love to play tennis",
    "interests": ['sports','music','travelling'],
    "city" : "paprola",
	"state" : "HP",
	"zip" : "176115",	
}


# res1 = es.index(index='company',id=1,body=e1)
# res2 = es.index(index='company',id=2,body=e2)
# res3 = es.index(index='company',id=3,body=e3)
# res4 = es.index(index='company',id=4,body=e4)
res5 = es.index(index='company',id=5,body=e5)
print(res5)


# def bulk_index():
#     actions = doc_generator()
#     res = bulk(es, actions, index='company', doc_type='company',
#                expand_action_callback=expand_action,
#                chunk_size=100000, timeout=30)
#     print('res: ', res)