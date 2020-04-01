from subprocess import SubprocessError
import Clases;
import Conexion;
import Repositorio;
from builtins import any
from lib2to3.btm_matcher import BottomMatcher
from tkinter import *;
from tkinter import ttk;
from tkinter import messagebox;
# from PIL import Image, ImageTk;
import webbrowser;
import pyperclip as clipboard;
from tokenize import String
from Tools.scripts.var_access_benchmark import B
Re=Repositorio.Repos();
Bd=Conexion.baseDeDatos();
class Ventana():
    def __init__(self):
        self.contCodePU = 1;
        # Recursos
        self.colorCorp = "#00A2CA";  # Color celeste de Corpciti
        self.fontOCR = "OCR A Extended";
        self.fontCali = "Calibri (Cuerpo)";
        self.colorFgW = "white";
        self.cursorBot = "hand2";
        # Ventana de Login
        self.ventLoginR = Tk();
        self.altoPantalla = self.ventLoginR.winfo_screenheight();  # Almacena la dimesión del alto de la pantalla en una variable
        self.anchoPantalla = self.ventLoginR.winfo_screenwidth();  # Almacena la dimesión del alto de la pantalla en una variable
        self.ventLoginR.title("Inicio");  # Da título a la ventana
        self.ventLoginR.config(bg=self.colorCorp);  # Color de fondo o background
        # Variables
        self.logPersonV = StringVar();
        self.logPassV = StringVar();
        # Da dimensiones a la ventana y establezco la posición
        self.ventLoginR.geometry("280x270+{}+{}".format(int(self.anchoPantalla / 3), int(self.altoPantalla / 3)));
        self.ventLoginR.iconbitmap("Recursos\corpcitico.ico");  # Inserta icono a la app
        self.ventLoginR.resizable(0, 0);  # Ventana no redimensionable
        # Labels
        self.labeLogTitu = Label(self.ventLoginR, text="CORPCITI", fg=self.colorFgW,
                                 bg=self.colorCorp, font=("Tw Cen MT Condensed Extra Bold", 26));
        self.labeLogTitu.pack(side="top");
        self.labeLogDesc = Label(self.ventLoginR, text="Inicia Sesión", fg=self.colorFgW,
                                 bg=self.colorCorp, font=(self.fontOCR, 14));
        self.labeLogDesc.place(x=5, y=60);
        self.labeLogUser = Label(self.ventLoginR, text="Usuario:", fg=self.colorFgW, bg=self.colorCorp,
                                 font=(self.fontOCR, 14));
        self.labeLogUser.place(x=7, y=95);
        self.labeLogPass = Label(self.ventLoginR, text="Contraseña:", fg=self.colorFgW, bg=self.colorCorp,
                                 font=(self.fontOCR, 14));
        self.labeLogPass.place(x=7, y=130);
        # Entrys
        self.entryUser = Entry(self.ventLoginR, textvariable=self.logPersonV, font=(self.fontCali, 12), width=14);
        self.entryUser.place(x=137, y=100);
        self.entryPass = Entry(self.ventLoginR, textvariable=self.logPassV, font=(self.fontCali, 12), width=14);
        self.entryPass.place(x=137, y=135);
        self.entryPass.config(show="*");
        # Botones
        self.botOlvidarPass = Button(self.ventLoginR, text="Recordar contraseña", font=(self.fontOCR, 9),
                                     fg=self.colorFgW, bg=self.colorCorp, relief="flat", cursor=self.cursorBot,
                                     command=self.ventRecuerdaPass);
        self.botOlvidarPass.place(x=123, y=155);
        self.botRegis = Button(self.ventLoginR, text="Registro", command=self.ventRegistro, font=(self.fontOCR, 12),
                               fg=self.colorFgW, bg=self.colorCorp, relief="groove", cursor=self.cursorBot);
        self.botRegis.place(x=30, y=195);
        self.botLoggin = Button(self.ventLoginR, text="Ingresar", font=(self.fontOCR, 12), fg=self.colorFgW,
                                bg=self.colorCorp, relief="groove", cursor=self.cursorBot,
                                command=lambda:[self.validacionlogin(self.daLoginCode(self.logPersonV.get(), self.logPassV.get()),
                                                self.daLoginCodeA(self.logPersonV.get(), self.logPassV.get()))]);
        self.botLoggin.place(x=150, y=195);
        # flat, groove, raised, ridge, solid, or sunken
        self.ventLoginR.mainloop();

    def ventRecuerdaPass(self):
        self.ventGetPass=Toplevel(self.ventLoginR);
        self.ventGetPass.grab_set();
        self.ventGetPass.title("Recordar Contraseña");
        self.ventGetPass.config(bg=self.colorFgW);
        self.ventGetPass.geometry("300x200+{}+{}".format(int(self.anchoPantalla/3), int(self.altoPantalla/3)));
        self.ventGetPass.iconbitmap("Recursos\corpcitico.ico");
        self.ventGetPass.resizable(0, 0);
        #Control
        self.validarInCeduP=self.ventGetPass.register(self.validaCedulaIn);
        #Variables
        self.cedulaPV=StringVar();
        self.resultPV=StringVar();
        #Labels
        self.labelTituloP=Label(self.ventGetPass, text="RECORDANDO...", fg=self.colorCorp, bg=self.colorFgW,
                                  font=("Tw Cen MT Condensed Extra Bold", 26));
        self.labelTituloP.place(x=20, y=10);
        self.labelCeduP=Label(self.ventGetPass, text="Cédula:", fg=self.colorCorp, bg=self.colorFgW,
                                  font=(self.fontOCR, 14));
        self.labelCeduP.place(x=30, y=70);
        self.labelResultP=Label(self.ventGetPass, text="Result:", fg=self.colorCorp, bg=self.colorFgW,
                                font=(self.fontOCR, 14));
        self.labelResultP.place(x=30, y=100);
        #Entry
        self.entryCeduP=Entry(self.ventGetPass, font=(self.fontCali, 14), textvariable=self.cedulaPV,
                                foreground=self.colorFgW, background=self.colorCorp,
                                validate="key", validatecommand=(self.validarInCeduP, "%S"));
        self.cedulaPV.trace("w", lambda *args: self.limitadorCedula(self.cedulaPV));
        self.entryCeduP.place(x=120, y=70, width=150);
        self.entryResultP=Entry(self.ventGetPass, font=(self.fontCali, 14), textvariable=self.resultPV,
                                foreground=self.colorFgW, background=self.colorCorp, state=DISABLED);
        self.entryResultP.place(x=120, y=100, width=150);
        #Botones
        self.botonAceptP=Button(self.ventGetPass, text="Aceptar", font=(self.fontOCR, 14),
                                fg=self.colorFgW, bg=self.colorCorp, relief="groove", cursor=self.cursorBot,
                                command=self.validacionPass);
        self.botonAceptP.place(x=45, y=140);
        self.botonCancelaP=Button(self.ventGetPass, text="Cancelar", font=(self.fontOCR, 14),
                                  fg=self.colorFgW, bg=self.colorCorp, relief="groove", cursor=self.cursorBot,
                                  command=lambda:[self.destroyVentana(self.ventGetPass)]);
        self.botonCancelaP.place(x=155, y=140);

    def validacionPass(self):
        cont=0;
        for i in Bd.extraeArray(Bd.devuelveCedulas()):
            if(self.cedulaPV.get()==i):
                self.entryResultP.config(state='readonly', foreground=self.colorCorp);
                self.resultPV.set(Bd.extraeTupla(Bd.devuelvePass(self.cedulaPV.get())));
                clipboard.copy=self.resultPV.get();
                #messagebox.showinfo("Copiar Contraseña", "Se copió la contraseña al Clipboard")
                cont += 1;
        if (cont==0):
            self.resultPV.set("");
            self.entryResultP.config(state=DISABLED);
            messagebox.showerror("Error de consulta",
                                 "La cédula ingresada no pertenece a ninguna cuenta registrada");

    def daLoginCode(self, nick, passw):
        return Bd.daCodeUserWhere(nick, passw);

    def daLoginCodeA(self, nick, passw):
        return Bd.daCodeAdmiWhere(nick, passw);

    def loginCodeNull(self):
        self.tempCodeUser=0;

    def limitadorCedula(self, entry_text):
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[:10]);

    def validaCedulaIn(self, char):
        return char in "0123456789";

    def validaFechaIn(self, action, char, text):
        if action != "1":
            return True;
        return char in "0123456789/" and len(text) < 10;

    def web(self):
        webbrowser.open("http://corpciti.ec/", new=2, autoraise=True)

    def habilitaEntryCodigo(self):
        if (self.radioV.get()==1):
            self.entryRegCodi.config(state=DISABLED);
        elif(self.radioV.get()==2):
            self.entryRegCodi.config(state=NORMAL, textvariable=self.regCodeV);

    def decreceCodeEvent(self):
        self.incrementCodeEvent=self.incrementCodeEvent-1;
        self.eventCodeV.set(self.incrementCodeEvent);

    def validacionlogin(self, tempCodeUser, tempCodeAdmi):
        if (self.logPersonV.get()== "" or self.logPassV.get()== ""):
            messagebox.showerror("Error de Loggin", "Debes llenar los campos primero");
        elif(self.logPersonV.get().isspace() or self.logPassV.get().isspace()):
            messagebox.showerror("Error de Loggin", "Los espacios no cuenta como llenar los campos");
        elif (Bd.daLogginUser(self.logPersonV.get(), self.logPassV.get())==True):
            self.hideVentana(self.ventLoginR);
            self.ventInicioUser(tempCodeUser);
            self.limpiaLogin()
        elif(Bd.daLogginAdmi(self.logPersonV.get(), self.logPassV.get())==True):
            self.hideVentana(self.ventLoginR);
            self.ventInicioAdmi(tempCodeAdmi);
        else:
            messagebox.showerror("Error de Ingreso", "Usuario y Contraseña incorrectos");

    def validacionRegistro(self, tempCodeUser, tempCodeAdmi):
        if (self.radioV.get() == 0):
            messagebox.showwarning("Advertencia", "Escoge entre usuario o Administrador para registrarte por favor");
        elif (self.radioV.get() == 1):
            if (self.regCeduV.get().isspace() or self.regCeduV.get()=="" or
                self.regNomV.get().isspace() or self.regNomV.get() =="" or
                self.regApeV.get().isspace() or self.regApeV.get()=="" or
                self.regFechaV.get().isspace() or self.regFechaV.get()=="" or
                self.regUserV.get().isspace() or self.regUserV.get()=="" or
                self.regTelfV.get().isspace() or self.regTelfV.get()=="" or
                self.regMailV.get().isspace() or self.regMailV.get()=="" or
                self.regPass1V.get().isspace() or self.regPass1V.get()=="" or
                self.regPass2V.get().isspace() or self.regPass2V.get()==""):
                messagebox.showerror("Error Registro", "Hay campos vacíos\nDebes llenar todos los campos");
            elif(self.regPass1V.get()!=self.regPass2V.get()):
                messagebox.showerror("Error de Registro", "No coinciden las contraseñas");
            elif(Bd.validaRepeatCedu(self.regCeduV.get())==True):
                messagebox.showerror("Error de Registro", "Ya hay alguien registrado con ese número de cédula");
            elif(Bd.validaRepeatNick(self.regUserV.get())==True):
                messagebox.showerror("Error de Registro", "Ya hay alguien registrado con ese nombre de usuario");
            else:
                self.destroyVentana(self.ventRegisR);
                self.insertaPersona();
                self.ventInicioUser(tempCodeUser);
        elif (self.radioV.get() == 2):
            if(self.regCodeV.get().isspace() or self.regCodeV.get()=="" or
                self.regCeduV.get().isspace() or self.regCeduV.get() =="" or
                self.regNomV.get().isspace() or self.regNomV.get()=="" or
                self.regApeV.get().isspace() or self.regApeV.get()=="" or
                self.regFechaV.get().isspace() or self.regFechaV.get()=="" or
                self.regUserV.get().isspace() or self.regUserV.get()=="" or
                self.regTelfV.get().isspace()or self.regTelfV.get()=="" or
                self.regMailV.get().isspace() or self.regMailV.get()=="" or
                self.regPass1V.get().isspace() or self.regPass1V.get()=="" or
                self.regPass2V.get().isspace() or self.regPass2V.get() == ""):
                messagebox.showerror("Error de Registro", "Hay campos vacíos\nDebes llenar todos los campos");
            elif (self.regPass1V.get() != self.regPass2V.get()):
                messagebox.showerror("Error de Registro", "No coinciden las contraseñas");
            elif (Bd.validaRepeatCedu(self.regCeduV.get()) == True):
                messagebox.showerror("Error de Registro", "Ya hay alguien registrado con ese número de cédula");
            elif (Bd.validaRepeatNick(self.regUserV.get()) == True):
                messagebox.showerror("Error de Registro", "Ya hay alguien registrado con ese nombre de usuario");
            else:
                self.cont=0;
                for i in Bd.extraeArray(Bd.daCodeAdmi()):
                    if (int(self.regCodeV.get())==i):
                        self.destroyVentana(self.ventRegisR);
                        self.insertaPersona();
                        self.ventInicioAdmi(tempCodeAdmi);self.cont+=1;
                if (self.cont==0):
                    messagebox.showerror("Error de consulta",
                                         "El código ingresado no pertenece a ningún administrador en nuestra Base de Datos");

    def validacionEdicionUser(self, tempCodeUser):
        if (self.ceduVE.get().isspace() or self.ceduVE.get() == "" or
                self.nomVE.get().isspace() or self.nomVE.get() == "" or
                self.apeVE.get().isspace() or self.apeVE.get() == "" or
                self.fechaVE.get().isspace() or self.fechaVE.get() == "" or
                self.userVE.get().isspace() or self.userVE.get() == "" or
                self.telfVE.get().isspace() or self.telfVE.get() == "" or
                self.mailVE.get().isspace() or self.mailVE.get() == "" or
                self.pass1VE.get().isspace() or self.pass1VE.get() == ""):
            messagebox.showwarning("Error de Edición", "Debes llenar todos los campos");
        else:
            self.editaDatosUser(tempCodeUser);

    def validacionEdicionAdmi(self, tempCodeUser):
        if (self.ceduVEA.get().isspace() or self.ceduVEA.get() == "" or
                self.nomVEA.get().isspace() or self.nomVEA.get() == "" or
                self.apeVEA.get().isspace() or self.apeVEA.get() == "" or
                self.fechaVEA.get().isspace() or self.fechaVEA.get() == "" or
                self.userVEA.get().isspace() or self.userVEA.get() == "" or
                self.telfVEA.get().isspace() or self.telfVEA.get() == "" or
                self.mailVEA.get().isspace() or self.mailVEA.get() == "" or
                self.pass1VEA.get().isspace() or self.pass1VEA.get() == ""):
            messagebox.showwarning("Error de Edición", "Debes llenar todos los campos");
        else:
            self.editaDatosAdmi(tempCodeUser);

    def validacionEdicionEvent(self, tempCodeAdmi, text):
        if(self.myTitulV.get().isspace() or self.myTitulV.get()=="" or
           text.get(1.0, END).isspace() or text.get(1.0, END)=="" or
           self.myLugarV.get().isspace() or self.myLugarV.get()=="" or
           self.myFechaV.get().isspace() or self.myFechaV.get()=="" or
           self.myBoletoV.get().isspace() or self.myBoletoV.get()==""):
            messagebox.showwarning("Error de Edición", "Debes llenar todos los campos");
        else:
            self.editaEvento(tempCodeAdmi, text);

    def validacionEvent(self, tempCodeAdmi, textDescrip):
        self.tuplaEvent=(self.eventNomV.get(), textDescrip.get(1.0, END),
                         self.eventLugarV.get(), self.eventFechaV.get(),
                         self.eventHoraV.get(),self.eventBoleV.get(),
                         tempCodeAdmi);
        if (self.eventNomV.get()=="" or self.eventNomV.get().isspace() or
            textDescrip.get(1.0, END)=="" or textDescrip.get(1.0, END).isspace() or
            self.eventLugarV.get()=="" or self.eventLugarV.get().isspace() or
            self.eventFechaV.get()=="" or self.eventFechaV.get().isspace()):
            messagebox.showerror("Error de ingreso", "Hay campos vacíos\nDebes llenar todos los campos");
        else:
            Bd.insertaEvent(self.tuplaEvent);
            self.incrementCodeEvent = Bd.extraeFor(Bd.daFinalCodeEvent())+1;
            self.eventCodeV.set(self.incrementCodeEvent);
            self.eventNomV.set(""); textDescrip.delete(1.0, END);
            self.eventLugarV.set(""); self.eventFechaV.set("");
            self.eventHoraV.set("09:30 AM"); self.eventBoleV.set(1);
            messagebox.showinfo("Felicidades", "¡Se creó el evento exitosamente!");

    def validacionEnlista(self, tempCodeUser):
        if(Bd.compruebaEnlisa(tempCodeUser, self.myCodeEIUV.get())==True):
            messagebox.showerror("Error al enlistarse", "Ya te has enlistado a este evento");
        else:
            Bd.insertaEnlista(tempCodeUser, self.myCodeEIUV.get());
            messagebox.showinfo("Felicidades", "Te enlistaste a este evento exitosamente");

    def insertaPersona(self):
        self.tuplaPersona=(self.regCeduV.get(), self.regNomV.get(), self.regApeV.get(),
                           self.regFechaV.get(), self.regUserV.get(), self.regTelfV.get(),
                           self.regMailV.get(), self.regPass1V.get());
        if(self.radioV.get()==1):
            I1=Clases.Usuario(self.contCodePU, self.regCeduV.get(), self.regNomV.get(), self.regApeV.get(),
                              self.regFechaV.get(), self.regUserV.get(), self.regTelfV.get(),
                              self.regMailV.get(), self.regPass1V.get());
            Re.insertaUser(I1);
            Bd.insertaUser(self.tuplaPersona);
            self.contCodePU += 1;
        elif (self.radioV.get()==2):
            Cla = Clases.Admin(self.regCodeV.get(), self.regCeduV.get(), self.regNomV.get(),
                               self.regApeV.get(), self.regFechaV.get(), self.regUserV.get(),
                               self.regTelfV.get(), self.regMailV.get(), self.regPass1V.get());
            Re.insertaAdm(Cla);
            Bd.insertAdmi(self.regCodeV.get(), self.regCeduV.get(), self.regNomV.get(), self.regApeV.get(),
                           self.regFechaV.get(), self.regUserV.get(), self.regTelfV.get(),
                           self.regMailV.get(), self.regPass1V.get());

    def editaDatosUser(self, tempCodeUser):
        Bd.editaUser(tempCodeUser, self.ceduVE.get(), self.nomVE.get(),
                         self.apeVE.get(), self.fechaVE.get(),
                         self.userVE.get(), self.telfVE.get(),
                         self.mailVE.get(), self.pass1VE.get());
        messagebox.showinfo("Edición Exitosa", "Se editaron tus datos correctamente :)")

    def editaDatosAdmi(self, tempCodeUser):
        Bd.editaAdmi(tempCodeUser, self.ceduVEA.get(), self.nomVEA.get(),
                         self.apeVEA.get(), self.fechaVEA.get(),
                         self.userVEA.get(), self.telfVEA.get(),
                         self.mailVEA.get(), self.pass1VEA.get());
        messagebox.showinfo("Edición Exitosa", "Se editaron tus datos correctamente :)")

    def editaEvento(self, tempCodeAdmi, text):
        Bd.editaEvent(self.myCodeEV.get(), tempCodeAdmi, self.myTitulV.get(),
                      text.get(1.0, END), self.myLugarV.get(), self.myFechaV.get(),
                      self.myHoraV.get(), self.myBoletoV.get());
        messagebox.showinfo("Edición Exitosa", "Se editó tu evento correctamente :)")

    def actualizaEditaEvent(self):
        self.myCodeEV.set(Bd.daUnDatoEventByCode(self.myCodeEV.get(), 0));
        self.myTitulV.set(Bd.daUnDatoEventByCode(self.myCodeEV.get(), 1));
        self.myDescripV.set(Bd.daUnDatoEventByCode(self.myCodeEV.get(), 2));
        self.myLugarV.set(Bd.daUnDatoEventByCode(self.myCodeEV.get(), 3));
        self.myFechaV.set(Bd.daUnDatoEventByCode(self.myCodeEV.get(), 4));
        self.myHoraV.set(Bd.daUnDatoEventByCode(self.myCodeEV.get(), 5));
        self.myBoletoV.set(Bd.daUnDatoEventByCode(self.myCodeEV.get(), 6));
        self.myCodeAV.set(Bd.daUnDatoEventByCode(self.myCodeEV.get(), 7));

    def compruebaSgtEventI(self):
        if (Bd.daFinalCodeEventCount()==1):
            return (Bd.daFinalCodeEventCount()*8)-1;
        else:
            return (Bd.daFinalCodeEventCount()*8);

    def compruebaSgtEventM(self,tempCodeUser):
        if (Bd.daFinalCodeEventByUser(tempCodeUser)==1):
            return (Bd.daFinalCodeEventByUser(tempCodeUser)*8)-1;
        else:
            return (Bd.daFinalCodeEventByUser(tempCodeUser)*8);

    def compruebaSgtEventCodeM(self,tempCodeUser):
        if (Bd.daFinalCodeEventByUser(tempCodeUser)==1):
            return (Bd.daFinalCodeEventByUser(tempCodeUser)*1)-1;
        else:
            return (Bd.daFinalCodeEventByUser(tempCodeUser)*1)-1;

    def compruebaSgtEvent(self, tempCodeAdmi):
        if (Bd.daFinalCodeEventByAdmi(tempCodeAdmi)==1):
            return (Bd.daFinalCodeEventByAdmi(tempCodeAdmi)*8)-1;
        else:
            return (Bd.daFinalCodeEventByAdmi(tempCodeAdmi)*8);

    def sgtEvent(self, tempCodeAdmi):
        if(self.pos8<=self.compruebaSgtEvent(tempCodeAdmi)):
            self.pos0+=8; self.pos1+=8; self.pos2+=8; self.pos3+=8;
            self.pos4+=8; self.pos5+=8; self.pos6+=8; self.pos7+=8;
            self.pos8+=8;
            self.myCodeEV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos0));
            self.myTitulV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos1));
            self.myDescripV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos2));
            self.myLugarV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos3));
            self.myFechaV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos4));
            self.myHoraV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos5));
            self.myBoletoV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos6));
            self.myCodeAV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos7));
        elif(Bd.daFinalCodeEventByAdmi(tempCodeAdmi)==None):
            messagebox.showerror("Error", "No has creado eventos aún");
        elif (Bd.daFinalCodeEventByAdmi(tempCodeAdmi)==0):
            messagebox.showerror("Error", "No has creado eventos aún");
        else:
            messagebox.showinfo("Información", "No hay más eventos creados por ti");

    def antesEvent(self, tempCodeAdmi):
        self.totalPos=(Bd.daFinalCodeEventByAdmi(tempCodeAdmi)*8);
        if(self.pos0>0):
            self.pos0-=8; self.pos1-=8; self.pos2-=8; self.pos3-=8;
            self.pos4-=8; self.pos5-=8; self.pos6-=8; self.pos7-=8;
            self.pos8-=8;
            self.myCodeEV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos0));
            self.myTitulV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos1));
            self.myDescripV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos2));
            self.myLugarV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos3));
            self.myFechaV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos4));
            self.myHoraV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos5));
            self.myBoletoV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos6));
            self.myCodeAV.set(Bd.daUnDatoEvent(tempCodeAdmi, self.pos7));
        elif (self.totalPos==0):
            messagebox.showerror("Error", "No has creado eventos aún");
        elif (self.totalPos==None):
            messagebox.showerror("Error", "No has creado eventos aún");
        else:
            messagebox.showinfo("Información", "No hay más eventos antes de este");

    def sgtEventI(self):
        if(self.posI8<=self.compruebaSgtEventI()):
            self.posI0+=8; self.posI1+=8; self.posI2+=8; self.posI3+=8;
            self.posI4+=8; self.posI5+=8; self.posI6+=8; self.posI7+=8;
            self.posI8+=8;
            self.myCodeEIV.set(Bd.devuelveEvents(self.posI0));
            self.myTitulIV.set(Bd.devuelveEvents(self.posI1));
            self.myDescripIV.set(Bd.devuelveEvents(self.posI2));
            self.myLugarIV.set(Bd.devuelveEvents(self.posI3));
            self.myFechaIV.set(Bd.devuelveEvents(self.posI4));
            self.myHoraIV.set(Bd.devuelveEvents(self.posI5));
            self.myBoletoIV.set(Bd.devuelveEvents(self.posI6));
            self.myCodeAIV.set(Bd.devuelveEvents(self.posI7));
        elif(Bd.daFinalCodeEventCount()==None):
            messagebox.showerror("Error", "No se han creado eventos aún");
        elif (Bd.daFinalCodeEventCount()==0):
            messagebox.showerror("Error", "No se han creado eventos aún");
        else:
            messagebox.showinfo("Información", "No hay más eventos creados");

    def antesEventI(self):
        self.totalPosI=(Bd.daFinalCodeEventCount()*8);
        if(self.posI0>0):
            self.posI0-=8; self.posI1-=8; self.posI2-=8; self.posI3-=8;
            self.posI4-=8; self.posI5-=8; self.posI6-=8; self.posI7-=8;
            self.posI8-=8;
            self.myCodeEIV.set(Bd.devuelveEvents(self.posI0));
            self.myTitulIV.set(Bd.devuelveEvents(self.posI1));
            self.myDescripIV.set(Bd.devuelveEvents(self.posI2));
            self.myLugarIV.set(Bd.devuelveEvents(self.posI3));
            self.myFechaIV.set(Bd.devuelveEvents(self.posI4));
            self.myHoraIV.set(Bd.devuelveEvents(self.posI5));
            self.myBoletoIV.set(Bd.devuelveEvents(self.posI6));
            self.myCodeAIV.set(Bd.devuelveEvents(self.posI7));
        elif (self.totalPosI==0):
            messagebox.showerror("Error", "No han creado eventos aún");
        elif (self.totalPosI==None):
            messagebox.showerror("Error", "No han creado eventos aún");
        else:
            messagebox.showinfo("Información", "No hay más eventos antes de este");

    def sgtEventIU(self):
        if(self.posIU8<=self.compruebaSgtEventI()):
            self.posIU0+=8; self.posIU1+=8; self.posIU2+=8; self.posIU3+=8;
            self.posIU4+=8; self.posIU5+=8; self.posIU6+=8; self.posIU7+=8;
            self.posIU8+=8;
            self.myCodeEIUV.set(Bd.devuelveEvents(self.posIU0));
            self.myTitulIUV.set(Bd.devuelveEvents(self.posIU1));
            self.myDescripIUV.set(Bd.devuelveEvents(self.posIU2));
            self.myLugarIUV.set(Bd.devuelveEvents(self.posIU3));
            self.myFechaIUV.set(Bd.devuelveEvents(self.posIU4));
            self.myHoraIUV.set(Bd.devuelveEvents(self.posIU5));
            self.myBoletoIUV.set(Bd.devuelveEvents(self.posIU6));
            self.myCodeAIUV.set(Bd.daNameAdminByCode(Bd.devuelveEvents(self.posIU7)));
        elif(Bd.daFinalCodeEventCount()==None):
            messagebox.showerror("Error", "No se han creado eventos aún");
        elif (Bd.daFinalCodeEventCount()==0):
            messagebox.showerror("Error", "No se han creado eventos aún");
        else:
            messagebox.showinfo("Información", "No hay más eventos creados");

    def antesEventIU(self):
        self.totalPosI=(Bd.daFinalCodeEventCount()*8);
        if(self.posIU0>0):
            self.posIU0-=8; self.posIU1-=8; self.posIU2-=8; self.posIU3-=8;
            self.posIU4-=8; self.posIU5-=8; self.posIU6-=8; self.posIU7-=8;
            self.posIU8-=8;
            self.myCodeEIUV.set(Bd.devuelveEvents(self.posIU0));
            self.myTitulIUV.set(Bd.devuelveEvents(self.posIU1));
            self.myDescripIUV.set(Bd.devuelveEvents(self.posIU2));
            self.myLugarIUV.set(Bd.devuelveEvents(self.posIU3));
            self.myFechaIUV.set(Bd.devuelveEvents(self.posIU4));
            self.myHoraIUV.set(Bd.devuelveEvents(self.posIU5));
            self.myBoletoIUV.set(Bd.devuelveEvents(self.posIU6));
            self.myCodeAIUV.set(Bd.daNameAdminByCode(Bd.devuelveEvents(self.posIU7)));
        elif (self.totalPosI==0):
            messagebox.showerror("Error", "No han creado eventos aún");
        elif (self.totalPosI==None):
            messagebox.showerror("Error", "No han creado eventos aún");
        else:
            messagebox.showinfo("Información", "No hay más eventos antes de este");

    def sgtEventMU(self, tempCodeUser):
        if(self.codeMU9<self.compruebaSgtEventCodeM(tempCodeUser)):
            self.codeMU9+=1;
            self.myCodeEMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU0));
            self.myTitulMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU1));
            self.myDescripMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU2));
            self.myLugarMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU3));
            self.myFechaMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU4));
            self.myHoraMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU5));
            self.myBoletoMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU6));
            self.myCodeAMUV.set(Bd.daNameAdminByCode(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU7)));
        elif(Bd.daFinalCodeEventByUser(tempCodeUser)==None):
            messagebox.showerror("Error", "No te has enlistado en eventos aún");
        elif (Bd.daFinalCodeEventByUser(tempCodeUser)==0):
            messagebox.showerror("Error", "No te has enlistado en eventos aún");
        else:
            messagebox.showinfo("Información", "No hay más eventos en los que te hayas enlistado");

    def antesEventMU(self, tempCodeUser):
        if(self.codeMU9>0):
            self.codeMU9-=1;
            self.myCodeEMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU0));
            self.myTitulMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU1));
            self.myDescripMUV.set(
                Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU2));
            self.myLugarMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU3));
            self.myFechaMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU4));
            self.myHoraMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU5));
            self.myBoletoMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU6));
            self.myCodeAMUV.set(Bd.daNameAdminByCode(
                Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, self.codeMU9), self.posMU7)));
        elif (Bd.daFinalCodeEventByUser(tempCodeUser)==None):
            messagebox.showerror("Error", "No te has enlistado en eventos aún");
        elif (Bd.daFinalCodeEventByUser(tempCodeUser)==0):
            messagebox.showerror("Error", "No te has enlistado en eventos aún");
        else:
            messagebox.showinfo("Información", "No hay más eventos en los que te enlistaste");

    def limpiaEditar(self):
        self.ceduVE.set("");
        self.nomVE.set("");
        self.apeVE.set("");
        self.fechaVE.set("");
        self.userVE.set("");
        self.telfVE.set("");
        self.mailVE.set("");
        self.pass1VE.set("");

    def limpiaEditarA(self):
        self.ceduVEA.set("");
        self.nomVEA.set("");
        self.apeVEA.set("");
        self.fechaVEA.set("");
        self.userVEA.set("");
        self.telfVEA.set("");
        self.mailVEA.set("");
        self.pass1VEA.set("");

    def limpiaLogin(self):
        self.logPersonV.set("");
        self.logPassV.set("");

    def muestraDatosUser(self, tempCodeUser):
        self.saludoPV.set(Bd.daUnDatoUser(tempCodeUser, 2));
        self.labelCodeVM.set(Bd.daUnDatoUser(tempCodeUser, 0));
        self.ceduVM.set(Bd.daUnDatoUser(tempCodeUser, 1));
        self.nomVM.set(Bd.daUnDatoUser(tempCodeUser, 2));
        self.apeVM.set(Bd.daUnDatoUser(tempCodeUser, 3));
        self.fechaVM.set(Bd.daUnDatoUser(tempCodeUser, 4));
        self.userVM.set(Bd.daUnDatoUser(tempCodeUser, 5));
        self.telfVM.set(Bd.daUnDatoUser(tempCodeUser, 6));
        self.mailVM.set(Bd.daUnDatoUser(tempCodeUser, 7));
        self.pass1VM.set(Bd.daUnDatoUser(tempCodeUser, 8));

    def muestraDatosAdmi(self, tempCodeAdmi):
        self.saludoPVA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 2));
        self.labelCodeVMA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 0));
        self.ceduVMA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 1));
        self.nomVMA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 2));
        self.apeVMA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 3));
        self.fechaVMA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 4));
        self.userVMA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 5));
        self.telfVMA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 6));
        self.mailVMA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 7));
        self.pass1VMA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 8));

    def insertaCodigoEntryReg(self):
        if (self.radioV.get() == 1):
            self.setCode=(Bd.extraeFor(Bd.daFinalCodeUser())+1);
            self.regCodeV.set(self.setCode);
            self.entryRegCodi.config(justify=RIGHT);
        elif (self.radioV.get() == 2):
            self.regCodeV.set("");
            self.entryRegCodi.config(justify=LEFT);

    def cambiaFrame(self, frame):
        frame.pack_forget();

    def returnVentana(self, ventana):
        ventana.deiconify();

    def destroyVentana(self, ventana):
        ventana.destroy();

    def hideVentana(self, ventana):
        ventana.withdraw();

    def fFrameMyEventoB(self, frameRoot, posx, posy, myCodeEV, myCodeAV,
                        myTitulV, myDescrip, myLugarV,
                        myFechaV, myHoraV, myBoletoV):
        #Frame
        self.framePrincipal=Frame(frameRoot, height='400', width='600', bg=self.colorFrameTitle, bd=5, relief='raised');
        self.framePrincipal.place(x=posx, y=posy);
        #Labels
        self.labelMyTitu=Label(self.framePrincipal, textvariable=myTitulV, fg=self.colorFgW, bg=self.colorFrameTitle,
                                    font=("Tw Cen MT Condensed Extra Bold", 26));
        self.labelMyTitu.place(x=45, y=10);
        self.labelMyCodeM = Label(self.framePrincipal, text="Codigo:", fg=self.colorFgW,
                                  bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyCodeM.place(x=45, y=80);
        self.labelMyCodeV=Label(self.framePrincipal, textvariable=myCodeEV, fg=self.colorFgW,
                                bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyCodeV.place(x=135, y=80);
        self.labelMyAdmiCodeM=Label(self.framePrincipal, text="Admin:", fg=self.colorFgW,
                                  bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyAdmiCodeM.place(x=190, y=80);
        self.labelMyAdmiCodeV = Label(self.framePrincipal, textvariable=myCodeAV, fg=self.colorFgW,
                                      bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyAdmiCodeV.place(x=270, y=80);
        self.labelMyAdmiCodeM = Label(self.framePrincipal, text="Boletos:", fg=self.colorFgW,
                                      bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyAdmiCodeM.place(x=385, y=80);
        self.labelMyAdmiCodeV = Label(self.framePrincipal, textvariable=myBoletoV, fg=self.colorFgW,
                                      bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyAdmiCodeV.place(x=490, y=80);
        self.labelMyLugarM = Label(self.framePrincipal, text="Lugar:", fg=self.colorFgW,
                                      bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyLugarM.place(x=45, y=110);
        self.labelMyLugarV = Label(self.framePrincipal, textvariable=myLugarV, fg=self.colorFgW,
                                      bg=self.colorFrameTitle, font=(self.fontCali, 14));
        self.labelMyLugarV.place(x=125, y=110);
        self.labelMyFechaM = Label(self.framePrincipal, text="Fecha:", fg=self.colorFgW,
                                      bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyFechaM.place(x=45, y=140);
        self.labelMyFechaV = Label(self.framePrincipal, textvariable=myFechaV, fg=self.colorFgW,
                                      bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyFechaV.place(x=125, y=140);
        self.labelMyHoraM = Label(self.framePrincipal, text="Hora:", fg=self.colorFgW,
                                   bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyHoraM.place(x=370, y=140);
        self.labelMyHoraV = Label(self.framePrincipal, textvariable=myHoraV, fg=self.colorFgW,
                                   bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyHoraV.place(x=435, y=140);
        self.labelMyDescripM = Label(self.framePrincipal, text="Descripción:", fg=self.colorFgW,
                                  bg=self.colorFrameTitle, font=(self.fontOCR, 16));
        self.labelMyDescripM.place(x=45, y=180);
        #Message para mostrar
        self.textMyDescrip=Message(self.framePrincipal, font=(self.fontCali, 12), relief='groove',
                                  bg=self.colorFrameTitle, fg=self.colorFgW, width=500,
                                   textvariable=myDescrip);
        self.textMyDescrip.place(x=45, y=210);
        # flat, groove, raised, ridge, solid, or sunken

    def fFrameMyEventU(self, Root, tempCodeUser):
        #Frame
        self.frameDatosEU=Frame(Root, height='800', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameDatosEU.pack(fill='x');
        #Variables
        self.myCodeEMUV=StringVar();
        self.myCodeAMUV=StringVar();
        self.myTitulMUV=StringVar();
        self.myDescripMUV=StringVar();
        self.myLugarMUV=StringVar();
        self.myFechaMUV=StringVar();
        self.myHoraMUV=StringVar();
        self.myBoletoMUV=StringVar();
        # Control
        self.posMU0=0; self.posMU1=1; self.posMU2=2;
        self.posMU3=3; self.posMU4=4; self.posMU5=5;
        self.posMU6=6; self.posMU7=7; self.posMU8=16;
        self.codeMU9=0;
        #Muestra evento
        if(Bd.validaEnlistaNull(tempCodeUser)==True):
            self.myCodeEMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, 0), self.posMU0));
            self.myTitulMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, 0), self.posMU1));
            self.myDescripMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, 0), self.posMU2));
            self.myLugarMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, 0), self.posMU3));
            self.myFechaMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, 0), self.posMU4));
            self.myHoraMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, 0), self.posMU5));
            self.myBoletoMUV.set(Bd.daUnDatoEventByCode(Bd.daCodeUserEnlista(tempCodeUser, 0), self.posMU6));
            self.myCodeAMUV.set(Bd.daNameAdminByCode(Bd.devuelveEvents(self.posMU7)));
        else:
            self.myCodeEMUV.set("XXXXX");
            self.myTitulMUV.set("No hay título del evento aún");
            self.myDescripMUV.set("No hay descripción porque ningún administrador ha creado un evento");
            self.myLugarMUV.set("Aquí el lugar donde se realizará pero aún no hay eventos");
            self.myFechaMUV.set("dd/mm/yyyy");
            self.myHoraMUV.set("02:00 AM");
            self.myBoletoMUV.set("100000");
            self.myCodeAMUV.set("Admin");
        #Enlaza frames
        self.fFrameMyEventoB(self.frameDatosEU, 350, 60, self.myCodeEMUV, self.myCodeAMUV,
                             self.myTitulMUV, self.myDescripMUV, self.myLugarMUV,
                             self.myFechaMUV, self.myHoraMUV, self.myBoletoMUV);
        #Labels
        self.tituloDatosEventMU=Label(self.frameDatosEU, text="GESTIONA TU EVENTO", fg=self.colorFgW,
                                    bg=self.colorFrameTitle, font=("Tw Cen MT Condensed Extra Bold", 20));
        # Coloca Labels
        self.tituloDatosEventMU.place(x=10, y=10);

        #Botones
        self.botonNextEventMU=Button(self.frameDatosEU, text="Siguiente", font=(self.fontOCR, 14),
                                   fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                   cursor=self.cursorBot, height=2, width=9,
                                   command=lambda:[self.sgtEventMU(tempCodeUser)]);
        self.botonLastEventMU=Button(self.frameDatosEU, text="Anterior", font=(self.fontOCR, 14),
                                   fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                   cursor=self.cursorBot, height=2, width=9,
                                   command=lambda:[self.antesEventMU(tempCodeUser)]);
        self.botonOutEvent=Button(self.frameDatosEU, text="Salirse", font=(self.fontOCR, 14),
                                       fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                       cursor=self.cursorBot, height=2, width=9,
                                       command=lambda: [messagebox.showerror("Error al salir de evento", "No puedes dejar este evento antes de que empiece")]);
        #Coloca Botones
        self.botonNextEventMU.place(x=960, y=260);
        self.botonLastEventMU.place(x=230, y=260);
        self.botonOutEvent.place(x=580, y=470);

    def fFrameMyEventA(self, Root, tempCodeAdmi):
        #Frame
        self.frameDatosE=Frame(Root, height='800', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameDatosE.pack(fill='x');
        #Variables
        self.myCodeEV = StringVar();
        self.myCodeAV = StringVar();
        self.myTitulV = StringVar();
        self.myDescripV = StringVar();
        self.myLugarV = StringVar();
        self.myFechaV = StringVar();
        self.myHoraV = StringVar();
        self.myBoletoV = StringVar();
        #Muestra evento
        if(Bd.validaEventNull(tempCodeAdmi)==True):
            self.myCodeEV.set(Bd.daUnDatoEvent(tempCodeAdmi, 0));
            self.myTitulV.set(Bd.daUnDatoEvent(tempCodeAdmi, 1));
            self.myDescripV.set(Bd.daUnDatoEvent(tempCodeAdmi, 2));
            self.myLugarV.set(Bd.daUnDatoEvent(tempCodeAdmi, 3));
            self.myFechaV.set(Bd.daUnDatoEvent(tempCodeAdmi, 4));
            self.myHoraV.set(Bd.daUnDatoEvent(tempCodeAdmi, 5));
            self.myBoletoV.set(Bd.daUnDatoEvent(tempCodeAdmi, 6));
            self.myCodeAV.set(Bd.daUnDatoEvent(tempCodeAdmi, 7));
        else:
            self.myCodeEV.set("XXXXX");
            self.myTitulV.set("Aquí va el título de tu evento creado");
            self.myDescripV.set("Aquí va una descripción de tu evento");
            self.myLugarV.set("Aquí el lugar donde se realizará");
            self.myFechaV.set("dd/mm/yyyy");
            self.myHoraV.set("02:00 AM");
            self.myBoletoV.set("100000");
            self.myCodeAV.set(tempCodeAdmi);
        #Control
        self.validarInTen=self.frameDatosE.register(self.validaCedulaIn);
        self.validarInFechaEventE=self.frameDatosE.register(self.validaFechaIn);
        self.tuplaHoraE=("09:30 AM", "10:00 AM", "10:30 AM", "11:00 AM",
                         "11:30 AM", "12:00 PM", "12:30 PM", "13:00 PM",
                         "13:30 PM", "14:00 PM", "14:30 PM", "15:00 PM",
                         "15:30 PM", "16:00 PM", "16:30 PM", "17:00 PM");
        self.pos0=0; self.pos1=1; self.pos2=2; self.pos3=3; self.pos4=4; self.pos5=5;
        self.pos6=6; self.pos7=7; self.pos8=16;
        #Enlaza frames
        self.fFrameMyEventoB(self.frameDatosE, 145, 80, self.myCodeEV, self.myCodeAV,
                             self.myTitulV, self.myDescripV, self.myLugarV,
                             self.myFechaV, self.myHoraV, self.myBoletoV);
        #Labels
        self.tituloDatosEvent=Label(self.frameDatosE, text="GESTIONA TU EVENTO", fg=self.colorFgW,
                                    bg=self.colorFrameTitle, font=("Tw Cen MT Condensed Extra Bold", 20));
        self.labelEventTituE=Label(self.frameDatosE, text="EDITA TU EVENTO", fg=self.colorFgW, bg=self.colorFrameTitle,
                                    font=("Tw Cen MT Condensed Extra Bold", 20));
        self.labelEventCodeE=Label(self.frameDatosE, text="Código:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                    font=(self.fontOCR, 18));
        self.labelEventCodeEM=Label(self.frameDatosE, textvariable=self.myCodeEV, fg=self.colorFgW,
                                     bg=self.colorFrameTitle, font=(self.fontOCR, 18));
        self.labelEventNomE=Label(self.frameDatosE, text="Título:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                   font=(self.fontOCR, 14));
        self.labelEventDescripE=Label(self.frameDatosE, text="Descripción:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                       font=(self.fontOCR, 14));
        self.labelEventLugarE=Label(self.frameDatosE, text="Lugar:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                     font=(self.fontOCR, 14));
        self.labelEventFechaE=Label(self.frameDatosE, text="Fecha:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                     font=(self.fontOCR, 14));
        self.labelEventHoraE=Label(self.frameDatosE, text="Hora:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                    font=(self.fontOCR, 14));
        self.labelEventBoleE=Label(self.frameDatosE, text="Boletos:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                    font=(self.fontOCR, 14));
        self.labelEventCodeAdmiEM=Label(self.frameDatosE, text="Admin:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                         font=(self.fontOCR, 14));
        self.labelEventCodeAdmiVE=Label(self.frameDatosE, textvariable=self.myCodeAV, fg=self.colorFgW,
                                        bg=self.colorFrameTitle, font=(self.fontOCR, 14));
        # Coloca Labels
        self.tituloDatosEvent.place(x=10, y=10);
        self.labelEventTituE.place(x=880, y=10);
        self.labelEventCodeE.place(x=910, y=80);
        self.labelEventCodeEM.place(x=1015, y=80);
        self.labelEventNomE.place(x=910, y=120);
        self.labelEventDescripE.place(x=910, y=160);
        self.labelEventLugarE.place(x=910, y=295);
        self.labelEventFechaE.place(x=910, y=365);
        self.labelEventHoraE.place(x=1145, y=365);
        self.labelEventBoleE.place(x=910, y=410);
        self.labelEventCodeAdmiEM.place(x=1145, y=410);
        self.labelEventCodeAdmiVE.place(x=1215, y=410);
        #Entrys
        self.entryEventNomE=Entry(self.frameDatosE, font=(self.fontCali, 14), textvariable=self.myTitulV);
        #Text para la descripción
        self.textEventDescripE=Text(self.frameDatosE, font=(self.fontCali, 12));
        #self.myDescripV.set(self.textEventDescripE.get(1.0, END));
        #Entrys
        self.entryEventLugarE=Entry(self.frameDatosE, font=(self.fontCali, 12), textvariable=self.myLugarV);
        self.entryEventFechaE=Entry(self.frameDatosE, font=(self.fontCali, 14), textvariable=self.myFechaV,
                                     validate="key", validatecommand=(self.validarInFechaEventE, "%d", "%S", "%s"));
        #Coloca Entrys
        self.entryEventNomE.place(x=990, y=120, width=320);
        self.textEventDescripE.place(x=910, y=185, width=400, height=100);
        self.entryEventLugarE.place(x=910, y=320, width=400);
        self.entryEventFechaE.place(x=985, y=365, width=120);
        #SpinBoxes
        self.spinEventHoraE=Spinbox(self.frameDatosE, font=(self.fontCali, 14), textvariable=self.myHoraV,
                                     values=self.tuplaHoraE, state='readonly');
        self.spinEventBoleE= Spinbox(self.frameDatosE, font=(self.fontCali, 14), textvariable=self.myBoletoV,
                                     from_=1, to=9999, validate="key", validatecommand=(self.validarInTen, "%S"));
        #Coloca SpinBoxes
        self.spinEventHoraE.place(x=1205, y=365, width=105);
        self.spinEventBoleE.place(x=1005, y=410, width=100);
        #Botones
        self.botonCreaEvent=Button(self.frameDatosE, text="Crear", font=(self.fontOCR, 14),
                                   fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                   cursor=self.cursorBot, height=2, width=9, command=lambda:[self.ventEvento(Root, tempCodeAdmi)]);
        self.botonNextEvent=Button(self.frameDatosE, text="Siguiente", font=(self.fontOCR, 14),
                                   fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                   cursor=self.cursorBot, height=2, width=9,
                                   command=lambda:[self.sgtEvent(tempCodeAdmi)]);
        self.botonLastEvent=Button(self.frameDatosE, text="Anterior", font=(self.fontOCR, 14),
                                   fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                   cursor=self.cursorBot, height=2, width=9,
                                   command=lambda:[self.antesEvent(tempCodeAdmi)]);
        self.botonEditaEvent=Button(self.frameDatosE, text="Edita", font=(self.fontOCR, 14),
                                     fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                     cursor=self.cursorBot, height=2, width=9,
                                     command=lambda:[self.validacionEdicionEvent(tempCodeAdmi, self.textEventDescripE),
                                                     self.actualizaEditaEvent()]);
        self.botonBorraEvent = Button(self.frameDatosE, text="Borrar", font=(self.fontOCR, 14),
                                     fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                     cursor=self.cursorBot, height=2, width=9,
                                     command=lambda: [messagebox.showerror("Error de Borrado", "No puedes simplemente borrar este evento, hay usuarios enlistados")]);
        #Coloca Botones
        self.botonCreaEvent.place(x=30, y=80);
        self.botonNextEvent.place(x=750, y=260);
        self.botonLastEvent.place(x=30, y=260);
        self.botonEditaEvent.place(x=1070, y=460);
        self.botonBorraEvent.place(x=750, y=80);

    def fFrameDatosU(self, Root, tempCodeUser):
        #Variables de control
        self.labelCodeVM=StringVar();
        self.ceduVM=StringVar();
        self.nomVM = StringVar();
        self.apeVM = StringVar();
        self.fechaVM = StringVar();
        self.userVM = StringVar();
        self.telfVM = StringVar();
        self.mailVM = StringVar();
        self.pass1VM = StringVar();
        self.ceduVE = StringVar();
        self.nomVE=StringVar();
        self.apeVE=StringVar();
        self.fechaVE=StringVar();
        self.userVE=StringVar();
        self.telfVE=StringVar();
        self.mailVE=StringVar();
        self.pass1VE=StringVar();
        #Control
        self.validarInCeduE=Root.register(self.validaCedulaIn);
        self.validarInFechaE=Root.register(self.validaFechaIn);
        #Frame
        self.frameDatos=Frame(Root, height='800', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameDatos.pack(fill='x');
        #Labels
        self.tituloDatos=Label(self.frameDatos, text="INFORMACIÓN DE USUARIO", fg=self.colorFgW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 20));
        self.tituloDatosE=Label(self.frameDatos, text="EDITA TUS DATOS", fg=self.colorFgW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 20));
        self.codigoDatosA=Label(self.frameDatos, text="Código: ", fg=self.colorFgW, bg=self.colorFrameTitle,
                                  font=(self.fontOCR, 18));
        self.codigoDatosB=Label(self.frameDatos, textvariable=self.labelCodeVM, fg=self.colorFgW, bg=self.colorFrameTitle,
                                  font=(self.fontCali, 18));
        self.cedulaDatosM=Label(self.frameDatos, text="Cédula:", fg=self.colorFgW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 14));
        self.cedulaDatosE=Label(self.frameDatos, text="Cédula:", fg=self.colorFgW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 14));
        self.nombreDatosM=Label(self.frameDatos, text="Nombre:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                 font=(self.fontOCR, 14));
        self.nombreDatosE=Label(self.frameDatos, text="Nombre:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                 font=(self.fontOCR, 14));
        self.apellidoDatosM=Label(self.frameDatos, text="Apellido:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                   font=(self.fontOCR, 14));
        self.apellidoDatosE=Label(self.frameDatos, text="Apellido:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                   font=(self.fontOCR, 14));
        self.fechaDatosM=Label(self.frameDatos, text="Fecha Nacim.:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                font=(self.fontOCR, 14));
        self.fechaDatosE=Label(self.frameDatos, text="Fecha Nacim.:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                font=(self.fontOCR, 14));
        self.userDatosM=Label(self.frameDatos, text="Nick:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.userDatosE=Label(self.frameDatos, text="Nick:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.telfDatosM=Label(self.frameDatos, text="Teléfono:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.telfDatosE=Label(self.frameDatos, text="Teléfono:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.mailDatosM=Label(self.frameDatos, text="Email:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.mailDatosE=Label(self.frameDatos, text="Email:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.passDatosM=Label(self.frameDatos, text="Contraseña:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.passDatosE=Label(self.frameDatos, text="Contraseña:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        # Coloca Labels
        self.tituloDatos.place(x=20, y=10);
        self.tituloDatosE.place(x=700, y=10);
        self.codigoDatosA.place(x=40, y=60);
        self.codigoDatosB.place(x=150, y=60);
        self.cedulaDatosM.place(x=60, y=120);
        self.cedulaDatosE.place(x=750, y=120);
        self.nombreDatosM.place(x=60, y=160);
        self.nombreDatosE.place(x=750, y=160);
        self.apellidoDatosM.place(x=60, y=200);
        self.apellidoDatosE.place(x=750, y=200);
        self.fechaDatosM.place(x=60, y=240);
        self.fechaDatosE.place(x=750, y=240);
        self.telfDatosM.place(x=60, y=280);
        self.telfDatosE.place(x=750, y=280);
        self.mailDatosM.place(x=60, y=320);
        self.mailDatosE.place(x=750, y=320);
        self.userDatosM.place(x=60, y=360);
        self.userDatosE.place(x=750, y=360);
        self.passDatosM.place(x=60, y=400);
        self.passDatosE.place(x=750, y=400);
        #Entrys
        self.entryCeduE = Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.ceduVE,
                                validate="key", validatecommand=(self.validarInCeduE, "%S"),
                                foreground=self.colorCorp);
        self.ceduVE.trace("w", lambda *args: self.limitadorCedula(self.ceduVE));
        self.entryNomE = Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.nomVE,
                               foreground=self.colorCorp);
        self.entryApeE = Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.apeVE,
                               foreground=self.colorCorp);
        self.entryFNacimE = Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.fechaVE,
                                  validate="key", validatecommand=(self.validarInFechaE, "%d", "%S", "%s"),
                                  foreground=self.colorCorp);
        self.entryTelfE = Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.telfVE,
                                validate="key", validatecommand=(self.validarInCeduE, "%S"),
                                foreground=self.colorCorp);
        self.telfVE.trace("w", lambda *args: self.limitadorCedula(self.telfVE));
        self.entryMailE = Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.mailVE,
                                foreground=self.colorCorp);
        self.entryNickE=Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.userVE,
                                foreground=self.colorCorp);
        self.entryPassE = Entry(self.frameDatos, show="*", font=(self.fontCali, 14), textvariable=self.pass1VE,
                                foreground=self.colorCorp);
        #Botone Edición
        self.botonEditaU = Button(self.frameDatos, text="Editar", font=(self.fontOCR, 12),
                                  fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                  cursor=self.cursorBot, height=2, width=9,
                                  command=lambda: [self.validacionEdicionUser(tempCodeUser), self.limpiaEditar(),
                                                   self.muestraDatosUser(tempCodeUser)]);
        self.botonEditaU.place(x=850, y=450);
        self.botonEliminaU=Button(self.frameDatos, text="Eliminar\nmi Cuenta", font=(self.fontOCR, 12),
                                  fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                  cursor=self.cursorBot, height=2, width=9,
                                  command=lambda:[messagebox.showerror("Error al borrar", "No se puede borrar esta cuenta")]);
        self.botonEliminaU.place(x=1200, y=450);
        #Entrys que muestran
        self.entryCeduM=Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.ceduVM,
                             validate="key", validatecommand=(self.validarInCeduE, "%S"),
                             foreground=self.colorCorp, state='readonly');
        self.entryNomM=Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.nomVM,
                              foreground=self.colorCorp, state='readonly');
        self.entryApeM=Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.apeVM,
                             foreground=self.colorCorp, state='readonly');
        self.entryFNacimM=Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.fechaVM,
                                validate="key", validatecommand=(self.validarInFechaE, "%d", "%S", "%s"),
                                foreground=self.colorCorp, state='readonly');
        self.entryNickM=Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.userVM,
                              foreground=self.colorCorp, state='readonly');
        self.entryTelfM=Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.telfVM,
                              validate="key", validatecommand=(self.validarInCeduE, "%S"),
                              foreground=self.colorCorp, state='readonly');
        self.entryMailM=Entry(self.frameDatos, font=(self.fontCali, 14), textvariable=self.mailVM,
                              foreground=self.colorCorp, state='readonly');
        self.entryPassM=Entry(self.frameDatos, show="*", font=(self.fontCali, 14), textvariable=self.pass1VM,
                              foreground=self.colorCorp, state='readonly');
        #Inserta Entrys
        self.entryCeduM.place(x=210, y=120, width=200);
        self.entryNomM.place(x=210, y=160, width=200);
        self.entryApeM.place(x=210, y=200, width=200);
        self.entryFNacimM.place(x=210, y=240, width=200);
        self.entryNickM.place(x=210, y=360, width=200);
        self.entryTelfM.place(x=210, y=280, width=200);
        self.entryMailM.place(x=210, y=320, width=200);
        self.entryPassM.place(x=210, y=400, width=200);
        self.entryCeduE.place(x=900, y=120, width=200);
        self.entryNomE.place(x=900, y=160, width=200);
        self.entryApeE.place(x=900, y=200, width=200);
        self.entryFNacimE.place(x=900, y=240, width=200);
        self.entryTelfE.place(x=900, y=280, width=200);
        self.entryMailE.place(x=900, y=320, width=200);
        self.entryNickE.place(x=900, y=360, width=200);
        self.entryPassE.place(x=900, y=400, width=200);

    def fFrameDatosA(self, Root, tempCodeAdmi):
        #Variables de control
        self.labelCodeVMA=StringVar();
        self.ceduVMA=StringVar();
        self.nomVMA=StringVar();
        self.apeVMA=StringVar();
        self.fechaVMA=StringVar();
        self.userVMA=StringVar();
        self.telfVMA=StringVar();
        self.mailVMA=StringVar();
        self.pass1VMA=StringVar();
        self.ceduVEA=StringVar();
        self.nomVEA=StringVar();
        self.apeVEA=StringVar();
        self.fechaVEA=StringVar();
        self.userVEA=StringVar();
        self.telfVEA=StringVar();
        self.mailVEA=StringVar();
        self.pass1VEA=StringVar();
        #Control
        self.validarInCeduEA=Root.register(self.validaCedulaIn);
        self.validarInFechaEA=Root.register(self.validaFechaIn);
        #Frame
        self.frameDatosA=Frame(Root, height='800', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameDatosA.pack(fill='x');
        #Labels
        self.tituloDatosA=Label(self.frameDatosA, text="INFORMACIÓN DE USUARIO", fg=self.colorFgW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 20));
        self.tituloDatosEA=Label(self.frameDatosA, text="EDITA TUS DATOS", fg=self.colorFgW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 20));
        self.codigoDatosAA=Label(self.frameDatosA, text="Código: ", fg=self.colorFgW, bg=self.colorFrameTitle,
                                  font=(self.fontOCR, 18));
        self.codigoDatosBA=Label(self.frameDatosA, textvariable=self.labelCodeVMA, fg=self.colorFgW, bg=self.colorFrameTitle,
                                  font=(self.fontCali, 18));
        self.cedulaDatosMA=Label(self.frameDatosA, text="Cédula:", fg=self.colorFgW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 14));
        self.cedulaDatosEA=Label(self.frameDatosA, text="Cédula:", fg=self.colorFgW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 14));
        self.nombreDatosMA=Label(self.frameDatosA, text="Nombre:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                 font=(self.fontOCR, 14));
        self.nombreDatosEA=Label(self.frameDatosA, text="Nombre:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                 font=(self.fontOCR, 14));
        self.apellidoDatosMA=Label(self.frameDatosA, text="Apellido:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                   font=(self.fontOCR, 14));
        self.apellidoDatosEA=Label(self.frameDatosA, text="Apellido:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                   font=(self.fontOCR, 14));
        self.fechaDatosMA=Label(self.frameDatosA, text="Fecha Nacim.:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                font=(self.fontOCR, 14));
        self.fechaDatosEA=Label(self.frameDatosA, text="Fecha Nacim.:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                font=(self.fontOCR, 14));
        self.userDatosMA=Label(self.frameDatosA, text="Nick:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.userDatosEA=Label(self.frameDatosA, text="Nick:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.telfDatosMA=Label(self.frameDatosA, text="Teléfono:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.telfDatosEA=Label(self.frameDatosA, text="Teléfono:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.mailDatosMA=Label(self.frameDatosA, text="Email:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.mailDatosEA=Label(self.frameDatosA, text="Email:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.passDatosMA=Label(self.frameDatosA, text="Contraseña:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.passDatosEA=Label(self.frameDatosA, text="Contraseña:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        # Coloca Labels
        self.tituloDatosA.place(x=20, y=10);
        self.tituloDatosEA.place(x=700, y=10);
        self.codigoDatosAA.place(x=40, y=60);
        self.codigoDatosBA.place(x=150, y=60);
        self.cedulaDatosMA.place(x=60, y=120);
        self.cedulaDatosEA.place(x=750, y=120);
        self.nombreDatosMA.place(x=60, y=160);
        self.nombreDatosEA.place(x=750, y=160);
        self.apellidoDatosMA.place(x=60, y=200);
        self.apellidoDatosEA.place(x=750, y=200);
        self.fechaDatosMA.place(x=60, y=240);
        self.fechaDatosEA.place(x=750, y=240);
        self.telfDatosMA.place(x=60, y=280);
        self.telfDatosEA.place(x=750, y=280);
        self.mailDatosMA.place(x=60, y=320);
        self.mailDatosEA.place(x=750, y=320);
        self.userDatosMA.place(x=60, y=360);
        self.userDatosEA.place(x=750, y=360);
        self.passDatosMA.place(x=60, y=400);
        self.passDatosEA.place(x=750, y=400);
        #Entrys
        self.entryCeduEA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.ceduVEA,
                                validate="key", validatecommand=(self.validarInCeduEA, "%S"),
                                foreground=self.colorCorp);
        self.ceduVEA.trace("w", lambda *args: self.limitadorCedula(self.ceduVEA));
        self.entryNomEA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.nomVEA,
                               foreground=self.colorCorp);
        self.entryApeEA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.apeVEA,
                               foreground=self.colorCorp);
        self.entryFNacimEA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.fechaVEA,
                                  validate="key", validatecommand=(self.validarInFechaEA, "%d", "%S", "%s"),
                                  foreground=self.colorCorp);
        self.entryTelfEA = Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.telfVEA,
                                validate="key", validatecommand=(self.validarInCeduEA, "%S"),
                                foreground=self.colorCorp);
        self.telfVEA.trace("w", lambda *args: self.limitadorCedula(self.telfVEA));
        self.entryMailEA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.mailVEA,
                                foreground=self.colorCorp);
        self.entryNickEA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.userVEA,
                                foreground=self.colorCorp);
        self.entryPassEA=Entry(self.frameDatosA, show="*", font=(self.fontCali, 14), textvariable=self.pass1VEA,
                                foreground=self.colorCorp);
        #Botone Edición
        self.botonEditaA=Button(self.frameDatosA, text="Editar", font=(self.fontOCR, 12),
                                  fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                  cursor=self.cursorBot, height=2, width=9,
                                  command=lambda: [self.validacionEdicionAdmi(tempCodeAdmi), self.limpiaEditarA(),
                                                   self.muestraDatosAdmi(tempCodeAdmi)]);
        self.botonEditaA.place(x=850, y=450);
        #Entrys que muestran
        self.entryCeduMA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.ceduVMA,
                             validate="key", validatecommand=(self.validarInCeduEA, "%S"),
                             foreground=self.colorCorp, state='readonly');
        self.entryNomMA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.nomVMA,
                              foreground=self.colorCorp, state='readonly');
        self.entryApeMA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.apeVMA,
                             foreground=self.colorCorp, state='readonly');
        self.entryFNacimMA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.fechaVMA,
                                validate="key", validatecommand=(self.validarInFechaEA, "%d", "%S", "%s"),
                                foreground=self.colorCorp, state='readonly');
        self.entryNickMA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.userVMA,
                              foreground=self.colorCorp, state='readonly');
        self.entryTelfMA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.telfVMA,
                              validate="key", validatecommand=(self.validarInCeduEA, "%S"),
                              foreground=self.colorCorp, state='readonly');
        self.entryMailMA=Entry(self.frameDatosA, font=(self.fontCali, 14), textvariable=self.mailVMA,
                              foreground=self.colorCorp, state='readonly');
        self.entryPassMA=Entry(self.frameDatosA, show="*", font=(self.fontCali, 14), textvariable=self.pass1VMA,
                              foreground=self.colorCorp, state='readonly');
        #Inserta Entrys
        self.entryCeduMA.place(x=210, y=120, width=200);
        self.entryNomMA.place(x=210, y=160, width=200);
        self.entryApeMA.place(x=210, y=200, width=200);
        self.entryFNacimMA.place(x=210, y=240, width=200);
        self.entryNickMA.place(x=210, y=360, width=200);
        self.entryTelfMA.place(x=210, y=280, width=200);
        self.entryMailMA.place(x=210, y=320, width=200);
        self.entryPassMA.place(x=210, y=400, width=200);
        self.entryCeduEA.place(x=900, y=120, width=200);
        self.entryNomEA.place(x=900, y=160, width=200);
        self.entryApeEA.place(x=900, y=200, width=200);
        self.entryFNacimEA.place(x=900, y=240, width=200);
        self.entryTelfEA.place(x=900, y=280, width=200);
        self.entryMailEA.place(x=900, y=320, width=200);
        self.entryNickEA.place(x=900, y=360, width=200);
        self.entryPassEA.place(x=900, y=400, width=200);

    def ventEvento(self, ventana, tempCodeAdmi):
        self.ventInEvent = Toplevel(ventana);
        self.ventInEvent.grab_set();
        altoPantalla = self.ventInEvent.winfo_screenheight();
        anchoPantalla = self.ventInEvent.winfo_screenwidth();
        self.ventInEvent.title("Crear Evento");
        self.ventInEvent.config(bg=self.colorCorp);
        self.ventInEvent.geometry("380x600+{}+{}".format(int(anchoPantalla/3), int(altoPantalla/10)));
        self.ventInEvent.iconbitmap("Recursos\corpcitico.ico");
        self.ventInEvent.resizable(0, 0);
        #Variables de control
        self.eventCodeV=StringVar();
        self.eventCodeAdmiV=StringVar();
        self.eventNomV=StringVar();
        self.eventDescripV=StringVar();
        self.eventLugarV = StringVar();
        self.eventFechaV=StringVar();
        self.eventHoraV=StringVar();
        self.eventBoleV=StringVar();
        #Control
        self.eventCodeAdmiV.set(tempCodeAdmi);
        self.validarInTenE=self.ventInEvent.register(self.validaCedulaIn);
        self.validarInFechaEvent=self.ventInEvent.register(self.validaFechaIn);
        self.tuplaHora = ("09:30 AM", "10:00 AM", "10:30 AM", "11:00 AM",
                          "11:30 AM", "12:00 PM", "12:30 PM", "13:00 PM",
                          "13:30 PM", "14:00 PM", "14:30 PM", "15:00 PM",
                          "15:30 PM", "16:00 PM", "16:30 PM", "17:00 PM");
        if(Bd.extraeFor(Bd.daFinalCodeEvent())==None):
            self.eventCodeV.set(1);
        else:
            self.incrementCodeEvent=Bd.extraeFor(Bd.daFinalCodeEvent())+1;
            self.eventCodeV.set(self.incrementCodeEvent);
        #Labels
        self.labelEventTitu = Label(self.ventInEvent, text="CREEMOS UN EVENTO...", fg=self.colorFgW, bg=self.colorCorp,
                                  font=("Tw Cen MT Condensed Extra Bold", 26));
        self.labelEventTitu.place(x=20, y=10);
        self.labelEventCode=Label(self.ventInEvent, text="Código:", fg=self.colorFgW, bg=self.colorCorp,
                                  font=(self.fontOCR, 18));
        self.labelEventCode.place(x=40, y=80);
        self.labelEventCodeM=Label(self.ventInEvent, textvariable=self.eventCodeV, fg=self.colorFgW, bg=self.colorCorp,
                                   font=(self.fontOCR, 18));
        self.labelEventCodeM.place(x=145, y=80);
        self.labelEventNom=Label(self.ventInEvent, text="Título:", fg=self.colorFgW, bg=self.colorCorp,
                                    font=(self.fontOCR, 14));
        self.labelEventNom.place(x=40, y=120);
        self.labelEventDescrip=Label(self.ventInEvent, text="Descripción:", fg=self.colorFgW, bg=self.colorCorp,
                                   font=(self.fontOCR, 14));
        self.labelEventDescrip.place(x=40, y=180);
        self.labelEventLugar=Label(self.ventInEvent, text="Lugar:", fg=self.colorFgW, bg=self.colorCorp,
                                       font=(self.fontOCR, 14));
        self.labelEventLugar.place(x=40, y=320);
        self.labelEventFecha = Label(self.ventInEvent, text="Fecha:", fg=self.colorFgW, bg=self.colorCorp,
                                       font=(self.fontOCR, 14));
        self.labelEventFecha.place(x=40, y=380);
        self.labelEventHora=Label(self.ventInEvent, text="Hora:", fg=self.colorFgW, bg=self.colorCorp,
                                       font=(self.fontOCR, 14));
        self.labelEventHora.place(x=200, y=380);
        self.labelEventBole=Label(self.ventInEvent, text="Boletos:", fg=self.colorFgW, bg=self.colorCorp,
                                    font=(self.fontOCR, 14));
        self.labelEventBole.place(x=40, y=440);
        self.labelEventCodeAdmiM=Label(self.ventInEvent, text="Administrador", fg=self.colorFgW, bg=self.colorCorp,
                                     font=(self.fontOCR, 14));
        self.labelEventCodeAdmiM.place(x=200, y=440);
        self.labelEventCodeAdmiV= Label(self.ventInEvent, textvariable=self.eventCodeAdmiV, fg=self.colorFgW, bg=self.colorCorp,
                                         font=(self.fontOCR, 14));
        self.labelEventCodeAdmiV.place(x=200, y=465);
        #Entrys
        self.entryEventNom=Entry(self.ventInEvent, font=(self.fontCali, 14), textvariable=self.eventNomV);
        self.entryEventNom.place(x=40, y=145, width=300);
        #Text para la descripción
        self.textEventDescrip=Text(self.ventInEvent, font=(self.fontCali, 12));
        self.textEventDescrip.place(x=40, y=205, width=300, height=100);
        #Entrys
        self.entryEventLugar = Entry(self.ventInEvent, font=(self.fontCali, 12), textvariable=self.eventLugarV);
        self.entryEventLugar.place(x=40, y=345, width=300);
        self.entryEventFecha=Entry(self.ventInEvent, font=(self.fontCali, 14), textvariable=self.eventFechaV,
                                   validate="key", validatecommand=(self.validarInFechaEvent, "%d", "%S", "%s"));
        self.entryEventFecha.place(x=40, y=405, width=140);
        #SpinBoxes
        self.spinEventHora=Spinbox(self.ventInEvent,font=(self.fontCali, 14), textvariable=self.eventHoraV,
                                   values=self.tuplaHora, state='readonly');
        self.spinEventHora.place(x=200, y=405, width=140);
        self.spinEventBole=Spinbox(self.ventInEvent, font=(self.fontCali, 14), textvariable=self.eventBoleV,
                                   from_=1, to=9999, validate="key", validatecommand=(self.validarInTenE, "%S"));
        self.spinEventBole.place(x=40, y=465,width=140);
        #Botones
        self.botonAceptaEvent = Button(self.ventInEvent, text="Aceptar", font=(self.fontOCR, 14),
                                       fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                       cursor=self.cursorBot, height=2, width=9,
                                       command=lambda:[self.validacionEvent(tempCodeAdmi, self.textEventDescrip)]);
        self.botonAceptaEvent.place(x=60, y=520);
        self.botonCancelaEvent=Button(self.ventInEvent, text="Cancelar", font=(self.fontOCR, 14),
                                      fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                      cursor=self.cursorBot, height=2, width=9,
                                      command=lambda:[self.destroyVentana(self.ventInEvent),
                                                      self.decreceCodeEvent()]);
        self.botonCancelaEvent.place(x=210, y=520);

    def ventRegistro(self):
        # Variables de control
        self.regCeduV = StringVar();
        self.regCodeV = StringVar();
        self.regNomV = StringVar();
        self.regApeV = StringVar();
        self.regFechaV = StringVar();
        self.regUserV = StringVar();
        self.regTelfV = StringVar();
        self.regMailV = StringVar();
        self.regPass1V = StringVar();
        self.regPass2V = StringVar();
        self.radioV = IntVar();
        # Ventana de Registro
        self.ventRegisR = Toplevel(self.ventLoginR);
        self.ventRegisR.grab_set();
        self.ventLoginR.withdraw();
        altoPantalla = self.ventRegisR.winfo_screenheight();
        anchoPantalla = self.ventRegisR.winfo_screenwidth();
        self.ventRegisR.title("Ventana de Registro");
        self.ventRegisR.config(bg=self.colorCorp);
        self.ventRegisR.geometry("400x500+{}+{}".format(int(anchoPantalla / 3), int(altoPantalla / 5)));
        self.ventRegisR.iconbitmap("Recursos\corpcitico.ico");
        self.ventRegisR.resizable(0, 0);
        #Controles
        self.validarInCeduR=self.ventRegisR.register(self.validaCedulaIn);
        self.validarInFechaR=self.ventRegisR.register(self.validaFechaIn);
        # RadioButton
        self.radioReg = Radiobutton(self.ventRegisR, text="Usuario", bg=self.colorCorp, activebackground=self.colorCorp,
                                    font=(self.fontOCR, 14), variable=self.radioV, value=1, cursor=self.cursorBot,
                                    command=lambda:[self.habilitaEntryCodigo(), self.insertaCodigoEntryReg()]);
        self.radioReg.place(x=30, y=90);
        self.radioReg = Radiobutton(self.ventRegisR, text="Administrador", bg=self.colorCorp,
                                    activebackground=self.colorCorp,
                                    font=(self.fontOCR, 14), variable=self.radioV, value=2, cursor=self.cursorBot,
                                    command=lambda: [self.habilitaEntryCodigo(), self.insertaCodigoEntryReg()]);
        self.radioReg.place(x=200, y=90);
        # Labels
        self.labelRegTitu = Label(self.ventRegisR, text="REGISTRO", fg=self.colorFgW, bg=self.colorCorp,
                                  font=("Tw Cen MT Condensed Extra Bold", 26));
        self.labelRegTitu.place(x=20, y=10);
        self.labelRegTipo = Label(self.ventRegisR, text="¿Cómo quieres registrarte?", fg=self.colorFgW, bg=self.colorCorp,
                                  font=(self.fontOCR, 14));
        self.labelRegTipo.place(x=20, y=60);
        self.labelRegCedu = Label(self.ventRegisR, text="Cédula:", fg=self.colorFgW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegCedu.place(x=30, y=130);
        self.labelRegCodi = Label(self.ventRegisR, text="Código:", fg=self.colorFgW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegCodi.place(x=210, y=130);
        self.labelRegNom = Label(self.ventRegisR, text="Nombres:", fg=self.colorFgW, bg=self.colorCorp,
                                 font=(self.fontOCR, 12));
        self.labelRegNom.place(x=30, y=185);
        self.labelRegApe = Label(self.ventRegisR, text="Apellidos:", fg=self.colorFgW, bg=self.colorCorp,
                                 font=(self.fontOCR, 12));
        self.labelRegApe.place(x=210, y=185);
        self.labelRegFNacim = Label(self.ventRegisR, text="Fech. Nacim.:", fg=self.colorFgW, bg=self.colorCorp,
                                    font=(self.fontOCR, 12));
        self.labelRegFNacim.place(x=30, y=240);
        self.labelRegNick = Label(self.ventRegisR, text="Usuario:", fg=self.colorFgW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegNick.place(x=210, y=240);
        self.labelRegTelf = Label(self.ventRegisR, text="Teléfono:", fg=self.colorFgW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegTelf.place(x=30, y=295);
        self.labelRegMail = Label(self.ventRegisR, text="Email:", fg=self.colorFgW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegMail.place(x=210, y=295);
        self.labelRegPass = Label(self.ventRegisR, text="Contraseña:", fg=self.colorFgW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegPass.place(x=30, y=350);
        self.labelRegPassA = Label(self.ventRegisR, text="Repita Contraseña:", fg=self.colorFgW, bg=self.colorCorp,
                                   font=(self.fontOCR, 12));
        self.labelRegPassA.place(x=210, y=350);
        # Entrys
        self.entryRegCodi = Entry(self.ventRegisR, state=DISABLED, font=(self.fontCali, 12),
                                  textvariable=self.regCodeV,
                                  validate="key", validatecommand=(self.validarInCeduR, "%S"));
        self.entryRegCodi.place(x=215, y=155, width=100);
        self.entryRegCedu = Entry(self.ventRegisR, font=(self.fontCali, 12), textvariable=self.regCeduV,
                                  validate="key", validatecommand=(self.validarInCeduR, "%S"));
        self.entryRegCedu.place(x=35, y=155, width=150);
        self.regCeduV.trace("w", lambda *args: self.limitadorCedula(self.regCeduV));
        self.entryRegNom = Entry(self.ventRegisR, font=(self.fontCali, 11), textvariable=self.regNomV);
        self.entryRegNom.place(x=35, y=210, width=150);
        self.entryRegApe = Entry(self.ventRegisR, font=(self.fontCali, 11), textvariable=self.regApeV);
        self.entryRegApe.place(x=215, y=210, width=150);
        self.entryRegFNacim = Entry(self.ventRegisR, font=(self.fontCali, 12), textvariable=self.regFechaV,
                                    validate="key", validatecommand=(self.validarInFechaR, "%d", "%S", "%s"));
        self.entryRegFNacim.place(x=35, y=265, width=150);
        self.entryRegNick = Entry(self.ventRegisR, font=(self.fontCali, 12), textvariable=self.regUserV);
        self.entryRegNick.place(x=215, y=265, width=150);
        self.entryRegTelf = Entry(self.ventRegisR, font=(self.fontCali, 12), textvariable=self.regTelfV,
                                  validate="key", validatecommand=(self.validarInCeduR, "%S"));
        self.entryRegTelf.place(x=35, y=320, width=150);
        self.regTelfV.trace("w", lambda *args: self.limitadorCedula(self.regTelfV));
        self.entryRegMail = Entry(self.ventRegisR, font=(self.fontCali, 11), textvariable=self.regMailV);
        self.entryRegMail.place(x=215, y=320, width=150);
        self.entryRegPass = Entry(self.ventRegisR, show="*", font=(self.fontCali, 12), textvariable=self.regPass1V);
        self.entryRegPass.place(x=35, y=375, width=150);
        self.entryRegPassA = Entry(self.ventRegisR, show="*", font=(self.fontCali, 12), textvariable=self.regPass2V);
        self.entryRegPassA.place(x=215, y=375, width=150);
        # Botones
        self.botRegisAcep = Button(self.ventRegisR, text="Aceptar", font=(self.fontOCR, 12),
                                   fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                   command=lambda:[self.validacionRegistro(Bd.extraeFor(Bd.daFinalCodeUser()) + 1,
                                                                           self.regCodeV.get())],
                                   cursor=self.cursorBot);
        self.botRegisAcep.place(x=90, y=420);
        self.botRegisCanc = Button(self.ventRegisR, text="Cancelar", font=(self.fontOCR, 12),
                                   fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                   command=lambda:[self.destroyVentana(self.ventRegisR),
                                                   self.returnVentana(self.ventLoginR)],
                                   cursor=self.cursorBot);
        self.botRegisCanc.place(x=220, y=420);

    def ventInicioUser(self, tempCodeUser):  #Inicio, Eventos, Datos
        self.ventInicioUR=Toplevel(self.ventLoginR);
        self.ventInicioUR.title("Ventana Inicio de Usuario");  # Da título a la ventana
        self.ventInicioUR.state('zoomed');  # Inicializa la veentana maximizada
        self.ventInicioUR.iconbitmap("Recursos\corpcitico.ico");  # Inserta icono a la app
        self.ventInicioUR.resizable(0, 0);
        # Recursos
        self.imgLogoU=PhotoImage(file="Recursos\corpciti.png");  # Inserto Imagen
        self.imgWebU=PhotoImage(file="Recursos\web.png");
        self.colorFrameTitle = "gray";  # Color establecido para el frame título
        # Frames
        # Ventana Principal
        self.frameTitle=Frame(self.ventInicioUR, height='105', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameTitle.pack(fill='x', expand=False);  # Ajusta el frame a la ventana(ventInicio)
        # Frame de Opciones
        self.frameOption=Frame(self.ventInicioUR, height='50', background=self.colorCorp, bd=5);
        self.frameOption.pack(fill='x');
        # Frame Inicio
        self.frameHome=Frame(self.ventInicioUR, height='800', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameHome.pack(fill='x');
        #Variables
        self.saludoPV=StringVar();
        self.saludoPV.set(Bd.daUnDatoUser(tempCodeUser, 2));
        self.myCodeEIUV=StringVar();
        self.myCodeAIUV=StringVar();
        self.myTitulIUV=StringVar();
        self.myDescripIUV=StringVar();
        self.myLugarIUV=StringVar();
        self.myFechaIUV=StringVar();
        self.myHoraIUV=StringVar();
        self.myBoletoIUV=StringVar();
        #Control
        self.fFrameMyEventoB(self.frameHome, 350, 60, self.myCodeEIUV, self.myCodeAIUV,
                             self.myTitulIUV, self.myDescripIUV, self.myLugarIUV, self.myFechaIUV,
                             self.myHoraIUV, self.myBoletoIUV);
        self.posIU0=0; self.posIU1=1; self.posIU2=2; self.posIU3=3;
        self.posIU4=4; self.posIU5=5; self.posIU6=6; self.posIU7=7;
        self.posIU8=16;
        if (Bd.validaEventNullI() == True):
            self.myCodeEIUV.set(Bd.devuelveEvents(self.posIU0));
            self.myTitulIUV.set(Bd.devuelveEvents(self.posIU1));
            self.myDescripIUV.set(Bd.devuelveEvents(self.posIU2));
            self.myLugarIUV.set(Bd.devuelveEvents(self.posIU3));
            self.myFechaIUV.set(Bd.devuelveEvents(self.posIU4));
            self.myHoraIUV.set(Bd.devuelveEvents(self.posIU5));
            self.myBoletoIUV.set(Bd.devuelveEvents(self.posIU6));
            self.myCodeAIUV.set(Bd.daNameAdminByCode(Bd.devuelveEvents(self.posIU7)));
        else:
            self.myCodeEIUV.set("XXXXX");
            self.myTitulIUV.set("Aquí va el título de tu evento creado");
            self.myDescripIUV.set("Aquí va una descripción de tu evento");
            self.myLugarIUV.set("Aquí el lugar donde se realizará");
            self.myFechaIUV.set("dd/mm/yyyy");
            self.myHoraIUV.set("02:00 AM");
            self.myBoletoIUV.set("100000");
            self.myCodeAIUV.set("Admin");
        # Crear los elementos
        # Crear Labels y botón
        self.imagenLogo=ttk.Label(self.frameTitle, image=self.imgLogoU, anchor="center");
        self.labelTitulo=ttk.Label(self.frameTitle,
                                     text="Corporación de Ciencia\nTecnología e Innovación del Ecuador",
                                     foreground=self.colorFgW, background=self.colorFrameTitle,
                                     font=("Imprint MT Shadow", 26),
                                     justify=CENTER);
        self.saludoEntidad1=ttk.Label(self.frameOption, text="Hola ",
                                       foreground=self.colorFgW, background=self.colorCorp,
                                       font=(self.fontOCR, 18),
                                       justify=CENTER);
        self.saludoEntidad=ttk.Label(self.frameOption, textvariable=self.saludoPV,
                                       foreground=self.colorFgW, background=self.colorCorp,
                                       font=(self.fontOCR, 18),
                                       justify=CENTER);
        self.tituloDatosEventIU=Label(self.frameHome, text="TODOS LOS EVENTOS", fg=self.colorFgW,
                                      bg=self.colorFrameTitle, font=("Tw Cen MT Condensed Extra Bold", 20));
        # Inserta y configura Labels
        self.tituloDatosEventIU.place(x=10, y=10);
        self.imagenLogo.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.labelTitulo.pack(side=TOP, expand=False, padx=330, pady=0);
        self.saludoEntidad1.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.saludoEntidad.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        # Crea Botones
        self.botonPagMain = ttk.Button(self.frameTitle, image=self.imgWebU, command=self.web, cursor=self.cursorBot);
        self.botonIniUser = Button(self.frameOption, text="Inicio", font=(self.fontOCR, 12),
                                   foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                   cursor=self.cursorBot, command=lambda: []);
        self.botonMiEvents=Button(self.frameOption, text="Mis Eventos", font=(self.fontOCR, 12),
                                  foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                  cursor=self.cursorBot,
                                  command=lambda:[self.cambiaFrame(self.frameDatos),
                                                  self.fFrameMyEventU(self.ventInicioUR, tempCodeUser)]);
        self.botonMiDato = Button(self.frameOption, text="Mis Datos", font=(self.fontOCR, 12), fg=self.colorFgW,
                                  background=self.colorCorp, relief="flat", cursor=self.cursorBot,
                                  command=lambda: [self.cambiaFrame(self.frameHome),
                                                   self.fFrameDatosU(self.ventInicioUR, tempCodeUser),
                                                   self.muestraDatosUser(tempCodeUser)]);
        self.botonIniSalir = Button(self.frameOption, text="Cerrar Sesión", font=(self.fontOCR, 12),
                                    foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                    cursor=self.cursorBot, command=lambda:[self.destroyVentana(self.ventInicioUR),
                                                                           self.returnVentana(self.ventLoginR)]);
        self.botonNextEventIU=Button(self.frameHome, text="Siguiente", font=(self.fontOCR, 14),
                                      fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                      cursor=self.cursorBot, height=2, width=9,
                                      command=lambda: [self.sgtEventIU()]);
        self.botonLastEventIU=Button(self.frameHome, text="Anterior", font=(self.fontOCR, 14),
                                      fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                      cursor=self.cursorBot, height=2, width=9,
                                      command=lambda: [self.antesEventIU()]);
        self.botonInsideEvent=Button(self.frameHome, text="Enlistarse", font=(self.fontOCR, 14),
                                     fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                     cursor=self.cursorBot, height=2, width=9,
                                     command=lambda:[self.validacionEnlista(tempCodeUser)]);
        # Inserta Botones
        self.botonPagMain.pack(side=RIGHT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.botonIniSalir.pack(side=RIGHT, expand=False, padx=20, pady=0, ipadx=0, ipady=0);
        self.botonMiDato.pack(side=RIGHT, expand=False, padx=30, pady=0, ipadx=0, ipady=0);
        self.botonMiEvents.pack(side=RIGHT, expand=False, padx=40, pady=0, ipadx=0, ipady=0);
        self.botonIniUser.pack(side=RIGHT, expand=False, padx=50, pady=0, ipadx=0, ipady=0);
        self.botonNextEventIU.place(x=960, y=260);
        self.botonLastEventIU.place(x=230, y=260);
        self.botonInsideEvent.place(x=580, y=470, width=150);

    def ventInicioAdmi(self, tempCodeAdmi):
        self.ventInicioAR = Toplevel(self.ventLoginR);
        self.ventInicioAR.title("Ventana Inicio de Administrador");  # Da título a la ventana
        self.ventInicioAR.state('zoomed');  # Inicializa la veentana maximizada
        self.ventInicioAR.iconbitmap("Recursos\corpcitico.ico");  # Inserta icono a la app
        self.ventInicioAR.resizable(0, 0);
        # Recursos
        self.imgLogoA = PhotoImage(file="Recursos\corpciti.png");  # Inserto Imagen
        self.imgWebA = PhotoImage(file="Recursos\web.png");
        self.colorFrameTitle = "gray";  # Color establecido para el frame título
        # Variables
        self.saludoPVA = StringVar();
        self.myCodeEIV = StringVar();
        self.myCodeAIV = StringVar();
        self.myTitulIV = StringVar();
        self.myDescripIV = StringVar();
        self.myLugarIV = StringVar();
        self.myFechaIV = StringVar();
        self.myHoraIV = StringVar();
        self.myBoletoIV = StringVar();
        self.saludoPVA.set(Bd.daUnDatoAdmi(tempCodeAdmi, 2));
        #Control
        self.posI0=0; self.posI1=1; self.posI2=2; self.posI3=3; self.posI4=4;
        self.posI5=5; self.posI6=6; self.posI7=7; self.posI8=16;
        if (Bd.validaEventNullI()==True):
            self.myCodeEIV.set(Bd.devuelveEvents(self.posI0));
            self.myTitulIV.set(Bd.devuelveEvents(self.posI1));
            self.myDescripIV.set(Bd.devuelveEvents(self.posI2));
            self.myLugarIV.set(Bd.devuelveEvents(self.posI3));
            self.myFechaIV.set(Bd.devuelveEvents(self.posI4));
            self.myHoraIV.set(Bd.devuelveEvents(self.posI5));
            self.myBoletoIV.set(Bd.devuelveEvents(self.posI6));
            self.myCodeAIV.set(Bd.devuelveEvents(self.posI7));
        else:
            self.myCodeEIV.set("XXXXX");
            self.myTitulIV.set("Aquí va el título de tu evento creado");
            self.myDescripIV.set("Aquí va una descripción de tu evento");
            self.myLugarIV.set("Aquí el lugar donde se realizará");
            self.myFechaIV.set("dd/mm/yyyy");
            self.myHoraIV.set("02:00 AM");
            self.myBoletoIV.set("100000");
            self.myCodeAIV.set(tempCodeAdmi);
        # Frames
        # Ventana Principal
        self.frameTitleA=Frame(self.ventInicioAR, height='105', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameTitleA.pack(fill='x', expand=False);  # Ajusta el frame a la ventana(ventInicio)
        # Frame de Opciones
        self.frameOptionA= Frame(self.ventInicioAR, height='50', background=self.colorCorp, bd=5);
        self.frameOptionA.pack(fill='x');
        # Frame Inicio
        self.frameHomeA=Frame(self.ventInicioAR, height='800', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameHomeA.pack(fill='x');
        self.fFrameMyEventoB(self.frameHomeA, 350, 80, self.myCodeEIV, self.myCodeAIV,
                             self.myTitulIV, self.myDescripIV, self.myLugarIV, self.myFechaIV,
                             self.myHoraIV, self.myBoletoIV);
        # Crear los elementos
        # Crear Labels y botón
        self.imagenLogoA = ttk.Label(self.frameTitleA, image=self.imgLogoA, anchor="center");
        self.labelTituloA = ttk.Label(self.frameTitleA,
                                      text="Corporación de Ciencia\nTecnología e Innovación del Ecuador",
                                      foreground=self.colorFgW, background=self.colorFrameTitle,
                                      font=("Imprint MT Shadow", 26),
                                      justify=CENTER);
        self.saludoEntidad1A=ttk.Label(self.frameOptionA, text="Hola ",
                                        foreground=self.colorFgW, background=self.colorCorp,
                                        font=(self.fontOCR, 18),
                                        justify=CENTER);
        self.saludoEntidadA=Label(self.frameOptionA, textvariable=self.saludoPVA,
                                    foreground=self.colorFgW, background=self.colorCorp,
                                    font=(self.fontOCR, 18), justify=CENTER);
        self.tituloDatosEventI=Label(self.frameHomeA, text="TODOS LOS EVENTOS", fg=self.colorFgW,
                                      bg=self.colorFrameTitle, font=("Tw Cen MT Condensed Extra Bold", 20));
        # Inserta y configura Labels
        self.tituloDatosEventI.place(x=10, y=10);
        self.imagenLogoA.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.labelTituloA.pack(side=TOP, expand=False, padx=330, pady=0);
        self.saludoEntidad1A.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.saludoEntidadA.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        # Crea Botones
        self.botonPagMainA=ttk.Button(self.frameTitleA, image=self.imgWebA, command=self.web, cursor=self.cursorBot);
        self.botonIniA=Button(self.frameOptionA, text="Inicio", font=(self.fontOCR, 12),
                                foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                cursor=self.cursorBot);
        self.botonMiEventsA=Button(self.frameOptionA, text="Mis Eventos", font=(self.fontOCR, 12),
                                   foreground=self.colorFgW, background=self.colorCorp, relief="flat", cursor=self.cursorBot,
                                   command=lambda: [self.cambiaFrame(self.frameDatosA),
                                                    self.fFrameMyEventA(self.ventInicioAR, tempCodeAdmi)]);
        self.botonMiDatoA=Button(self.frameOptionA, text="Mis Datos", font=(self.fontOCR, 12), fg=self.colorFgW,
                                 background=self.colorCorp, relief="flat", cursor=self.cursorBot,
                                 command=lambda: [self.cambiaFrame(self.frameHomeA),
                                                  self.fFrameDatosA(self.ventInicioAR, tempCodeAdmi),
                                                  self.muestraDatosAdmi(tempCodeAdmi)]);
        self.botonIniSalirA=Button(self.frameOptionA, text="Cerrar Sesión", font=(self.fontOCR, 12),
                                     foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                     cursor=self.cursorBot, command=lambda: [self.destroyVentana(self.ventInicioAR),
                                                                            self.returnVentana(self.ventLoginR)]);
        self.botonNextEventI=Button(self.frameHomeA, text="Siguiente", font=(self.fontOCR, 14),
                                     fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                     cursor=self.cursorBot, height=2, width=9,
                                     command=lambda: [self.sgtEventI()]);
        self.botonLastEventI=Button(self.frameHomeA, text="Anterior", font=(self.fontOCR, 14),
                                     fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                     cursor=self.cursorBot, height=2, width=9,
                                     command=lambda: [self.antesEventI()]);
        # Inserta Botones
        self.botonPagMainA.pack(side=RIGHT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.botonIniSalirA.pack(side=RIGHT, expand=False, padx=20, pady=0, ipadx=0, ipady=0);
        self.botonMiDatoA.pack(side=RIGHT, expand=False, padx=30, pady=0, ipadx=0, ipady=0);
        self.botonMiEventsA.pack(side=RIGHT, expand=False, padx=40, pady=0, ipadx=0, ipady=0);
        self.botonIniA.pack(side=RIGHT, expand=False, padx=50, pady=0, ipadx=0, ipady=0);
        self.botonNextEventI.place(x=960, y=260);
        self.botonLastEventI.place(x=230, y=260);

def main():
    mi_app = Ventana();
    return 0;

if __name__ == '__main__':
    main();