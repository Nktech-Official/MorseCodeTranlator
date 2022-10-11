from flask import Flask, render_template, redirect, url_for, request, jsonify
from cipher import MorseCodeCipher

app = Flask(__name__)

MorseCode = MorseCodeCipher()


@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:
        if request.method == 'POST':
            code = request.form['code']
            code = code.upper()

            if MorseCode.is_morse_code(code):
                result = MorseCode.decrypt(code)
            else:
                result = MorseCode.encrypt(code)

            return jsonify(value=result)
    except:

        return jsonify(value=f"plz Enter valid characters (abc or ABC or 0-9) the symbol cannot be translated.")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/PrivacyPolicy")
def PrivacyPolicy():
    return render_template("PrivacyPolicy.html")


if __name__ == "__main__":
    app.run(debug=True)
