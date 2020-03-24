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
                                      self.nombre_usuario+';PWD=' +self.password);
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

    def devuelveCedulas(self):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "SELECT cedula FROM usuario UNION SELECT cedula FROM administrador;"
                cursor.execute(self.consulta)
                getCedul = cursor.fetchall();
                return getCedul;
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se encontró cédula igual {}".format(e));
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

    def insertAdmi(self, codigo, cedula, nombre, apell, fecha, nick, telefono, email, contra,):
        try:
            with self.pruebaConexion().cursor() as cursor:
                self.consulta = "UPDATE administrador SET cedula=?, nombre=?, apellido=?, fechanacim=?, nick=?, telefono=?, email=?, contrasena=? WHERE codigo=?;";
                cursor.execute(self.consulta, (cedula, nombre, apell, fecha, nick, telefono, email, contra, codigo));
            self.pruebaConexion().commit();
        except Exception as e:
            messagebox.showerror("Error de consulta", "No se actualizaron los datos {}".format(e));
        finally:
            self.pruebaConexion().close();

x=baseDeDatos();
print(x.extraeArray(x.devuelveCedulas()));
#print(x.extraeTupla(x.devuelvePass('0953895570')))
#print(x.convertCodeAdmi());
#print(x.daCodeAdmi())
#print("{}".format(x.daCodeAdmi(1130)));