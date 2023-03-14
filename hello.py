from flask import Flask
from flask import make_response
import package
app = Flask(__name__)

@app.route('/api/v.1/ping', methods=['GET'])
def index():
    res = make_response("pong!")
    return res

if __name__ == '__main__':
    app.run(debug=True)

print(package.NAME)