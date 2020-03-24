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
        self.loggPersonV = StringVar();
        self.loggPassV = StringVar();
        # Da dimensiones a la ventana y establezco la posición
        self.ventLoginR.geometry("270x270+{}+{}".format(int(self.anchoPantalla / 3), int(self.altoPantalla / 3)));
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
        self.entryUser = Entry(self.ventLoginR, textvariable=self.loggPersonV);
        self.entryUser.place(x=137, y=100);
        self.entryPass = Entry(self.ventLoginR, textvariable=self.loggPassV);
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
                                command=self.validacionlogin);
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
                                foreground=self.colorFgW, background=self.colorCorp, state=DISABLED,
                                exportselection=1);
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
                cont += 1;
        if (cont==0):
            messagebox.showerror("Error de consulta",
                                 "La cédula ingresada no pertenece a ninguna cuenta registrada");

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

    def validacionlogin(self):
        if (self.loggPersonV.get()== "" or self.loggPassV.get()== ""):
            messagebox.showerror("Error de Loggin", "Debes llenar los campos primero");
        elif(self.loggPersonV.get().isspace() or self.loggPassV.get().isspace()):
            messagebox.showerror("Error de Loggin", "Los espacios no cuenta como llenar los campos");
        elif(Re.loguinUser(self.loggPersonV.get(), self.loggPassV.get()) == True):
            self.hideVentana(self.ventLoginR);
            self.ventInicioUser();
        elif(Re.loguinUser(self.loggPersonV.get(), self.loggPassV.get()) == False):
            messagebox.showerror("Error de Ingreso", "Usuario y Contraseña incorrectos");
        elif(Re.loguinAdmi(self.loggPersonV.get(), self.loggPassV.get()) == True):
            self.hideVentana(self.ventLoginR);
            self.ventInicioAdmi();
        elif (Re.loguinAdmi(self.loggPersonV.get(), self.loggPassV.get()) == False):
            messagebox.showerror("Error de Ingreso", "Usuario y Contraseña incorrectos");
        else: messagebox.showerror("Error de Ingreso", "Usuario y Contraseña incorrectos");

    def validacionRegistro(self):
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
                messagebox.showwarning("Error de Registro", "Hay campos vacíos\nDebes llenar todos los campos");
            elif(self.regPass1V.get()!=self.regPass2V.get()):
                messagebox.showwarning("Error de Registro", "No coinciden las contraseñas");
            else:
                self.destroyVentana(self.ventRegisR);
                self.insertaPersona();
                self.ventInicioUser();
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
                messagebox.showwarning("Error de Registro", "Hay campos vacíos\nDebes llenar todos los campos");
            elif (self.regPass1V.get() != self.regPass2V.get()):
                messagebox.showwarning("Error de Registro", "No coinciden las contraseñas");
            else:
                self.cont=0;
                for i in Bd.extraeArray(Bd.daCodeAdmi()):
                    if (int(self.regCodeV.get())==i):
                        self.destroyVentana(self.ventRegisR);
                        self.insertaPersona();
                        self.ventInicioAdmi();self.cont+=1;
                if (self.cont==0):
                    messagebox.showerror("Error de consulta",
                                         "El código ingresado no pertenece a ningún administrador en nuestra Base de Datos");

    def validacionEdicion(self):
        if (self.regCeduVe.get().isspace() or self.regCeduVe.get() == "" or
                self.regNomVe.get().isspace() or self.regNomVe.get() == "" or
                self.regApeVe.get().isspace() or self.regApeVe.get() == "" or
                self.regFechaVe.get().isspace() or self.regFechaVe.get() == "" or
                self.regUserVe.get().isspace() or self.regUserVe.get() == "" or
                self.regTelfVe.get().isspace() or self.regTelfVe.get() == "" or
                self.regMailVe.get().isspace() or self.regMailV.get() == "" or
                self.regPass1Ve.get().isspace() or self.regPass1Ve.get() == ""):
            messagebox.showwarning("Error de Registro", "Debes llenar todos los campos");

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

    def muestraUser(self):
        Re.listataUser(self.contCodePU);

    def editaDatosU(self):
        E1 = Clases.Usuario(self.contCodePU, self.regCeduVe.get(), self.regNomVe.get(),
                            self.regApeVe.get(), self.regFechaVe.get(), self.regUserVe.get(),
                            self.regTelfVe.get(), self.regMailVe.get(), self.regPass1Ve.get());
        Re.editaUser(int(self.contCodePU), E1);
        messagebox.showinfo("Edición Exitosa", "Se editaron tus datos correctamente :)")

    def limpiaEditar(self):
        self.regCeduVe.set("");
        self.regNomVe.set("");
        self.regApeVe.set("");
        self.regFechaVe.set("");
        self.regUserVe.set("");
        self.regTelfVe.set("");
        self.regMailVe.set("");
        self.regPass1Ve.set("");

    def insertaCodigoEntryReg(self):
        if (self.radioV.get() == 1):
            self.regCodeV.set(self.contCodePU);
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

    def fFrameEvento(self, frameRoot):
        self.frameEvent = Frame(frameRoot, height='300', width='600', bg=self.colorFrameTitle, bd=5, relief='raised');
        self.frameEvent.place(x=50, y=50);
        self.frameEvent1 = Frame(frameRoot, height='300', width='600', bg=self.colorFrameTitle, bd=5, relief='raised');
        self.frameEvent1.place(x=700, y=50);
        # flat, groove, raised, ridge, solid, or sunken

    def fFrameDatosU(self, Root):
        #Variables de control
        self.regCeduVe = StringVar();
        self.regNomVe = StringVar();
        self.regApeVe = StringVar();
        self.regFechaVe = StringVar();
        self.regUserVe = StringVar();
        self.regTelfVe = StringVar();
        self.regMailVe = StringVar();
        self.regPass1Ve = StringVar();
        self.regPass2Ve = StringVar();
        #Control
        self.validarInCeduE = self.ventRegisR.register(self.validaCedulaIn);
        self.validarInFechaE = self.ventRegisR.register(self.validaFechaIn)
        #Frame
        self.frameDatos = Frame(Root, height='800', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameDatos.pack(fill='x');
        #Labels
        self.tituloDatos = Label(self.frameDatos, text="INFORMACIÓN DE USUARIO", fg=self.colorFgW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 20));
        self.codigoDatosA = Label(self.frameDatos, text="Código: ", fg=self.colorFgW, bg=self.colorFrameTitle,
                                  font=(self.fontOCR, 14));
        self.codigoDatosB = Label(self.frameDatos, text=self.contCodePU, fg=self.colorFgW, bg=self.colorFrameTitle,
                                  font=(self.fontCali, 14));
        self.cedulaDatos = Label(self.frameDatos, text="Cédula:", fg=self.colorFgW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 14));
        self.nombreDatos = Label(self.frameDatos, text="Nombre:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                 font=(self.fontOCR, 14));
        self.apellidoDatos = Label(self.frameDatos, text="Apellido:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                   font=(self.fontOCR, 14));
        self.fechaDatos = Label(self.frameDatos, text="Fecha de Nacimiento:", fg=self.colorFgW, bg=self.colorFrameTitle,
                                font=(self.fontOCR, 14));
        self.userDatos = Label(self.frameDatos, text="Nombre de Usuario:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.telfDatos = Label(self.frameDatos, text="Teléfono:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.mailDatos = Label(self.frameDatos, text="Correo Electrónico:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.passDatos = Label(self.frameDatos, text="Contraseña:", fg=self.colorFgW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        # Coloca Labels
        self.tituloDatos.place(x=20, y=10);
        self.codigoDatosA.place(x=60, y=80);
        self.codigoDatosB.place(x=150, y=80);
        self.cedulaDatos.place(x=60, y=120);
        self.nombreDatos.place(x=60, y=160);
        self.apellidoDatos.place(x=505, y=160);
        self.fechaDatos.place(x=400, y=200);
        self.userDatos.place(x=60, y=280);
        self.telfDatos.place(x=60, y=200);
        self.mailDatos.place(x=60, y=240);
        self.passDatos.place(x=500, y=280);
        #Entrys
        self.entryCedu = Entry(self.frameDatos, font=(self.fontCali, 12), textvariable=self.regCeduVe,
                               validate="key", validatecommand=(self.validarInCeduE, "%S"));
        self.entryCedu.place(x=150, y=120, width=150);
        self.regCeduV.trace("w", lambda *args: self.limitadorCedula(self.regCeduVe));
        self.entryNom = Entry(self.frameDatos, font=(self.fontCali, 11), textvariable=self.regNomVe);
        self.entryNom.place(x=150, y=160, width=300);
        self.entryApe = Entry(self.frameDatos, font=(self.fontCali, 11), textvariable=self.regApeVe);
        self.entryApe.place(x=630, y=160, width=300);
        self.entryFNacim = Entry(self.frameDatos, font=(self.fontCali, 12), textvariable=self.regFechaVe,
                                 validate="key", validatecommand=(self.validarInFechaE, "%d", "%S", "%s"));
        self.entryFNacim.place(x=630, y=200, width=150);
        self.entryNick = Entry(self.frameDatos, font=(self.fontCali, 12), textvariable=self.regUserVe);
        self.entryNick.place(x=280, y=280, width=150);
        self.entryTelf = Entry(self.frameDatos, font=(self.fontCali, 12), textvariable=self.regTelfVe,
                               validate="key", validatecommand=(self.validarInCeduE, "%S"));
        self.entryTelf.place(x=170, y=200, width=170);
        self.regTelfV.trace("w", lambda *args: self.limitadorCedula(self.regTelfV));
        self.entryMail = Entry(self.frameDatos, font=(self.fontCali, 11), textvariable=self.regMailVe);
        self.entryMail.place(x=280, y=240, width=350);
        self.entryPassA = Entry(self.frameDatos, show="*", font=(self.fontCali, 12), textvariable=self.regPass1Ve);
        self.entryPassA.place(x=630, y=280, width=150);
        #Botones
        self.botonEditaU = Button(self.frameDatos, text="Editar", font=(self.fontOCR, 12),
                                  fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                  cursor=self.cursorBot, height=2, width=9,
                                  command=lambda:[self.editaDatosU(), self.limpiaEditar()]);
        self.botonEditaU.place(x=790, y=350);

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
        self.radioReg.place(x=200, y=90, );
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
                                   command=lambda:[self.validacionRegistro()],
                                   cursor=self.cursorBot);
        self.botRegisAcep.place(x=90, y=420);
        self.botRegisCanc = Button(self.ventRegisR, text="Cancelar", font=(self.fontOCR, 12),
                                   fg=self.colorFgW, bg=self.colorCorp, relief="groove",
                                   command=lambda:[self.destroyVentana(self.ventRegisR),
                                                   self.returnVentana(self.ventLoginR)],
                                   cursor=self.cursorBot);
        self.botRegisCanc.place(x=220, y=420);

    def ventInicioUser(self):  # Inicio, Eventos, Datos
        self.ventInicioUR = Toplevel(self.ventLoginR);
        self.ventInicioUR.title("Ventana Inicio de Usuario");  # Da título a la ventana
        self.ventInicioUR.state('zoomed');  # Inicializa la veentana maximizada
        self.ventInicioUR.iconbitmap("Recursos\corpcitico.ico");  # Inserta icono a la app
        self.ventInicioUR.resizable(0, 0);
        # Recursos
        self.imgLogo = PhotoImage(file="Recursos\corpciti.png");  # Inserto Imagen
        self.imgWeb = PhotoImage(file="Recursos\web.png");
        self.colorFrameTitle = "gray";  # Color establecido para el frame título
        # Frames
        # Ventana Principal
        self.frameTitle = Frame(self.ventInicioUR, height='105', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameTitle.pack(fill='x', expand=False);  # Ajusta el frame a la ventana(ventInicio)
        # Frame de Opciones
        self.frameOption = Frame(self.ventInicioUR, height='50', background=self.colorCorp, bd=5);
        self.frameOption.pack(fill='x');
        # Frame Inicio
        self.frameHome = Frame(self.ventInicioUR, height='800', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameHome.pack(fill='x');
        self.fFrameEvento(self.frameHome);
        # Crear los elementos
        # Crear Labels y botón
        self.imagenLogo = ttk.Label(self.frameTitle, image=self.imgLogo, anchor="center");
        self.labelTitulo = ttk.Label(self.frameTitle,
                                     text="Corporación de Ciencia\nTecnología e Innovación del Ecuador",
                                     foreground=self.colorFgW, background=self.colorFrameTitle,
                                     font=("Imprint MT Shadow", 26),
                                     justify=CENTER);
        self.saludoEntidad = ttk.Label(self.frameOption, text="¡BIENVENIDO!",
                                       foreground=self.colorFgW, background=self.colorCorp,
                                       font=(self.fontOCR, 18),
                                       justify=CENTER);
        # Inserta y configura Labels
        self.imagenLogo.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.labelTitulo.pack(side=TOP, expand=False, padx=330, pady=0);
        self.saludoEntidad.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        # Crea Botones
        self.botonPagMain = ttk.Button(self.frameTitle, image=self.imgWeb, command=self.web, cursor=self.cursorBot);
        self.botonIniUser = Button(self.frameOption, text="Inicio", font=(self.fontOCR, 12),
                                   foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                   cursor=self.cursorBot, command=lambda: []);
        self.botonMiEvents = Button(self.frameOption, text="Mis Eventos", font=(self.fontOCR, 12),
                                    foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                    cursor=self.cursorBot);
        self.botonMiDato = Button(self.frameOption, text="Mis Datos", font=(self.fontOCR, 12), fg=self.colorFgW,
                                  background=self.colorCorp, relief="flat", cursor=self.cursorBot,
                                  command=lambda: [self.fFrameDatosU(self.ventInicioUR),
                                                   self.cambiaFrame(self.frameHome)]);
        self.botonIniSalir = Button(self.frameOption, text="Cerrar Sesión", font=(self.fontOCR, 12),
                                    foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                    cursor=self.cursorBot, command=lambda: [self.destroyVentana(self.ventInicioUR),
                                                                            self.returnVentana(self.ventLoginR)]);
        # Inserta Botones
        self.botonPagMain.pack(side=RIGHT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.botonIniSalir.pack(side=RIGHT, expand=False, padx=20, pady=0, ipadx=0, ipady=0);
        self.botonMiDato.pack(side=RIGHT, expand=False, padx=30, pady=0, ipadx=0, ipady=0);
        self.botonMiEvents.pack(side=RIGHT, expand=False, padx=40, pady=0, ipadx=0, ipady=0);
        self.botonIniUser.pack(side=RIGHT, expand=False, padx=50, pady=0, ipadx=0, ipady=0);

    def ventInicioAdmi(self):
        self.ventInicioAR = Toplevel(self.ventLoginR);
        self.ventInicioAR.title("Ventana Inicio de Administrador");  # Da título a la ventana
        self.ventInicioAR.state('zoomed');  # Inicializa la veentana maximizada
        self.ventInicioAR.iconbitmap("Recursos\corpcitico.ico");  # Inserta icono a la app
        self.ventInicioAR.resizable(0, 0);
        # Recursos
        self.imgLogo = PhotoImage(file="Recursos\corpciti.png");  # Inserto Imagen
        self.imgWeb = PhotoImage(file="Recursos\web.png");
        self.colorFrameTitle = "gray";  # Color establecido para el frame título
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
        self.fFrameEvento(self.frameHomeA);
        # Crear los elementos
        # Crear Labels y botón
        self.imagenLogoA = ttk.Label(self.frameTitleA, image=self.imgLogo, anchor="center");
        self.labelTituloA = ttk.Label(self.frameTitleA,
                                      text="Corporación de Ciencia\nTecnología e Innovación del Ecuador",
                                      foreground=self.colorFgW, background=self.colorFrameTitle,
                                      font=("Imprint MT Shadow", 26),
                                      justify=CENTER);
        self.saludoEntidadA = Label(self.frameOptionA, text="¡BIENVENIDO!",
                                    foreground=self.colorFgW, background=self.colorCorp,
                                    font=(self.fontOCR, 18), justify=CENTER);
        # Inserta y configura Labels
        self.imagenLogoA.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.labelTituloA.pack(side=TOP, expand=False, padx=330, pady=0);
        self.saludoEntidadA.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        # Crea Botones
        self.botonPagMainA = ttk.Button(self.frameTitleA, image=self.imgWeb, command=self.web, cursor=self.cursorBot);
        self.botonIniA = Button(self.frameOptionA, text="Inicio", font=(self.fontOCR, 12),
                                foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                cursor=self.cursorBot);
        self.botonMiEventsA = Button(self.frameOptionA, text="Mis Eventos", font=(self.fontOCR, 12),
                                     foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                     cursor=self.cursorBot);
        self.botonMiDatoA = Button(self.frameOptionA, text="Mis Datos", font=(self.fontOCR, 12), fg=self.colorFgW,
                                   background=self.colorCorp, relief="flat", cursor=self.cursorBot);
        self.botonIniSalirA = Button(self.frameOptionA, text="Cerrar Sesión", font=(self.fontOCR, 12),
                                     foreground=self.colorFgW, background=self.colorCorp, relief="flat",
                                     cursor=self.cursorBot, command=lambda: [self.destroyVentana(self.ventInicioAR),
                                                                            self.returnVentana(self.ventLoginR)]);
        # Inserta Botones
        self.botonPagMainA.pack(side=RIGHT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.botonIniSalirA.pack(side=RIGHT, expand=False, padx=20, pady=0, ipadx=0, ipady=0);
        self.botonMiDatoA.pack(side=RIGHT, expand=False, padx=30, pady=0, ipadx=0, ipady=0);
        self.botonMiEventsA.pack(side=RIGHT, expand=False, padx=40, pady=0, ipadx=0, ipady=0);
        self.botonIniA.pack(side=RIGHT, expand=False, padx=50, pady=0, ipadx=0, ipady=0);

def main():
    mi_app = Ventana();
    return 0;

if __name__ == '__main__':
    main();