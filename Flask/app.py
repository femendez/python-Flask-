from flask import Flask, render_template, request, redirect, url_for,flash
from flask_mysqldb import MySQL
from datetime import datetime
import smtplib
fec_act = datetime.now()

app=Flask(__name__)

app.secret_key='M@ncitor02'

#Base de Datos
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='sisglobal'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''

mysql=MySQL(app)

@app.route('/')
def Index():
    cur=mysql.connection.cursor()
    cur.execute('select d.*,s.txt_sexo from dpersona d inner join dsexo s on d.cod_sexo = s.txt_cod_sexo')
    datos=cur.fetchall()
    return render_template('index.html',contactos=datos)

@app.route('/add_contacto',methods=['POST'])
def add_contacto():
    if request.method == 'POST':
        txt_name=request.form['txt_name'].upper()
        txt_pass=request.form['txt_pass']
        txt_email=request.form['txt_email'].upper()
        txt_dir=request.form['txt_dir'].upper()
        txt_cel=request.form['txt_cel'].upper()
        txt_sexo=request.form['txt_sexo']
        cur=mysql.connection.cursor()
        sSql='Select * from users where txt_usuario = "{0}"'.format(txt_name)
        #print(txt_sexo)
        cur.execute(sSql)
        rdoRs=cur.fetchall()
        print(len(rdoRs))
        if len(rdoRs)==0:
            cur = mysql.connection.cursor()
            sSql = 'insert into users(txt_usuario, txt_pass,txt_mail, txt_dir,txt_cel,txt_sexo) ' 
            sSql = sSql +'values(%s, %s, %s, %s,  %s, %s)'
            cur.execute(sSql,(txt_name,txt_pass,txt_email,txt_dir,txt_cel, txt_sexo))
            mysql.connection.commit()    
    else :
        flash('You were successfully logged in')        
    return render_template('index.html')



@app.route('/borrar/<string:id>')
def borrar(id):
    cur=mysql.connection.cursor()
    cur.execute('delete from dpersona where id_persona = {0}'.format(id))
    mysql.connection.commit ()

    return redirect(url_for('Index'))
    
@app.route('/update/<id>',methods=['POST'])
def update_contact(id):
    if request.method == 'POST':
        id_persona=id
        txt_nombre = request.form['txt_nombre']
        txt_apellido = request.form['txt_apellido']
        txt_sexo = request.form['txt_sexo']
        cur=mysql.connection.cursor()
        sSql='Update dpersona set txt_nombre = %s, txt_apellido = %s, txt_sexo=%s where id_persona = %s'
        cur.execute(sSql,(txt_nombre.upper(),txt_apellido.upper(),txt_sexo,id_persona))  
        mysql.connection.commit()      
    return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_dpersona(id):
    cur=mysql.connection.cursor()
    cur.execute('select * from dpersona where id_persona={0}'.format(id)+' order by txt_nombre')
    dato=cur.fetchall()
    #mysql.connection.commit()
    print('entro en editar......')
    return render_template('edit_persona.html',contacto = dato[0])

@app.route('/add_pedido/<id>')
def add_pedido(id):
    cur=mysql.connection.cursor()
    sSql='Select cod_producto,txt_desc,invent,txt_presentacion from dproducto'
    cur.execute('select * from dproducto')
    Datos=cur.fetchall()
    print(id)
    return render_template('pedido.html',pedido=Datos)



@app.route('/add_pedido1/<id>')
def add_pedido1(id):
    cur=mysql.connection.cursor()
    sSql='Select cod_producto,txt_desc,invent,txt_presentacion from dproducto'
    cur.execute('select * from dproducto')
    Datos=cur.fetchall()
    print(id)
    return 'chong'

@app.route('/users')
def user():
    return render_template('users.html')


@app.route('/new_user')
def new_user():
    return render_template('new_user.html')

@app.route('/seek_user',methods=['POST'])
def seek_user():
    if request.method == 'POST':
        txt_user=request.form['txt_user'].upper()
        txt_pass=request.form['txt_pass']
        cur = mysql.connection.cursor()
        sSql='Select * from users where txt_usuario = %s and txt_pass = %s'
        cur.execute(sSql,(txt_user,txt_pass))
        rdo=cur.fetchall()
        print(rdo)
        if len(rdo) == 0 :
            sSql='no hay chong chong base datos '
        else:
            sSql='si hay  chong.....base de datos  pass:=' + txt_pass + ' user:= ' + txt_user       
    return render_template('users.html')


@app.route('/credito')
def creditos():
    cur = mysql.connection.cursor()
    sSql = 'select distinct txt_desc from fpago order by txt_desc'
    cur.execute(sSql)
    rdo = cur.fetchall() 
    return render_template('calcredito.html', rdos = rdo)


@app.route('/ccredito',methods=['POST'])
def calcreditos():
    #
    if request.method == 'POST':
        ipago = float(request.form['ipago'])
        tasa_iva  = float(request.form['imp_iva'])/100
        imp_credito = float(request.form['imp_credito']) * (1 + tasa_iva)  
        imp_tasa = ((float(request.form['imp_tasa']))/ipago)/100
        imp_tasa = imp_tasa * (1 + tasa_iva)
        imp_cuota = pow((1+imp_tasa),ipago)*imp_tasa
        imp_cuota = (imp_cuota / (pow((1+imp_tasa),ipago) - 1)) * imp_credito
                
        i=1
        cur=mysql.connection.cursor()
        cur.execute('delete from amortizacion')
        mysql.connection.commit()

        sSql='insert into amortizacion (id_persona,nro_cuota,imp_amortizacion,imp_interes,imp_saldo, imp_iva, imp_interes_iva,imp_interes_cred, imp_amort_cuota)'
        sSql = sSql + ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s,%s)'
        cur.execute(sSql,(1,0,round(imp_cuota,2),0,round(imp_credito,2),0,0,0,0))
        mysql.connection.commit()
        while i<= ipago:
            imp_interes= round(imp_credito * (imp_tasa),2)
            imp_amortiza = imp_cuota - imp_interes 
            imp_credito = imp_credito - imp_amortiza
            imp_interes_iva = round((imp_interes * tasa_iva),2)
            imp_iva = round(imp_amortiza - (imp_amortiza / (1+tasa_iva)),2)
            imp_interes_cre = round((imp_interes - imp_interes_iva),2)
            imp_amort_cuota = round(imp_amortiza - imp_iva,2)

            sSql='insert into amortizacion (id_persona,nro_cuota,imp_amortizacion,imp_interes,imp_saldo, imp_iva, imp_interes_iva, imp_interes_cred, imp_amort_cuota)'
            sSql = sSql + ' VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            print(sSql)
            cur.execute(sSql,(1,i,round(imp_amortiza,2),round(imp_interes,2),round(imp_credito,2),round(imp_iva,2),round(imp_interes_iva,2),imp_interes_cre,imp_amort_cuota))
            i +=1
            mysql.connection.commit()
            sSql = 'Select * from amortizacion'
            cur.execute(sSql)
            rdo = cur.fetchall()
    return render_template('tablacredito.html', rdos = rdo)

#--------envio de correos electronicos masivos una vez registrado
# Configuración del servidor SMTP
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'edigraficasmendez@gmail.com'
SMTP_PASSWORD = 'malparidae'

def enviar_correo(destinatario):
    remitente = SMTP_USERNAME
    asunto = 'Registro exitoso'
    mensaje = 'Gracias por registrarte en nuestra aplicación'

    # Crear objeto de conexión SMTP
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls()
    smtp.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Crear mensaje de correo electrónico
    mensaje_correo = f'To: {destinatario}\nSubject: {asunto}\n\n{mensaje}'

    # Enviar correo electrónico
    smtp.sendmail(remitente, destinatario, mensaje_correo)
    smtp.quit()

if __name__ == '__main__':
    app.run(port=5050,debug=True)
    