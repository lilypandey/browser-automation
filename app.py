from flask import Flask, request, jsonify
from browser_controller import open_browser, close_browser, clear_browser_data

app = Flask(__name__)

@app.route('/open')
def open_url():
    app_name = request.args.get('app')
    url = request.args.get('url')
    if not app_name or not url:
        return jsonify({"error": "Missing 'app' or 'url' parameter"}), 400
    result = open_browser(app_name.lower(), url)
    return jsonify({"result": result})

@app.route('/close')
def close():
    app_name = request.args.get('app')
    if not app_name:
        return jsonify({"error": "Missing 'app' parameter"}), 400
    result = close_browser(app_name.lower())
    return jsonify({"result": result})

@app.route('/clear')
def clear():
    app_name = request.args.get('app')
    if not app_name:
        return jsonify({"error": "Missing 'app' parameter"}), 400
    result = clear_browser_data(app_name.lower())
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
