import pandas as pd;
from pandas import ExcelWriter;
from openpyxl.writer.excel import ExcelWriter
class Repos():
    eventos=[]; usuarios=[]; admins=[];
    def __init__(self, eventos=[], usuarios=[], admins=[]):
        self.eventos=eventos;
        self.usuarios=usuarios;
        self.admins=admins;
    def loguinUser(self, user, contra):
        for i in self.usuarios:
            if (i.nick == user and i.contrase==contra):
                return True;
            else: return False;
    def loguinAdmi(self, user, contra):
        for i in self.admins:
            if (i.nick == user and i.contrase==contra):
                return True;
            else: return False;
    def insertaEvent(self, ob):
        self.eventos.append(ob);
    def insertaUser(self, ob):
        self.usuarios.append(ob);
    def insertaAdm(self, ob):
        self.admins.append(ob);
    def countEvent(self):
        c=0;
        for i in self.eventos:
            c+=1;
        return c;
    def countUser(self):
        c=0;
        for i in self.usuarios:
            c+=1;
        return c;
    def countAdm(self):
        c=0;
        for i in self.admins:
            c+=1;
        return c;
    def listataEvent(self, i):
        return (self.eventos[i]);
    def listataUser(self, i):
        return(self.usuarios[i]);
    def listataAdm(self, i):
        return (self.admins[i]);
    def editaEvent(self, cod, ob):
        c=0;
        for i in self.eventos:
            if(i.codEvent==cod):
                self.eventos[c]=ob;
            c+=1;
    def editaUser(self, cod, ob):
        c=0;
        for i in self.usuarios:
            if(i.codigo==cod):
                self.usuarios[c]=ob;
            c+=1;
    def editaAdm(self, cod, ob):
        c=0;
        for i in self.admins:
            if(i.codigo==cod):
                self.admins[c]=ob;
            c+=1;
    def buscaEvent(self, cod, iter):
        for i in self.eventos:
            if(i.codEvent==cod):
                return(self.eventos[iter]);
    def buscaUser(self, cod, iter):
        for i in self.usuarios:
            if (i.codigo == cod):
                return (self.usuarios[iter]);
    def buscaAdm(self, cod, iter):
        for i in self.admins:
            if (i.codigo == cod):
                return (self.admins[iter]);
    def borraEvent(self, cod):
        for i in self.eventos:
            if(i.codEvent==cod):
                self.eventos.remove(i);
    def borraUser(self, cod):
        for i in self.usuarios:
            if(i.codigo==cod):
                self.usuarios.remove(i);
    def borraAdm(self, cod):
        for i in self.admins:
            if(i.codigo==cod):
                self.admins.remove(i);
    def SaveExcelEvent(self):
        coA=[]; nomA=[]; descrA=[]; lugA=[]; fechaA=[]; horaA=[];
        for i in self.eventos:
            coA.append(i.codEvent); nomA.append(i.nomEvent);
            descrA.append(i.descrEvent); lugA.append(i.lugar);
            fechaA.append(i.fecha); horaA.append(i.hora);
        data = {'Codigo': coA, 'Nombre': nomA, 'Descripción': descrA, 'Lugar': lugA, 'Fecha': fechaA, 'Hora': horaA}
        #data2 = [{'Tipo': t, 'Cantidad': ca}];
        df = pd.DataFrame(data, columns=['Codigo', 'Nombre', 'Descripción', 'Lugar', 'Fecha', 'Hora']);
        writer = ExcelWriter('RegistroEventos.xlsx');
        df.to_excel(writer, index=False);
        writer.save();
    def SaveExcelUser(self):
        coA=[]; ceduA=[]; nomA=[]; apellA=[]; fNacimA=[]; nickA=[]; telfA=[]; emailA=[]; contraseA=[];
        for i in self.usuarios:
            coA.append(i.codigo); ceduA.append(i.cedula); nomA.append(i.nombre);
            apellA.append(i.apellido); fNacimA.append(i.fNacim);
            nickA.append(i.nick); telfA.append(i.telf); emailA.append(i.email);
            contraseA.append(i.contrase);
        data = {'Codigo': coA, 'Cédula':ceduA, 'Nombre': nomA, 'Apellido': apellA,
                'Fecha de Naicimiento': fNacimA, 'Nick': nickA,
                'Teléfono': telfA, 'Email': emailA, 'Contraseña:': contraseA}
        #data2 = [{'Tipo': t, 'Cantidad': ca}];
        df = pd.DataFrame(data, columns=['Codigo','Cédula','Nombre','Apellido','Fecha de Nacimiento',
                                         'Nick','Teléfono','Email','Contraseña']);
        writer = ExcelWriter('RegistroUsuarios.xlsx');
        df.to_excel(writer, index=False);
        writer.save();
    def SaveExcelAdmin(self):
        coA=[]; ceduA=[]; nomA=[]; apellA=[]; nickA=[]; telfA=[]; emailA=[]; contraseA=[];
        for i in self.admins:
            coA.append(i.codigo); ceduA.append(i.cedula); nomA.append(i.nombre);
            apellA.append(i.apellido); nickA.append(i.nick);
            telfA.append(i.telf); emailA.append(i.email);
            contraseA.append(i.contrase);
        data = {'Codigo': coA, 'Cédula':ceduA, 'Nombre': nomA, 'Apellido': apellA, 'Nick': nickA,
                'Teléfono': telfA, 'Email': emailA, 'Contraseña:': contraseA}
        df = pd.DataFrame(data, columns=['Codigo', 'Cédula', 'Nombre','Apellido','Fecha de Nacimiento',
                                         'Nick','Teléfono','Email','Contraseña']);
        writer = ExcelWriter('RegistroAdmins.xlsx');
        df.to_excel(writer, index=False);
        writer.save();