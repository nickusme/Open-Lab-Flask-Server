from flask import Flask, render_template, request, jsonify, abort

app = Flask(__name__)

# Define a route that will serve your website
@app.route('/')
def serve_website():
    print("Request received")
    return render_template("index.html", flask_token="Hello   world")

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from the server!'}
    return jsonify(data)


# Implement IP-based access control
# @app.before_request
# def restrict_access():
#     allowed_ip = '192.168.1.100'  # Replace with the specific IP address you want to allow
#     client_ip = request.remote_addr
#     if client_ip != allowed_ip:
#         abort(403)  # Forbidden

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)