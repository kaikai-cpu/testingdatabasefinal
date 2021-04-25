from flask import Flask, render_template, request

from flask_mysqldb import MySQL

app =  Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']='cannabis' 
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'



mysql = MySQL(app)

app.static_folder = 'static'

@app.route('/strains', methods=["GET","POST"])
def strains():
    render_template("strains.html")
    search = request.form.get("search")
    if search == None:
        search = 5
    cur = mysql.connection.cursor()
    sqlquery = ("SELECT * from cannabisreco WHERE Rating = "+str(search))
    print(sqlquery)
    cur.execute(sqlquery)
    results= cur.fetchall()
    
    print(results)

    p = []
    tbl = "<tr><td>Strain</td><td>Type</td><td>Rating</td><td>Flavor</td><td>Description</td></tr>"
    p.append(tbl)
    for row in results:
        a = "<tr><td>%s</td>"%row['Strain']
        p.append(a)
        b = "<td>%s</td>"%row['Type']
        p.append(b)
        c = "<td>%s</td>"%row['Rating']
        p.append(c)
        d = "<td>%s</td></tr>"%row['Effects']
        p.append(d)
        e = "<td>%s</td></tr>"%row['Description']
        p.append(e)

    return(render_template("strains.html",data = results, table = p))

@app.route('/')
def age_confirmation():
    return render_template("ageconfirmation.html")

if __name__ =="__main__":
    app.run(debug=True)

