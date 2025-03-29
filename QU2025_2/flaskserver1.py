from flask import Flask, request, render_template

app=Flask(__name__)

langchain_html="testing testing 123"

@app.route("/")#Double check

def send_output():
    global langchain_html
    #return "<p>Hello, World!</p>"
    return render_template('career.html', data=langchain_html)

@app.route("/submit_data", methods=["POST"])

def get_data():
    if request.method == 'POST':
        data = request.form['data_input']
        # Process the data (e.g., save to a database, perform calculations)
        return data

app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)