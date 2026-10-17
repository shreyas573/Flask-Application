from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)
def create_table():
    conn=sqlite3.connect("user.db")
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS 
    user(id integer primary key,name varchar(20))""")
    conn.commit()
    conn.close()
    

@app.route("/",methods=["GET","POST"])
def home():
    message="" 
    if request.method=="POST":
        name=request.form.get("name")
        if not name:
            message="please enter a name"
        else:
            conn=sqlite3.connect("user.db")
            cursor=conn.cursor()
            cursor.execute("INSERT INTO user(name) VALUES(?)", (name,))
            conn.commit()
            conn.close()
            message="name saved succesfully"


    return render_template("index.html", message=message)

if __name__=="__main__":
    app.run(debug=True)