from flask import Flask , render_template , redirect, url_for,request,jsonify
from flask_sitemap import Sitemap
app = Flask(__name__)
ext=Sitemap(app=app)
@app.route('/')
def Home():
    return render_template('index.html')
@ext.register_generator
def Home():
    # Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
    yield 'Home', {}

@app.route('/submit',methods = ['POST']) 
def submit():
    try:
        if request.method == 'POST':
            code = request.form['code']
            name=code.upper()
            name=" ".join(name.split())

            data={'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '-':'-....-', '(':'-.--.', ')':'-.--.-'," ":"/" ,'0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',',':'_ _ . . _ _',"'":". _ _ _ _ .","(":"_ . _ _ .",")":"_ . _ _ . _","=":"_ . . . _","+":". _ . _ .","*":"_ . . _","@":". _ _ . _ ."}
            str=""
            for i in name:
                if i=="\n" or i=='\r':
                    str+=""
                else:
                    str+=data[i]+' '
            
            return jsonify(value=str)
    except:
        
        return jsonify(value=f"plz Enter valid characters (abc or ABC or 0-9) the symbol cannot be translated.")
        

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/PrivacyPolicy")
def PrivacyPolicy():
    return render_template("PrivacyPolicy.html")

    
if __name__=="__main__":
    app.run(debug=True)