
from flask import Flask , render_template, request
import urllib.request
import simplejson
import requests
app = Flask(__name__)

# @app.route('/')
# def index():
#    return render_template('hello.html')
data_list = []
index =[]
main_item = []
@app.route('/')
def getdata_list():
    connection = urllib.request.urlopen('http://localhost:8983/solr/music/select?indent=on&q=*:*&rows=200&wt=json')
    response = simplejson.load(connection)

    print (response['response']['numFound'], "documents found.")
    global data_list
    global index
    i = 0
    k =0
    data_list2 =[]
    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('hello.html',result = data_list2, index = index)
@app.route('/all', methods=['POST'])
def getalldata_list():
    connection = urllib.request.urlopen('http://localhost:8983/solr/music/select?indent=on&q=*:*&rows=200&wt=json')

    response = simplejson.load(connection)

    print (response['response']['numFound'], "documents found.")
    global data_list
    global index
    data_list = []
    index =[]
    i = 0
    k =0
    data_list2 =[]
    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0

    return render_template('search.html',result = data_list2, index = index)

@app.route('/search', methods=['POST'])
def search():
    search = request.form['searchs']
    search_list = search.split()
    # re.sub(' +',' ','The     quick brown    fox')
    # print('search text length is :'+' ' == search_list[0], len(search_list))

    query = '('
    m =0
    for i in search_list:
        ii = i.capitalize()
        if m == 0:
            m = 1
            query += '*'+i+'* '
            query += 'OR *'+ii+'* '
        else:
            query += 'OR *'+i+'* OR'
            query += ' *'+ii+'* '
    query += ')'
    # querys = 'http://localhost:8983/solr/music/select?indent=on&q=title:'+query+'album:'+query+'artist:'+query+'genres:'+query+'&rows=200&wt=json'
    querys = 'http://localhost:8983/solr/music/select?q=*:*&fq=title:'+query+'album:'+query+'artist:'+query+'genres:'+query+'&rows=200&wt=json'
    print(querys)
# Request data_list from link as 'str'
    response = requests.get(querys).json()

    print(response['response']['numFound'])
    global data_list
    global index
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]
    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('search.html',result = data_list2, index = index)

@app.route('/searchMoreLikeThis', methods=['POST'])
def searchMoreLikeThis():
    search = request.form['searchsMoreLikeThis']
    search_list = search.split()
    query = '('
    m =0
    for i in search_list:
        ii = i.capitalize()
        if m == 0:
            m = 1
            query += '*'+i+'* '
            query += 'OR *'+ii+'* '
        else:
            query += 'OR *'+i+'* OR'
            query += ' *'+ii+'* '
    query += ')'
    querys = 'http://localhost:8983/solr/music/select?q=*:*&fq=title:'+query+'album:'+query+'artist:'+query+'genres:'+query+'&rows=200&wt=json'

    print(querys)
# Request data_list from link as 'str'
    response = requests.get(querys).json()

    print(response['response']['numFound'])
    global data_list
    global index
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]
    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('songTemplate.html',result = data_list2, index = index, mainSong=main_item)

@app.route('/call_to_related_song', methods=['POST'])
def call_to_related_song():
    search = request.form['searchs']
    search_list = search.split()
    query = '('
    m =0
    for i in search_list:
        ii = i.capitalize()
        if m == 0:
            m = 1
            query += '*'+i+'* '
            query += 'OR *'+ii+'* '
        else:
            query += 'OR *'+i+'* OR'
            query += ' *'+ii+'* '
    query += ')'
    querys = 'http://localhost:8983/solr/music/select?q=*:*&fq=title:'+query+'&rows=200&wt=json'
    # querys = 'http://localhost:8983/solr/music/select?indent=on&q=title:'+query+'&rows=200&wt=json'

# Request data_list from link as 'str'
    response = requests.get(querys).json()

    print(response['response']['numFound'])
    global data_list
    global index
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]
    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('search.html',result = data_list2, index = index)

@app.route('/call_to_related_artists', methods=['POST'])
def call_to_related_artists():
    search = request.form['searchs']
    search_list = search.split()
    query = '('
    m =0
    for i in search_list:
        ii = i.capitalize()
        if m == 0:
            m = 1
            query += '*'+i+'* '
            query += 'OR *'+ii+'* '
        else:
            query += 'OR *'+i+'* OR'
            query += ' *'+ii+'* '
    query += ')'
    querys = 'http://localhost:8983/solr/music/select?q=*:*&fq=artist:'+query+'&rows=200&wt=json'
    # querys = 'http://localhost:8983/solr/music/select?indent=on&q=artist:'+query+'&rows=200&wt=json'

    print(querys)
# Request data_list from link as 'str'
    response = requests.get(querys).json()

    print(response['response']['numFound'])
    global data_list
    global index
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]
    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('search.html',result = data_list2, index = index)

@app.route('/call_to_related_album', methods=['POST'])
def call_to_related_album():
    search = request.form['searchs']
    search_list = search.split()
    query = '('
    m =0
    for i in search_list:
        ii = i.capitalize()
        if m == 0:
            m = 1
            query += '*'+i+'* '
            query += 'OR *'+ii+'* '
        else:
            query += 'OR *'+i+'* OR'
            query += ' *'+ii+'* '
    query += ')'
    querys = 'http://localhost:8983/solr/music/select?q=*:*&fq=album:'+query+'&rows=200&wt=json'
    # querys = 'http://localhost:8983/solr/music/select?indent=on&q=album:'+query+'&rows=200&wt=json'

    print(querys)
# Request data_list from link as 'str'
    response = requests.get(querys).json()

    print(response['response']['numFound'])
    global data_list
    global index
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]
    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('search.html',result = data_list2, index = index)

@app.route('/call_to_related_mood', methods=['POST'])
def call_to_related_mood():
    search = request.form['searchs']
    search_list = search.split()
    query = '('
    m =0
    for i in search_list:
        ii = i.capitalize()
        if m == 0:
            m = 1
            query += '*'+i+'* '
            query += 'OR *'+ii+'* '
        else:
            query += 'OR *'+i+'* OR'
            query += ' *'+ii+'* '
    query += ')'
    querys = 'http://localhost:8983/solr/music/select?q=*:*&fq=genres:'+query+'&rows=200&wt=json'
    # querys = 'http://localhost:8983/solr/music/select?indent=on&q=genres:'+query+'&rows=200&wt=json'

    print(querys)
# Request data_list from link as 'str'
    response = requests.get(querys).json()

    print(response['response']['numFound'])
    global data_list
    global index
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]
    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('search.html',result = data_list2, index = index)

@app.route('/nextPage', methods=['POST'])
def nextPage():
    data_list2 = []
    print(index)
    id = int(request.form['id'])
    for i in range(id*12,id*12+12):
        if (i) < len(data_list):
            data_list2.append(data_list[i])
    return render_template('search.html',result = data_list2, index=index)

@app.route('/nextPageMoreLikeThis', methods=['POST'])
def nextPageMoreLikeThis():
    data_list2 = []
    global main_item
    global data_list
    global index
    id = int(request.form['id'])
    for i in range(id*12,id*12+12):
        if (i) < len(data_list):
            data_list2.append(data_list[i])
    return render_template('songTemplate.html',result = data_list2, index = index, mainSong=main_item)

@app.route('/moreLikeThat', methods=['POST'])
def moreLikeThat():
    id = request.form['id']

    querys = 'http://localhost:8983/solr/music/mlt?q=id:'+id+'&mlt.fl=title,artist,album,genres&mlt.mindf=1&mlt.mintf=1&rows=200&wt=json'

# Request data_list from link as 'str'
    response = requests.get(querys).json()

    print(response['response']['numFound'])
    global data_list
    global index
    global main_item
    # response['match']
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]
    main_item = []
    main_item.append(response['match']['docs'][0])
    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('songTemplate.html',result = data_list2, index = index, mainSong=main_item)

@app.route('/allButtonMoreLikeThat', methods=['POST'])
def allButtonMoreLikeThat():
    global main_item
    id = main_item[0]['id']

    querys = 'http://localhost:8983/solr/music/mlt?q=id:'+id+'&mlt.fl=title,artist,album,genres&mlt.mindf=1&mlt.mintf=1&rows=200&wt=json'

# Request data_list from link as 'str'
    response = requests.get(querys).json()

    print(response['response']['numFound'])
    global data_list
    global index

    # response['match']
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]

    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('songTemplate.html',result = data_list2, index = index, mainSong=main_item)

@app.route('/artistButtonMoreLikeThat', methods=['POST'])
def artistButtonMoreLikeThat():
    global main_item
    id = main_item[0]['id']

    querys = 'http://localhost:8983/solr/music/mlt?q=id:'+id+'&mlt.fl=artist&mlt.mindf=1&mlt.mintf=1&rows=200&wt=json'

# Request data_list from link as 'str'
    response = requests.get(querys).json()

    print(response['response']['numFound'])
    global data_list
    global index

    # response['match']
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]

    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('songTemplate.html',result = data_list2, index = index, mainSong=main_item)

@app.route('/albumButtonMoreLikeThat', methods=['POST'])
def albumButtonMoreLikeThat():
    global main_item
    id = main_item[0]['id']

    querys = 'http://localhost:8983/solr/music/mlt?q=id:'+id+'&mlt.fl=album&mlt.mindf=1&mlt.mintf=1&rows=200&wt=json'

# Request data_list from link as 'str'
    response = requests.get(querys).json()
    print(response['response']['numFound'])
    global data_list
    global index

    # response['match']
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]

    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('songTemplate.html',result = data_list2, index = index, mainSong=main_item)

@app.route('/moodButtonMoreLikeThat', methods=['POST'])
def moodButtonMoreLikeThat():
    global main_item
    id = main_item[0]['id']

    querys = 'http://localhost:8983/solr/music/mlt?q=id:'+id+'&mlt.fl=genres&mlt.mindf=1&mlt.mintf=1&rows=200&wt=json'

# Request data_list from link as 'str'
    response = requests.get(querys).json()

    print(response['response']['numFound'])
    global data_list
    global index

    # response['match']
    data_list =[]
    index =[]
    i = 0
    k =0
    data_list2 =[]

    # Print the name of each document.
    for document in response['response']['docs']:
      data_list.append(document)
      if i < 12:
        data_list2.append(document)
      if i%12 == 0:
          index.append(k)
          k = k+1
      i=i+1
    i = 0
    return render_template('songTemplate.html',result = data_list2, index = index, mainSong=main_item)
if __name__ == '__main__':
   app.run(debug = True)
