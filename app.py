from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Mysql connection
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts' #nombre de la base de datos
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'
#para decirle como va a ir protegida nuestra sesion

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)
#con fetchall almacenamos todos los datos de la consulta y le pasamos data al html con el nombre de contacts

#a esa ruta la enviamos a través del método POST
@app.route('/add_contact', methods = ['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        print(fullname)
        print(phone)
        print(email)
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()
        flash('Contact added successfully')

    return redirect(url_for('index'))
#el cursor permite ejecutar las consultas de mysql, es algo asi como obtener la coneccion con mysql. con cur.execute escribimos la consulta y con mysql.connection.commit ejecutamos la consulta
#cuando terminamos, redireccionamos a la vista principal con el redirect y el url_for

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contact Removed Succesfully')
    return redirect(url_for('index'))
#a la ruta delete tenemos que entregarle un parametro, este sera un string de tipo id; cada vez que usemos la ruta delete, tendra que tener al lado un numero para eliminarlo


@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = {0}'.format(id))
    data = cur.fetchall()
    #print(data[0])
    return render_template('edit-contact.html', contact = data[0])

#estamos creando una nueva pestaña para editar el contacto, lo que hacemos en editar es pasarle el indice del contacto seleccionado y luego se obtiene todos sus datos de la consulta sql y se le pasa a edit-contact.html

@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        email = request.form['email']
        phone = request.form['phone']
        cur = mysql.connection.cursor()
        cur.execute('''
            UPDATE contacts
            SET fullname = %s,
                email = %s,
                phone = %s
            WHERE id = %s
        ''', (fullname,email,phone,id))
        mysql.connection.commit()
        flash('Contact updated Succesfully')
        return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(port=3000, debug=True)