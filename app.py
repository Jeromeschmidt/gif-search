from flask import Flask, render_template, request
import requests
import json
import os

from dotenv import load_dotenv
load_dotenv()

TENOR_API_KEY = os.getenv("TENOR_API_KEY")

app = Flask(__name__)


@app.route('/')
def index():
    """Return homepage."""
    #display random gifs on page before search
    # Extract the query term from url using request.args.get()
    query = request.args.get('name')
    # Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'
    params = {
      'q': query,
      'key': TENOR_API_KEY,
      'limit': 10
    }
    #Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    try:
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (params['q'], params['key'], params['limit']))

    # Use the '.json()' function to get the JSON of the returned response
    # object
    # Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

        result_list = list()
        are_results = False

        result_json = json.loads(r.content)
        are_results = True
        for i in range(params['limit']):

            result_list.append({"url": result_json['results'][i]['url'], "id": result_json['results'][i]['id'], "itemurl":result_json['results'][i]['itemurl']})

        return render_template("index.html", result_list=result_list, are_results=are_results)
    except:
        return render_template("index.html")
    # Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'

@app.route('/trending')
def trending():

    params = {
      'key': TENOR_API_KEY,
      'limit': 10
    }
    # Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    try:
        r = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" % (params['key'], params['limit']))

    # Use the '.json()' function to get the JSON of the returned response
    # object
    # Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
        result_list = list()
        are_results = False

        result_json = json.loads(r.content)
        are_results = True
        for i in range(params['limit']):
            result_list.append({"url": result_json['results'][i]['id'], "id": result_json['results'][i]['id'], "itemurl":result_json['results'][i]['itemurl']})
        return render_template("index.html", result_list=result_list, are_results=are_results)
    except:
        return render_template("index.html")

@app.route('/random')
def random():
    query = request.args.get('name')

    params = {
      'q': query,
      'key': TENOR_API_KEY,
      'limit': 10
    }
    # Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation
    try:
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (params['q'], params['key'], params['limit']))

    # Use the '.json()' function to get the JSON of the returned response
    # object
    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list
        result_list = list()
        are_results = False

        result_json = json.loads(r.content)
        are_results = True
        for i in range(params['limit']):
            result_list.append({"url": result_json['results'][i]['id'], "id": result_json['results'][i]['id'], "itemurl":result_json['results'][i]['itemurl']})
        return render_template("index.html", result_list=result_list, are_results=are_results)
    except:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
