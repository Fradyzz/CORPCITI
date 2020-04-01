from tkinter import messagebox;
import pyodbc
class baseDeDatos():
    def __init__(self):
        pass;

    def pruebaConexion(self):
        self.direccion_servidor='BRADOG';
        self.nombre_bd='corpciti';
        self.nombre_usuario ='sa';
        self.password='123';
        try:
            self.conexion=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+
                                      self.direccion_servidor+';DATABASE='+self.nombre_bd+';UID='+
                                      self.nombre_usuario+';PWD='+self.password);
            return self.conexion;
        except Exception as e:
            messagebox.showerror("Error de conexión", "Hubo un error al conectar la base datos\n{}".format(e));

    def insertaUser(self, tupla):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta="INSERT INTO usuario(cedula, nombre, apellido, fechanacim, nick, telefono, email, contrasena) VALUES (?, ?, ?, ?, ?, ?, ?, ?);";
                cursor.execute(self.consulta, tupla);
        except Exception as e:
            messagebox.showerror("Error de ingreso", "Hubo un error al insertar\n{}".format(e));
        finally:
            self.pruebaConexion().close();

    def insertaEnlista(self, codeUser, codeEvent):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta="INSERT INTO enlista(codigo_usuario, codigo_evento) VALUES (?, ?);";
                cursor.execute(self.consulta, codeUser, codeEvent);
        except Exception as e:
            messagebox.showerror("Error de ingreso", "Hubo un error al insertar\n{}".format(e));
        finally:
            self.pruebaConexion().close();

    def insertaEvent(self, tupla):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta="INSERT INTO evento(nombre, descripcion, lugar, fecha, hora, boletos, codigo_admin) VALUES (?, ?, ?, ?, ?, ?, ?);";
                cursor.execute(self.consulta, tupla);
        except Exception as e:
            messagebox.showerror("Error de ingreso", "Hubo un error al insertar\n{}".format(e));
        finally:
            self.pruebaConexion().close();

    def daCodeAdmi(self):
        try:
            with self.pruebaConexion().cursor() as cursor:
                cursor.execute('SELECT codigo FROM administrador;');
                administrador = cursor.fetchall();
                return administrador;
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se entregaron lso datos");
        finally:
            self.pruebaConexion().close()

    def compruebaEnlisa(self, tempCodeUser, codeEvent):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta='SELECT * FROM enlista WHERE codigo_usuario=? AND codigo_evento=?;';
                cursor.execute(self.consulta, (tempCodeUser, codeEvent));
                if(cursor.fetchall()):
                    return True;
                else:return False;
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se entregaron lso datos");
        finally:
            self.pruebaConexion().close()

    def daFinalCodeUser(self):
        try:
            with self.pruebaConexion().cursor() as cursor:
                cursor.execute('SELECT COUNT(codigo) FROM usuario;');
                code = cursor.fetchall();
                return self.extraeArray(code);
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se entregaron lso datos");
        finally:
            self.pruebaConexion().close()

    def daFinalCodeEvent(self):
        try:
            with self.pruebaConexion().cursor() as cursor:
                cursor.execute('SELECT MAX(codigo) FROM evento;');
                code = cursor.fetchall();
                return self.extraeArray(code);
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se entregaron lso datos");
        finally:
            self.pruebaConexion().close()

    def daFinalCodeEventByAdmi(self, tempCodeAdmi):
        try:
            with self.pruebaConexion().cursor() as cursor:
                cursor.execute('SELECT COUNT(codigo) FROM evento WHERE codigo_admin=?;', tempCodeAdmi);
                code = cursor.fetchall();
                return self.extraeFor(self.extraeArray(code));
        except Exception as e:
            return 0;
        finally:
            self.pruebaConexion().close()

    def daFinalCodeEventByUser(self, tempCodeUser):
        try:
            with self.pruebaConexion().cursor() as cursor:
                cursor.execute('SELECT COUNT(codigo_evento) FROM enlista WHERE codigo_usuario=?;', tempCodeUser);
                code = cursor.fetchall();
                return self.extraeFor(self.extraeArray(code));
        except Exception as e:
            messagebox.showerror("Error Base de Datos", "No se encontró registro con código {} en {}".format(tempCodeUser, e));
        finally:
            self.pruebaConexion().close()

    def daNameAdminByCode(self, tempCodeAdmi):
        try:
            with self.pruebaConexion().cursor() as cursor:
                cursor.execute('SELECT nombre FROM administrador WHERE codigo=?;', tempCodeAdmi);
                name=cursor.fetchall();
                for i in self.extraeArray(name):
                    return i;
        except Exception as e:
            return 0;
        finally:
            self.pruebaConexion().close()

    def daFinalCodeEventCount(self):
        try:
            with self.pruebaConexion().cursor() as cursor:
                cursor.execute('SELECT COUNT(codigo) FROM evento;');
                code = cursor.fetchall();
                return self.extraeFor(self.extraeArray(code));
        except Exception as e:
            return 0;
        finally:
            self.pruebaConexion().close()

    def daCodeUserWhere(self, nick, passw):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = 'SELECT codigo FROM usuario WHERE nick=? AND contrasena=?;';
                cursor.execute(self.consulta, (nick, passw));
                code = cursor.fetchall();
                return self.extraeFor(self.extraeArray(code));
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se entregaron lso datos");
        finally:
            self.pruebaConexion().close()

    def daCodeAdmiWhere(self, nick, passw):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = 'SELECT codigo FROM administrador WHERE nick=? AND contrasena=?;';
                cursor.execute(self.consulta, (nick, passw));
                code = cursor.fetchall();
                return self.extraeFor(self.extraeArray(code));
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se entregaron lso datos");
        finally:
            self.pruebaConexion().close()

    def devuelveCedulas(self):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT cedula FROM usuario UNION SELECT cedula FROM administrador;";
                cursor.execute(self.consulta);
                getCedul = cursor.fetchall();
                return getCedul;
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró cédula igual {}".format(e));
        finally:
            self.pruebaConexion().close();

    def devuelveEvents(self, indice):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT * FROM evento;";
                cursor.execute(self.consulta);
                getEvent = cursor.fetchall();
                return self.daArrayEnIndice(self.extraeArray(getEvent), indice);
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró dato en base al código{}".format(e));
        finally:
            self.pruebaConexion().close();

    def validaRepeatCedu(self, ceduIn):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT cedula FROM usuario UNION SELECT cedula FROM administrador;";
                cursor.execute(self.consulta);
                getCeduls = cursor.fetchall();
                for i in self.extraeArray(getCeduls):
                    if(ceduIn==i):
                        return True;
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró cédula igual {}".format(e));
        finally:
            self.pruebaConexion().close();

    def validaEventNull(self, tempCodeAdmi):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT * FROM evento WHERE codigo_admin=?;";
                cursor.execute(self.consulta, (tempCodeAdmi));
                variable=cursor.fetchall();
                if (self.extraeFor(variable)==None):
                    return False;
                else:
                    return True;

        except Exception as e: return False;
        finally:
            self.pruebaConexion().close();

    def validaEnlistaNull(self, tempCodeUser):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT * FROM enlista WHERE codigo_usuario=?;";
                cursor.execute(self.consulta, (tempCodeUser));
                variable=cursor.fetchall();
                if (self.extraeFor(variable)==None):
                    return False;
                else:
                    return True;

        except Exception as e: return False;
        finally:
            self.pruebaConexion().close();

    def validaEventNullI(self):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT * FROM evento;";
                cursor.execute(self.consulta);
                variable=cursor.fetchall();
                if (self.extraeFor(variable)==None):
                    return False;
                else:
                    return True;

        except Exception as e: return False;
        finally:
            self.pruebaConexion().close();

    def validaRepeatNick(self, nickIn):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT nick FROM usuario UNION SELECT nick FROM administrador;";
                cursor.execute(self.consulta);
                getNicks = cursor.fetchall();
                for i in self.extraeArray(getNicks):
                    if(nickIn==i):
                        return True;
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró nick igual {}".format(e));
        finally:
            self.pruebaConexion().close();

    def devuelvePass(self, cedula):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT contrasena FROM usuario WHERE cedula=? UNION SELECT contrasena FROM administrador WHERE cedula=?;"
                cursor.execute(self.consulta, (cedula, cedula))
                getpass = cursor.fetchall();
                for i in getpass:
                    return i;
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró contraseña {}".format(e));
        finally:
            self.pruebaConexion().close();

    def extraeArray(self, funcion):
        llena = [];
        for i in funcion:
            for j in i:
                llena.append(j);
        return(llena);

    def extraeTupla(self, funcion):
        llena = [];
        for i in funcion:
            llena.append(i);
        return (llena);

    def extraeFor(self, rango):
        for i in rango:
            return i;

    def insertAdmi(self, codigo, cedula, nombre, apell, fecha, nick, telefono, email, contra):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "UPDATE administrador SET cedula=?, nombre=?, apellido=?, fechanacim=?, nick=?, telefono=?, email=?, contrasena=? WHERE codigo=?;";
                cursor.execute(self.consulta, (cedula, nombre, apell, fecha, nick, telefono, email, contra, codigo));
            self.pruebaConexion().commit();
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se actualizaron los datos {}".format(e));
        finally:
            self.pruebaConexion().close();

    def daLogginUser(self, nick, passw):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT * FROM usuario WHERE nick=? AND contrasena=?;";
                cursor.execute(self.consulta, (nick, passw));
                if(cursor.fetchall()):
                    return(True);
                else: return False;
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró credenciales iguales {}".format(e));
        finally:
            self.pruebaConexion().close();

    def daLogginAdmi(self, nick, passw):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT * FROM administrador WHERE nick=? AND contrasena=?;";
                cursor.execute(self.consulta, (nick, passw));
                if(cursor.fetchall()):
                    return True;
                else: return False;
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró credenciales iguales {}".format(e));
        finally:
            self.pruebaConexion().close();

    def editaUser(self, codigo, cedula, nombre, apell, fecha, nick, telefono, email, contra,):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "UPDATE usuario SET cedula=?, nombre=?, apellido=?, fechanacim=?, telefono=?, email=?, nick=?, contrasena=? WHERE codigo=?;";
                cursor.execute(self.consulta, (cedula, nombre, apell, fecha, telefono, email, nick, contra, codigo));
            self.pruebaConexion().commit();
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se actualizaron los datos {}".format(e));
        finally:
            self.pruebaConexion().close();

    def editaAdmi(self, codigo, cedula, nombre, apell, fecha, nick, telefono, email, contra,):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "UPDATE administrador SET cedula=?, nombre=?, apellido=?, fechanacim=?, telefono=?, email=?, nick=?, contrasena=? WHERE codigo=?;";
                cursor.execute(self.consulta, (cedula, nombre, apell, fecha, telefono, email, nick, contra, codigo));
            self.pruebaConexion().commit();
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se actualizaron los datos {}".format(e));
        finally:
            self.pruebaConexion().close();

    def editaEvent(self, codigo, codeAdmin, nombre, descrip, lugar, fecha, hora, boletos):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "UPDATE evento SET nombre=?, descripcion=?, lugar=?, fecha=?, hora=?, boletos=? WHERE codigo=? AND codigo_admin=?;";
                cursor.execute(self.consulta, (nombre, descrip, lugar, fecha, hora, boletos, codigo, codeAdmin));
            self.pruebaConexion().commit();
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se actualizaron los datos {}".format(e));
        finally:
            self.pruebaConexion().close();

    def daUnDatoUser(self, codigo, indice):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT * FROM usuario WHERE codigo=?;";
                cursor.execute(self.consulta, (codigo));
                getUser = cursor.fetchall();
                return self.daArrayEnIndice(self.extraeArray(getUser), indice);
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró dato en base al código{} {}".format(codigo, e));
        finally:
            self.pruebaConexion().close();

    def daUnDatoAdmi(self, codigo, indice):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT * FROM administrador WHERE codigo=?;";
                cursor.execute(self.consulta, (codigo));
                getUser = cursor.fetchall();
                return self.daArrayEnIndice(self.extraeArray(getUser), indice);
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró dato en base al código{} {}".format(codigo, e));
        finally:
            self.pruebaConexion().close();

    def daUnDatoEvent(self, tempCodeAdmi, indice):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT * FROM evento WHERE codigo_admin=?;";
                cursor.execute(self.consulta, (tempCodeAdmi));
                getEvent = cursor.fetchall();
                return self.daArrayEnIndice(self.extraeArray(getEvent), indice);
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró dato en base al código{} {}".format(tempCodeAdmi, e));
        finally:
            self.pruebaConexion().close();

    def daCodeUserEnlista(self, tempCodeUser, indice):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT codigo_evento FROM enlista WHERE codigo_usuario=?;";
                cursor.execute(self.consulta, (tempCodeUser));
                getEvent = cursor.fetchall();
                return self.daArrayEnIndice(self.extraeArray(getEvent), indice);
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró dato en base del código{} {}".format(tempCodeUser, e));
        finally:
            self.pruebaConexion().close();

    def daUnDatoEventByCode(self, codigoEvent, indice):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT * FROM evento WHERE codigo=?;";
                cursor.execute(self.consulta, (codigoEvent));
                getEvent = cursor.fetchall();
                return self.daArrayEnIndice(self.extraeArray(getEvent), indice);
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró dato en base al código{} {}".format(codigoEvent, e));
        finally:
            self.pruebaConexion().close();

    def daArrayEnIndice(self, rango, indice):
        llena=[];
        for i in rango:
            llena.append(i);
        return llena[indice];