#backend kısmı burasi
#pythonla yazılan bir backenddir flask
#yapay zeka veri tabani vs tüm backend burda pythonda yazılır

from flask import Flask, render_template, request,redirect,url_for
#flask indirsem de vscode da gözükmedi anacondadan vscode u launch edince flaskı görüyor
import mysql.connector
#pip install mysql-connector-python

print("a")

app= Flask(__name__)

db=mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='12345',
    database='ai28'
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/kayitol' ,methods=['POST']) #kayit ol formunun adi
def kayitol():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['password']

        cursor=db.cursor()
        cursor.execute('INSERT INTO kullanici_bilgisi (name,email,password) VALUES (%s,%s,%s)',(name,email,password))
        db.commit()
        db.close()
        return redirect(url_for("index"))
    
"""cursor=db.cursor()
name="ahmet"
email= 'ahmet@ahmet'
password="5678"
user_id=1

cursor.execute("UPDATE kullanici_bilgisi SET name=%s, email=%s , password=%s WHERE id=%s", (name,email,password,user_id))
db.commit()
db.close()
cursor=db.cursor()
user_id=1
"""

"""cursor.execute("DELETE FROM kullanici_bilgisi WHERE id = %s", (user_id,))
db.commit()
db.close()"""

if __name__=='__main__':
    app.run(debug=True)