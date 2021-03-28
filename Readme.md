# Morse Code Generator
This is a Translation tool which tanslate normal text to morse code
## Try it on Heroku : 
https://morse-code-translater.herokuapp.com/

# Features:
1. Use Flask
2. Show the result without reloading page
3. use javascript for that
4. use Bootstrap for html form 
5. Deployed on Heroku Try it on Heroku https://morse-code-translater.herokuapp.com/

# Requirement:
1. click==7.1.2
2. Flask==1.1.2
3. gunicorn==20.0.4
4. itsdangerous==1.1.0
5. Jinja2==2.11.3
6. MarkupSafe==1.1.1
7. Werkzeug==1.0.1

# File & Folder
1. Static
    This folder contain stylesheet , images & javascript. 
2. templates
    This folder contain html template for the site . 
3. app.py
    This is the main app file 
4. Procfile
    This file is used to tell the Heroku that this  is a webapp for deploying purpose not needed on local server
5. Readme.md
    Discription and usage wirtten in this file
6. Requirements.txt
    This file contain the required module name which are nedded ot use this webapp.

# Usage
1. clone or download the app clone using git
    git clone https://github.com/Nktech-Official/MorseCodeTranlator.git

2. Install the requirement files 
    pip install -r requirements.txt

3. Now launch the app.py
    python app.py

4. After launching the application you will get following ouptut
    * Serving Flask app "app" (lazy loading)
    * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
    * Debug mode: on
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 125-144-452
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    127.0.0.1 - - [28/Mar/2021 15:55:29] "GET / HTTP/1.1" 200 -

5. open WebBrowser and type in addressbar link given in second last line of output 
     http://127.0.0.1:5000/

6. To quit or exit the app in the command line Press CTRL+C.



