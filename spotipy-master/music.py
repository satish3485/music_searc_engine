# import urllib.request
# import simplejson
#
# connection = urllib.request.urlopen('http://localhost:8983/solr/music/select?indent=on&q=popularity_i:74&rows=100&wt=json')
#
# response = simplejson.load(connection)
#
# print (response['response']['numFound'], "documents found.")
#
# # Print the name of each document.
#
# for document in response['response']['docs']:
#   print ("  Name =", document['title_ss'])
