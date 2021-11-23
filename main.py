from flask import Flask, render_template, request
from search import search
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def search_box():
    if request.method == 'POST':
        search_query = request.form['searchQuery']
        result= search(search_query)
        hits = result['hits']['hits']
        aggs = result['aggregations']
        result_count = len(hits)
        print("**************************************")
        print(hits)
        print("**************************************")
        return render_template('show_result.html', search_query=search_query, hits=hits, aggs=aggs, result_count=result_count)
    if request.method == 'GET':
        return render_template('show_result.html')

if __name__ == "__main__":
    app.run(debug=True)