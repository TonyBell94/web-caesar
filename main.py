from flask import Flask, request
from helpers import rotate_character
all_sym = {'alphabet' : "abcdefghijklmnopqrstuvwxyz" , 'ALPHABET' : "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 'sym' : "'!@#$%^&*()_+=-?/.,><:; ", 'num' : '1234567890'}  


app = Flask(__name__)
app.config["DEBUG"] = True

display = """
        <!DOCTYPE html>

        <html>
            <head>
                <style>
                    form{{
                        background-color: gray;
                        padding: 20px;
                        margin: 0 auto;
                        width: 540;
                        font: 16pk sans-serif;
                        border-radius: 10px;
                    }}
                    textarea{{
                        margin: 10px 0;
                        width: 540px;
                        height: 120px;
                    }}
                </style>
            </head>

            <body>
                <form action="/rota" method="POST">
                    <label>Rotate By:

                        <input type="text" name="rotate" value="0" id="rotater">

                        </input>
                    </label>

                    <br><br>

                    <input id="text" type="text" name="message">
                        {0}
                    </input>

                    <br><br>

                    <input type="submit" value="Submit">

                </form> 

            </body>
        </html>

        """

@app.route("/")
def idk():
    return display

@app.route("/rota", methods=["POST"])

def index():

    rot = int(request.form["rotate"])
    text = str(request.form["message"])

    encryption = ""
    for char in text:    
        encryption += rotate_character(char, rot)
    encryption = display.format(encryption)      
    return encryption

app.run()