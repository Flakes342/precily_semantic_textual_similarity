from flask import Flask, render_template, request
from MachineLearningCode import MachineLearningCode

# apps initializations
app = Flask(__name__)
print("Flask app initialized")
MLC = MachineLearningCode()


# routes definitions

@app.route('/')
@app.route('/home')
def hello_world():
    print("Hello World!")
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predictandoutput():
    text1 = request.form["text1"]
    text2 = request.form["text2"]
    
    Result = MLC.predict(text1,text2)
    return render_template("result.html", similarity_score=Result)


# app run
if __name__ == '__main__':
    app.run(debug=True, port=5001)
