from flask import Flask , render_template , redirect, url_for,request
app = Flask(__name__)
# app.debug=True
@app.route('/',methods = ['POST', 'GET']) 
def Home():
    try:
        if request.method == 'POST':
            code = request.form['code']
            print(code)
        #   return output(Code)
        else:
            code = request.args.get('code')
        #   return output(Code)
        if code==None:
            return render_template("index.html",str="",code="")
        else:
            name=code.upper()
            name=" ".join(name.split())

            data={'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '-':'-....-', '(':'-.--.', ')':'-.--.-'," ":"/" ,'0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',',':'_ _ . . _ _',"'":". _ _ _ _ .","(":"_ . _ _ .",")":"_ . _ _ . _","=":"_ . . . _","+":". _ . _ .","*":"_ . . _","@":". _ _ . _ ."}
            str=""
            for i in name:
                if i=="\n" or i=='\r':
                    str+=""
                else:
                    str+=data[i]+' '
            str=str.replace("//","/")  
            str=str.replace("/ /","/")
            
            return render_template("index.html",str=str,code=code)
    except:
        return render_template("index.html",str="plz Enter valid characters (abc or ABC) no Numerical value plz",code=code)

@app.route("/about")
def about():
    dict={"math":40,"Physics":56,"Chemistry":69,"English":58,"Computer Science":89}
    return render_template("about.html",values=dict)
@app.route("/PrivacyPolicy")
def PrivacyPolicy():
    return render_template("PrivacyPolicy.html")

    
if __name__=="__main__":
    app.run()