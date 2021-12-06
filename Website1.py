from flask import Flask
from flask.globals import request

app = Flask(__name__)

def validation(name, password):
   pass

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
        <html>
        <body>

        <h2>Welcome to the page</h2>

        <a href="/login" >Click here </a>

        </body>
        </html>
    """

@app.route('/validate', methods=['GET', 'POST'])
def validate():
    if request.method == 'POST':
        first_name = request.form['fname']
        return f"Hello {first_name}"
    elif request.method == 'GET':
        pass
    
    return "Otherwise"


@app.route('/login')
def login():
    return """
        <!DOCTYPE html>
        <html>
        <body>

        <h2>HTML Forms</h2>

        <form method="post" action="/validate">
        <label for="fname">First name:</label><br>
        <input type="text" id="fname" name="fname" value="John"><br>
        <label for="lname">Last name:</label><br>
        <input type="text" id="lname" name="lname" value="Doe"><br><br>
        <input type="submit" value="Submit">
        </form> 

        <p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>

        </body>
        </html>
    """


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)