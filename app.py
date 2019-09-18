from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    #display random gifs on page before search
    #r = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" % (params['key'], params['limit']))

    # TODO: Extract the query term from url using request.args.get()
    query = request.args.get('name')
    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {
      'q': query,
      'key': "5CFEKEV8TNLP",
      'limit': 10
    }
    # TODO: Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    try:
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params['q'], params['key'], params['limit']))

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    # result_url = list()
    # result_id = list()
    # result_itemurl = list()
    # result_dict = dict()
        result_list = list()
        are_results = False

        result_json = json.loads(r.content)
        are_results = True
        for i in range(params['limit']):
            # result_dict[i]['id'] = result_id[i]
            # result_dict[i]['itemurl'] = result_itemurl[i]
            # result_dict[i]['url'] = result_url[i]
            result_list.append({"url": result_json['results'][i]['id'], "id": result_json['results'][i]['id'], "itemurl":result_json['results'][i]['itemurl']})
            # result_url.append(result_json['results'][i]['media'][0]['mediumgif']['url'])
            # result_id.append(result_json['results'][i]['id'])
            # result_itemurl.append(result_json['results'][i]['itemurl'])
        return render_template("index.html", result_list=result_list, are_results=are_results)
    except:
        return render_template("index.html")
    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

@app.route('/trending')
def trending():

    params = {
      'key': "5CFEKEV8TNLP",
      'limit': 10
    }
    # TODO: Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    try:
        r = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" % (params['key'], params['limit']))

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    # result_url = list()
    # result_id = list()
    # result_itemurl = list()
    # result_dict = dict()
        result_list = list()
        are_results = False

        result_json = json.loads(r.content)
        are_results = True
        for i in range(params['limit']):
            # result_dict[i]['id'] = result_id[i]
            # result_dict[i]['itemurl'] = result_itemurl[i]
            # result_dict[i]['url'] = result_url[i]
            result_list.append({"url": result_json['results'][i]['id'], "id": result_json['results'][i]['id'], "itemurl":result_json['results'][i]['itemurl']})
            # result_url.append(result_json['results'][i]['media'][0]['mediumgif']['url'])
            # result_id.append(result_json['results'][i]['id'])
            # result_itemurl.append(result_json['results'][i]['itemurl'])
        return render_template("trending.html", result_list=result_list)
    except:
        return render_template("index.html")

@app.route('/trending')
def trending():

    params = {
      'key': "5CFEKEV8TNLP",
      'limit': 10
    }
    # TODO: Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    try:
        r = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" % (params['key'], params['limit']))

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object
    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
    # result_url = list()
    # result_id = list()
    # result_itemurl = list()
    # result_dict = dict()
        result_list = list()
        are_results = False

        result_json = json.loads(r.content)
        are_results = True
        for i in range(params['limit']):
            # result_dict[i]['id'] = result_id[i]
            # result_dict[i]['itemurl'] = result_itemurl[i]
            # result_dict[i]['url'] = result_url[i]
            result_list.append({"url": result_json['results'][i]['id'], "id": result_json['results'][i]['id'], "itemurl":result_json['results'][i]['itemurl']})
            # result_url.append(result_json['results'][i]['media'][0]['mediumgif']['url'])
            # result_id.append(result_json['results'][i]['id'])
            # result_itemurl.append(result_json['results'][i]['itemurl'])
        return render_template("trending.html", result_list=result_list)
    except:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
