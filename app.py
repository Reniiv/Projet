from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         pseudo= request.form['pseudo']
         email = request.form['email']
         mdp = request.form['mdp']
         
         
         with sql.connect("database\database.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO client (pseudo,email,mdp) VALUES (?,?,?)",(pseudo,email,mdp) )
            
            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

if __name__ == '__main__':
   app.run(debug = True,use_reloader=False)
   
