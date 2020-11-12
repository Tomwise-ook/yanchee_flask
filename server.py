from flask import Flask, request, render_template
import json
import requests

app = Flask(__name__)

@app.route('/firstrequest', methods=['GET'])
def firstrequest():
    return('Thomas posted ...')

@app.route('/', methods=['GET'])
def rootRequest():
    return(render_template('index.html'))



@app.route('/form-example', methods=['GET', 'POST']) #allow both GEt and POST requests
def form_example():
    if request.method == 'POST':  #this block is only entered when form is submitted
        language = request.form.get('language')
        framework = request.form['framework']

        return '''  <h1> the language value is : {}</h>
                    <h1> the framework value is : {}</h>'''.format(language,framework)

    return    """<form method="POST">
                     Language: <input type="text" name="language"><br><br>
                    Framework: <input type="text" name="framework"><br><br>
                    <input type="submit" value="Submit"><br>
                    </form>"""


"""
@app.route('/form-example', methods=['GET', 'POST']) #allow both GEt and POST requests
def form_example():
    (render_template('login_page.html'))  """



if __name__ == '__main__':
    app.run(debug=True)
