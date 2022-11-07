from flask import Flask,render_template,request,session
from flask_mysqldb import MySQL
import review
import json 
import os
from flask import jsonify
import algo
app=Flask(__name__)
app.secret_key = "zdcxfxfvxcvcvcv25562521cvbcgb2152521cggcg215252"
mysql=MySQL(app)
APP_ROOT=os.path.dirname(os.path.abspath(__file__))
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']="root"
app.config['MYSQL_DB']="hospital"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_password')
def u_password():
    return render_template('u_password.html')

@app.route('/forgot_password',methods=["POST"])
def forgot_password():
    email=request.form["email"]
    cur=mysql.connection.cursor()
    n=cur.execute("SELECT email FROM register where email='"+email+"'")
    print(n)
    if n==0:
        return "<script>alert(\"Invalid Email\");window.location.href=\"/login\";</script>"
    
    import random
    rand=random.randint(1000,9999)
    
    cur.execute("UPDATE register SET password=%s where email=%s",(str(rand),email))
    mysql.connection.commit()
    import smtplib 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login("kushalkushi1704@gmail.com", "kush@1704") 
    message = "password    "+str(rand) 
    s.sendmail("kushalkushi1704@gmail.com",email, message) 
    s.quit()
    return "<script>alert(\"Password Updated\");window.location.href=\"/login\";</script>"


@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/admin')
def admin():
    return render_template('admin.html')


  






@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/heart')
def heart():
    return render_template("heart.html")
@app.route('/diabetes')
def diabetes():
    return render_template("diabetes.html")
    
@app.route('/breast')
def breast():
    return render_template("breast.html")

@app.route('/user_home')
def user_home():
    session.pop('username', None)
    return render_template("user_login.html")

@app.route('/admin_login', methods=['POST'])
def admin_login():
    uname=request.form["username"]
    password=request.form["pass"]
    if uname=="admin@gmail.com" and password=="1234":
        return render_template("admin.html")
    else:
        return render_template("login.html")

@app.route('/register', methods=["POST","GET"])
def register():
    name=request.form["name"]
    email=request.form["email"]
    password=request.form["password"]
    cpassword=request.form["cpassword"]
    phonenumber=request.form["phonenumber"]
    if password != cpassword:
        return "<script>alert(\"password miss match\");window.location.href=\"/login\";</script>"
    cur=mysql.connection.cursor()
    n=cur.execute("SELECT email FROM register where email='"+email+"'")
    print(n)
    if n==1:
        return "<script>alert(\"already registered\");window.location.href=\"/login\";</script>"
    cur.execute('''
                    insert into register
                    (name,email,password,phonenumber)
                    values(%s,%s,%s,%s)
                    ''',(name,email,password,phonenumber))
    mysql.connection.commit()
    return "<script>alert(\"Register succesfully\");window.location.href=\"/login\";</script>"
         
@app.route('/user_login', methods=["POST"])
def user_login():
    email=request.form["email"]
    password=request.form["password"]
    print(email,password)
    cur=mysql.connection.cursor()
    if email=="admin@gmail.com" and password=="1234":
        return render_template("admin.html")
    n=cur.execute("SELECT * FROM register where email='"+email+"'")
    print(n)
    if n==0:
        return "<script>alert(\"Not Register\");window.location.href=\"/login\";</script>"
    cur.execute("SELECT password FROM register where email='"+email+"'")
    psw=cur.fetchall()
    if password==psw[0][0]:
        return render_template("user_login.html")
    else:
        return "<script>alert(\"Invalid Password\");window.location.href=\"/login\";</script>"
    

@app.route("/heart_pred", methods=["POST","GET"])
def heart_pred():
    age=request.form["age"]
    gender=request.form["gender"]
    cp=request.form["cp"]
    bp=request.form["bp"]
    chol=request.form["chol"]
    fbs=request.form["fbs"]
    electro=request.form["electro"]
    heart_rate=request.form["heart_rate"]
    angina=request.form["angina"]
    Depression=request.form["Depression"]
    slop=request.form["slope"]
    vessels=request.form["vessels"]
    thal=request.form["thal"]
    t_list=[age,gender,cp,bp,chol,fbs,electro,heart_rate,angina,Depression,slop,vessels,thal]
    res=algo.h_pred(t_list)
    session["disease"]="heart"
    if res[0]==0:
        return render_template("no_disease.html",d="HEART")
    return render_template("decision.html", d="Diabetes Prediction")



@app.route('/h_upload')
def h_upload():
    return render_template('h_upload.html')

@app.route('/h_data', methods=["POST"])
def h_data():
    age=request.form["age"]
    gender=request.form["gender"]
    cp=request.form["cp"]
    bp=request.form["bp"]
    chol=request.form["chol"]
    fbs=request.form["fbs"]
    electro=request.form["electro"]
    heart_rate=request.form["heart_rate"]
    angina=request.form["angina"]
    Depression=request.form["Depression"]
    slop=request.form["slope"]
    vessels=request.form["vessels"]
    thal=request.form["thal"]
    Outcome=request.form["Outcome"]
    t_list=[age,gender,cp,bp,chol,fbs,electro,heart_rate,angina,Depression,slop,vessels,thal]
    cur=mysql.connection.cursor()
    cur.execute('''
                    insert into heart
                    (age,gender,cp,bp,chol,fbs,electro,heart_rate,angina,Depression,slop,vessels,thal,Outcome)
                    values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',(age,gender,cp,bp,chol,fbs,electro,heart_rate,angina,Depression,slop,vessels,thal,Outcome))
    mysql.connection.commit()                  
    return "<script>alert(\"Updated successfully\");window.location.href=\"/h_upload\";</script>"  

@app.route("/diabetes_pred", methods=["POST","GET"])
def diabetes_pred():
    age=request.form["age"]
    Glucose=request.form["Glucose"]
    bp=request.form["bp"]
    SkinThickness=request.form["SkinThickness"]
    Insulin=request.form["Insulin"]
    BMI=request.form["BMI"]
    DPF=request.form["DPF"]
    t_list=[age,Glucose,bp,SkinThickness,Insulin,BMI,DPF]
    res=algo.d_pred(t_list)
    session["disease"]="diabetes"  
    if res[0]==0:
        return render_template("no_disease.html",d="diabetes")
    return render_template("decision.html", d="Diabetes Prediction")

@app.route("/cancer_pred", methods=["GET","POST"])
def cancer_pred():
    mr=request.form["mr"]
    mt=request.form["mt"] 
    mp=request.form["mp"]
    ma=request.form["ma"]
    ms=request.form["ms"]
    t_list=[mr,mt,mp,ma,ms]
    res=algo.c_pred(t_list)
    session["disease"]="breast" 
    if res==0:
        return render_template("no_disease.html",d="Breast cancer")
    return render_template("decision.html",d="Breast cancer")

@app.route('/c_upload')
def c_upload():
    return render_template('c_upload.html')

@app.route('/c_data', methods=["POST"])
def c_data():
    mr=request.form["mr"]
    mt=request.form["mt"] 
    mp=request.form["mp"]
    ma=request.form["ma"]
    ms=request.form["ms"]
    Outcome=request.form["Outcome"]
    t_list=[mr,mt,mp,ma,ms]
    res=algo.c_pred(t_list)
    cur=mysql.connection.cursor()
    cur.execute('''
                    insert into cancer
                    (mr,mt,mp,ma,ms,Outcome)
                    values(%s,%s,%s,%s,%s,%s)
                    ''',(mr,mt,mp,ma,ms,Outcome))
    mysql.connection.commit()
    return "<script>alert(\"Updated successfully\");window.location.href=\"/c_upload\";</script>"

@app.route('/d_upload')
def d_upload():
    return render_template('d_upload.html')

@app.route('/d_data', methods=["POST"])
def d_data():
    age=request.form["age"]
    Glucose=request.form["Glucose"]
    bp=request.form["bp"]
    SkinThickness=request.form["SkinThickness"]
    Insulin=request.form["Insulin"]
    BMI=request.form["BMI"]
    DPF=request.form["DPF"]
    Outcome=request.form["Outcome"]
    t_list=[age,Glucose,bp,SkinThickness,Insulin,BMI,DPF]
    cur=mysql.connection.cursor()
    cur.execute('''
                    insert into diabetes
                    (age,Glucose,bp,SkinThickness,Insulin,BMI,DPF,Outcome)
                    values(%s,%s,%s,%s,%s,%s,%s,%s)
                    ''',(age,Glucose,bp,SkinThickness,Insulin,BMI,DPF,Outcome))
    mysql.connection.commit()
    return "<script>alert(\"Updated successfully\");window.location.href=\"/d_upload\";</script>"

@app.route('/r_upload')
def r_upload():
    return render_template('r_upload.html')

@app.route('/r_data', methods=["POST"])
def r_data():
    Outcome=request.form["Outcome"]
    name=request.form["name"]
    hospital=request.form["hospital"]
    d_review=request.form["d_review"]
    h_review=request.form["h_review"]   
    cur=mysql.connection.cursor()
    cur.execute('''
                    insert into review
                    (Outcome,name,hospital,d_review,h_review)
                    values(%s,%s,%s,%s,%s)
                    ''',(Outcome,name,hospital,d_review,h_review))
    mysql.connection.commit()                               
    return "<script>alert(\"Updated successfully\");window.location.href=\"/r_upload\";</script>"  


@app.route('/d_recommendation')
def d_recommendation():
    d=session["disease"]
    print(d)
    s=review.d_senti(d)
    print(s)
    return render_template("doctor_list.html",d_list=s)

@app.route('/recomendation_home')
def recomendation_home():
    d=session["disease"]
    return render_template("decision.html",d=d)


@app.route('/h_recommendation')
def h_recommendation():
    d=session["disease"]
    s=review.h_senti(d)
    return render_template("hospital_list.html",d_list=s)

if __name__ == "__main__":
    app.debug = True
    app.run()