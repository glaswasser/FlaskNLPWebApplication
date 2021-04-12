
from flask import Flask, request, jsonify
import pandas as pd
from bertopic import BERTopic


app = Flask(__name__)

@app.route("/upload", methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #print(request.files['file'])
        #f = request.files['file']
        f = "/Users/alexanderheinz/github/privat/topic modelling/labeled-german-tables/bra_tee_labeled.xlsx"
        comments = pd.read_excel(f)
        ## INSERT TOPIC MODELLING HERE
        comments.loc[comments.text.isnull(), "text"] = " " # replace nan with empty string
        ## RUN BERTOPIC
        docs = comments.text
        topic_model = BERTopic(language = "multilingual", verbose = True, calculate_probabilities = True) # arguments: min_topic_size, nr_topics = "auto", 
        
        topics, probabilities = topic_model.fit_transform(docs)

        graph = topic_model.visualize_topics()

        graphJSON = json.dumps(graph, cls=plotly.utils.PlotlyJSONEncoder)

        for line in iter(proc.stdout.readline,''):
            time.sleep(1)  # Don't need this just shows the text streaming
            yield line.rstrip() + '<br/>\n'
    return render_template('layouts/index.html',
                           ids=ids,
                           graphJSON=graphJSON)
   #     return "test" #topic_model.visualize_topics()
    #return '''
    #<!doctype html>
    #<title>Upload an excel file, text column must be called "text".</title>
    #<h1>Excel file upload</h1>
    #<form action="" method=post enctype=multipart/form-data>
    #<p><input type=file name=file><input type=submit value=Upload>
   # </form>
   # '''
    



@app.route("/export", methods = ['GET'])
def export_records():
    return 


if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)