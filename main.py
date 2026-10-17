#IDOR lab
#IDOR is a security vulnerability where an application exposes internal object references, allowing attackers to access or manipulate resources without proper authorization
#instagram: https://www.instagram.com/cyber_6869/
#GitHub: https://github.com/cyber6869

from flask import Flask,render_template,request,jsonify,session
import json,secrets,webbrowser

#users data information 
with open('data.json','r',encoding='utf-8') as j:
    users=json.load(j)


app=Flask(__name__)
app.secret_key=secrets.token_hex(100)

@app.route('/')
def Login():
    return render_template('login.html')

@app.route('/profile/<int:user_id>')
def Profile(user_id):
   if session.get("username"): 
        for i in range(1,len(users)+1):
            if user_id == users[f"user{i}"]["id"] :
                return jsonify(users[f"user{i}"]),200
                           
        return jsonify({"message":"not found"}),404 
   else:
       return """  <script>window.location.href="/";</script> """,302            

#login verification    
@app.route('/verification',methods=['GET','POST'])
def verification():
    try:
       username=request.form['username']
       password=request.form['password']
       
       for i in range(1,len(users)+1):
           user=users[f"user{i}"]
           if username==user["username"] and password== user["password"]:
               session["username"]=user["username"]
               return f""" <script>window.location.href="/profile/{user["id"]}";</script> """,308
       return jsonify({"message":"username or password incorrect!"}) ,404

    except:
      
          return jsonify({"message":"error"}) ,404

#page error         
@app.errorhandler(404)
def page_not_found(error):
    return """ <h1>404 Page Not Found</h1> """
                           


if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5778") #for open the browser
    app.run(host="127.0.0.1",port=5778)
   
    
