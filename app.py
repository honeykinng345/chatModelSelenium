from flask import Flask, request, jsonify

import logging
from preplexity_handler.perplexity_web_scrapper import PerplexityHandler
from utils.user_handler import UserHandler

driver = None
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@app.route('/')
def home():
    return "Welcome to the Teacher Assistant Api"


@app.route('/chatrequest', methods=['POST'])
def amazon_webpage():
    global driver
    data = request.json
    query = data.get('query')
    appId = data.get('appId')

    if not query:
        return jsonify({"error": "Please provide a query parameter"}), 400
    try:
        userObject = UserHandler.checkUserAlreadyExistOrNot(appId)
        perplexityHandler = PerplexityHandler.scrape_amazon_webpage(query, userObject)
        return perplexityHandler
        # Initialize the driver once and reuse it
        # if driver is None:
        #     UserHandler.checkUserAlreadyExistOrNot(appId)
        #
        # result = scrape_amazon_webpage(driver, query)
        # return jsonify({"response": result,message}), 200

    except Exception as e:
        return jsonify({"error": "Error "+str(e.args[0][0].response[0])}), 400


@app.route('/chatrequest', methods=['POST'])
def amazon_webpage():
    global driver
    data = request.json
    query = data.get('query')
    appId = data.get('appId')

    if not query:
        return jsonify({"error": "Please provide a query parameter"}), 400
    try:
        userObject = UserHandler.checkUserAlreadyExistOrNot(appId)
        perplexityHandler = PerplexityHandler.scrape_amazon_webpage(query, userObject)
        return perplexityHandler
        # Initialize the driver once and reuse it
        # if driver is None:
        #     UserHandler.checkUserAlreadyExistOrNot(appId)
        #
        # result = scrape_amazon_webpage(driver, query)
        # return jsonify({"response": result,message}), 200

    except Exception as e:
        return jsonify({"error": "Error "+str(e.args[0][0].response[0])}), 400


if __name__ == '__main__':
    app.run(debug=True)
