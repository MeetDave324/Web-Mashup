from flask import Flask
app = Flask(__name__)
import wikipedia
from flask import jsonify
from flask import request
@app.route('/wiki/',methods=['GET'])
def wiki():
    inputdata=request.args.get('word')
    print(inputdata)
    wikiresult=wikipedia.search(inputdata, results=1)
    print(wikiresult)
    summary=wikipedia.summary(str(wikiresult))
    print(summary)
    return jsonify({'word':inputdata,
                    'summary':summary})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)