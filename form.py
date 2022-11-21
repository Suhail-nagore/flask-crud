from flask import Flask,redirect,render_template, request
import sqlite3 as sql
app=Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def student():
    return render_template('student.html')


@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method=='POST':
        try:
            addr=request.form['addr']
            city=request.form['city']
            pin=request.form['pin']
            nm=request.form['nm']
            with sql.connect('database.db') as con:
               cur=con.cursor()
               cur.execute('INSERT INTO students (name,addr,city,pin) VALUES(?,?,?,?)',(nm,addr,city,pin))
               msg='Record succesfully added'
        except:
            con.rollback()
            msg='error in inserting the data'
        finally:
            return render_template('result.html',msg=msg)
            con.close()




@app.route('/list')
def list():
    con=sql.connect('database.db')
    con.row_factory=sql.Row
    cur=con.cursor()
    cur.execute('SELECT * FROM students')
    rows=cur.fetchall();
    return render_template('list.html',rows=rows)

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method=='POST':
        result=request.form
        return render_template('table.html',result=result)
    

if __name__=='__main__':
    app.run(debug=True)
