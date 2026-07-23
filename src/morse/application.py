from flask import Flask, render_template, url_for

app = Flask(__name__)
print(app.name)
@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)