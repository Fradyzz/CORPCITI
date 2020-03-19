class Evento():
    def __init__(self, codEvent, nomEvent, descrEvent, lugar, fecha, hora, boletos):
        self.codEvent=codEvent;
        self.nomEvent=nomEvent;
        self.descrEvent=descrEvent;
        self.lugar=lugar;
        self.fecha=fecha;
        self.hora=hora;
        self.boletos=boletos;
    def __str__(self):
        return("Código: {}\nNombre: {}\nDescripción: {}\nLugar: {}\n"
               "Fecha: {}\nHora: {}\nBoletos: {}".format(self.codEvent, self.nomEvent,
                                            self.descrEvent, self.lugar,
                                            self.fecha, self.hora, self.boletos));
class Persona():
    def __init__(self, codigo, cedula, nombre, apellido, fNacim, nick, telf, email, contrase):
        self.codigo=codigo;
        self.cedula=cedula;
        self.nombre=nombre;
        self.apellido=apellido;
        self.fNacim=fNacim;
        self.nick=nick;
        self.telf=telf;
        self.email=email;
        self.contrase=contrase;
    def __str__(self):
        return("Código: {}\nCedula:{}\nNombres: {}\nApellidos: {}\n Fecha de Nacimiento: {}\nNombre de Usuario: {}"
               "\nTeléfono: {}\nEmail: {}\nContraseña: {}"
               .format(self.codigo, self.cedula, self.nombre, self.apellido, self.fNacim, self.nick,
                       self.telf, self.email, self.contrase));
class Usuario(Persona):
    def __init__(self, codigo, cedula, nombre, apellido, fNacim, nick, telf, email, contrase):
        super().__init__(codigo, cedula, nombre, apellido, fNacim, nick, telf, email, contrase);
    def __str__(self):
        return super().__str__();
class Admin(Persona):
    def __init__(self, codigo, cedula, nombre, apellido, fNacim, nick, telf, email, contrase):
        super().__init__(codigo, cedula, nombre, apellido, fNacim, nick, telf, email, contrase);
    def __str__(self):
        return super().__str__();