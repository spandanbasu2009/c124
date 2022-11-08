from flask import Flask,jsonify,request
app = Flask(__name__)
tasks = [
    {
        "ID":1,
        "Title":"Buy Groceries",
        "Description":"Milk,Cheese,Fruits",
        "Done":False
    },
    {
        "ID":2,
        "Title":"Learn Python",
        "Description":"Need to find good tutorial",
        "Done":False
    }
]


@app.route('/post-data',methods = ["POST"])
def post_task():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the data"
        })
    task = {
        "ID":tasks[-1]["ID"]+1,
        "Title":request.json["Title"],
        "Description":request.json.get("Description",""),
        "Done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })

@app.route('/get-data')
def get_task():
    return jsonify({
        "data":tasks
    })

if (__name__ == "__main__"):
    app.run(debug = True)