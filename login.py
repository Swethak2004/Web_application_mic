from flask import Flask,request,render_template,redirect,url_for
# from flaskext.mysql import MySQL
from flask_mysqldb import MySQL




app=Flask(__name__)
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Srmbca2021'
app.config['MYSQL_DB']='besant'
app.config['MYSQL_HOST']='localhost'
mysql=MySQL(app)
# mysql.init_app(app)


#home page
@app.route('/')
def home():
    return render_template("home.html")


#register page
@app.route("/register",methods=["GET","POST"])
def register():
    msg = ''
    if request.method=="POST":
       Name=request.form.get("name")
       Gender=request.form.get("gender") 
       Phone_number=request.form.get("phone_number")
       Password=request.form.get("password")
       Email=request.form.get("email")

       cursor=mysql.connection.cursor()
       
       cursor.execute(f"INSERT INTO user VALUES ('{Name}','{Gender}','{Phone_number}','{Password}','{Email}');")
       
       mysql.connection.commit()
       msg = 'You have successfully registered !'
       return render_template("home.html")



    return render_template("register.html",msg = msg)

#login page
@app.route('/login',methods=['POST','GET'])
def authentication():
    if request.method=="POST":
        UserName=request.form.get('username')
        Password=request.form.get('password')
        
        print(UserName)
        print(Password)

        cursor=mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM user WHERE Name= '{UserName}' and Password= '{Password}'")

        data=cursor.fetchone()
        
        if data == None:
            return f"{data} no"
        else:
            return f"{data} yes"
    return render_template('loginpage.html')    

if __name__ == "__main__":
    app.run(debug=True)
