import Clases;
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
Re = Repositorio.Repos();
class Ventana():
    def __init__(self):
        self.contCodeP = 1;
        self.ventLogin();

    def limitador(self, entry_text):
        if len(entry_text.get()) > 0:
            entry_text.set(entry_text.get()[:10])

    def web(self):
        webbrowser.open("http://corpciti.ec/", new=2, autoraise=True)

    def validaUser(self):
        if (self.radioV.get() == 1):
            self.entryRegCodi.config(state=DISABLED);

    def validaAdmi(self):
        self.entryRegCodi.config(state=NORMAL);

    def validaBlanco(self):
        if (self.radioV.get() == 1):
            try: (self.regCeduV.get().isspace() or self.regNomV.get().isspace() or self.regApeV.get().isspace()
                  or self.regFechaV.get().isspace() or self.regUserV.get().isspace() or
                  self.regTelfV.get().isspace() or self.regMailV.get().isspace() or self.regPass1V.get().isspace());
            except ValueError: messagebox.showwarning("Advertencia", "Debe llenar todos los campos");
        elif (self.radioV.get() == 2):
            try: (self.regCodeV.get().isspace(), self.regCeduV.get().isspace(),self.regNomV.get().isspace(),
                  self.regApeV.get().isspace(), self.regFechaV.get().isspace(), self.regUserV.get().isspace(),
                  self.regTelfV.get().isspace(), self.regMailV.get().isspace(), self.regPass1V.get().isspace());
            except ValueError: messagebox.showwarning("Advertencia", "Debe llenar todos los campos");

    def insertaPersona(self):
        if(self.radioV.get()==1):
            Cla=Clases.Usuario(self.contCodeP, self.regCeduV.get(), self.regNomV.get(),
                               self.regApeV.get(), self.regFechaV.get(), self.regUserV.get(),
                               self.regTelfV.get(), self.regMailV.get(), self.regPass1V.get());
            Re.insertaUser(Cla);
        elif (self.radioV.get()==2):
            Cla = Clases.Admin(self.regCodeV.get(), self.regCeduV.get(), self.regNomV.get(),
                               self.regApeV.get(), self.regFechaV.get(), self.regUserV.get(),
                               self.regTelfV.get(), self.regMailV.get(), self.regPass1V.get());
            Re.insertaAdm(Cla);
            self.contCodeP += 1;

    def codigoEntry(self):
        if (self.radioV.get() == 1):
            self.regCodeV.set(self.contCodeP);
            self.entryRegCodi.config(justify=RIGHT);
        elif (self.radioV.get() == 2):
            self.regCodeV.set("");
            self.entryRegCodi.config(justify=LEFT);

    def cambiaFrame(self, frame):
        frame.pack_forget();

    def ventLogin(self):
        # Recursos
        self.colorCorp = "#00A2CA";  # Color celeste de Corpciti
        self.fontOCR = "OCR A Extended";
        self.fontCali = "Calibri (Cuerpo)";
        self.fgColorW = "white";
        self.cursorBot = "hand2";
        # Ventana de Login
        self.ventLogin = Tk();
        altoPantalla = self.ventLogin.winfo_screenheight();  # Almacena la dimesión del alto de la pantalla en una variable
        anchoPantalla = self.ventLogin.winfo_screenwidth();  # Almacena la dimesión del alto de la pantalla en una variable
        self.ventLogin.title("Inicio");  # Da título a la ventana
        self.ventLogin.config(bg=self.colorCorp);  # Color de fondo o background
        # Da dimensiones a la ventana y establezco la posición
        self.ventLogin.geometry("270x270+{}+{}".format(int(anchoPantalla / 3), int(altoPantalla / 3)));
        self.ventLogin.iconbitmap("Recursos\corpcitico.ico");  # Inserta icono a la app
        self.ventLogin.resizable(0, 0);  # Ventana no redimensionable
        # Labels
        self.labeLogTitu = Label(self.ventLogin, text="CORPCITI", fg=self.fgColorW,
                                 bg=self.colorCorp, font=("Tw Cen MT Condensed Extra Bold", 26));
        self.labeLogTitu.pack(side="top");
        self.labeLogDesc = Label(self.ventLogin, text="Inicia Sesión", fg=self.fgColorW,
                                 bg=self.colorCorp, font=(self.fontOCR, 14));
        self.labeLogDesc.place(x=5, y=60);
        self.labeLogUser = Label(self.ventLogin, text="Usuario:", fg=self.fgColorW, bg=self.colorCorp,
                                 font=(self.fontOCR, 14));
        self.labeLogUser.place(x=7, y=95);
        self.labeLogPass = Label(self.ventLogin, text="Contraseña:", fg=self.fgColorW, bg=self.colorCorp,
                                 font=(self.fontOCR, 14));
        self.labeLogPass.place(x=7, y=130);
        # Entrys
        self.entryUser = Entry(self.ventLogin);
        self.entryUser.place(x=137, y=100);
        self.entryPass = Entry(self.ventLogin);
        self.entryPass.place(x=137, y=135);
        self.entryPass.config(show="*");
        # Botones
        self.botOlvidarPass = Button(self.ventLogin, text="Recordar contraseña", font=(self.fontOCR, 9),
                                     fg=self.fgColorW, bg=self.colorCorp, relief="flat", cursor=self.cursorBot);
        self.botOlvidarPass.place(x=7, y=155);
        self.botRegis = Button(self.ventLogin, text="Registro", command=self.registroPersona, font=(self.fontOCR, 12),
                               fg=self.fgColorW, bg=self.colorCorp, relief="groove", cursor=self.cursorBot);
        self.botRegis.place(x=30, y=195);
        self.botLoggin = Button(self.ventLogin, text="Ingresar", font=(self.fontOCR, 12), fg=self.fgColorW,
                                bg=self.colorCorp,
                                relief="groove", cursor=self.cursorBot);
        self.botLoggin.place(x=150, y=195);
        # flat, groove, raised, ridge, solid, or sunken
        self.ventLogin.mainloop();

    def registroPersona(self):
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
        self.ventRegis = Toplevel(self.ventLogin);
        self.ventRegis.grab_set();
        altoPantalla = self.ventRegis.winfo_screenheight();
        anchoPantalla = self.ventRegis.winfo_screenwidth();
        self.ventRegis.title("Ventana de Registro");
        self.ventRegis.config(bg=self.colorCorp);
        self.ventRegis.geometry("400x500+{}+{}".format(int(anchoPantalla/3), int(altoPantalla / 5)));
        self.ventRegis.iconbitmap("Recursos\corpcitico.ico");
        self.ventRegis.resizable(0, 0);
        # RadioButton
        self.radioReg = Radiobutton(self.ventRegis, text="Usuario", bg=self.colorCorp, activebackground=self.colorCorp,
                                    font=(self.fontOCR, 14), variable=self.radioV, value=1, cursor=self.cursorBot,
                                    command=lambda: [self.validaUser(), self.codigoEntry()]);
        self.radioReg.place(x=20, y=90);
        self.radioReg = Radiobutton(self.ventRegis, text="Administrador", bg=self.colorCorp,
                                    activebackground=self.colorCorp,
                                    font=(self.fontOCR, 14), variable=self.radioV, value=2, cursor=self.cursorBot,
                                    command=lambda: [self.validaAdmi(), self.codigoEntry()]);
        self.radioReg.place(x=200, y=90, );
        # Labels
        self.labelRegTitu = Label(self.ventRegis, text="REGISTRO", fg=self.fgColorW, bg=self.colorCorp,
                                  font=("Tw Cen MT Condensed Extra Bold", 26));
        self.labelRegTitu.place(x=20, y=10);
        self.labelRegTipo = Label(self.ventRegis, text="¿Cómo quieres loggearte?", fg=self.fgColorW, bg=self.colorCorp,
                                  font=(self.fontOCR, 14));
        self.labelRegTipo.place(x=20, y=60);
        self.labelRegCedu = Label(self.ventRegis, text="Cédula:", fg=self.fgColorW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegCedu.place(x=20, y=130);
        self.labelRegCodi = Label(self.ventRegis, text="Código:", fg=self.fgColorW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegCodi.place(x=200, y=130);
        self.labelRegNom = Label(self.ventRegis, text="Nombres:", fg=self.fgColorW, bg=self.colorCorp,
                                 font=(self.fontOCR, 12));
        self.labelRegNom.place(x=20, y=185);
        self.labelRegApe = Label(self.ventRegis, text="Apellidos:", fg=self.fgColorW, bg=self.colorCorp,
                                 font=(self.fontOCR, 12));
        self.labelRegApe.place(x=200, y=185);
        self.labelRegFNacim = Label(self.ventRegis, text="Fech. Nacim.:", fg=self.fgColorW, bg=self.colorCorp,
                                    font=(self.fontOCR, 12));
        self.labelRegFNacim.place(x=20, y=240);
        self.labelRegNick = Label(self.ventRegis, text="Usuario:", fg=self.fgColorW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegNick.place(x=200, y=240);
        self.labelRegTelf = Label(self.ventRegis, text="Teléfono:", fg=self.fgColorW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegTelf.place(x=20, y=295);
        self.labelRegMail = Label(self.ventRegis, text="Email:", fg=self.fgColorW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegMail.place(x=200, y=295);
        self.labelRegPass = Label(self.ventRegis, text="Contraseña:", fg=self.fgColorW, bg=self.colorCorp,
                                  font=(self.fontOCR, 12));
        self.labelRegPass.place(x=20, y=350);
        self.labelRegPassA = Label(self.ventRegis, text="Repita Contraseña:", fg=self.fgColorW, bg=self.colorCorp,
                                   font=(self.fontOCR, 12));
        self.labelRegPassA.place(x=200, y=350);
        # Entrys
        self.entryRegCodi = Entry(self.ventRegis, state=DISABLED, font=(self.fontCali, 12),
                                  textvariable=self.regCodeV);
        self.entryRegCodi.place(x=205, y=155, width=100);
        self.entryRegCedu = Entry(self.ventRegis, font=(self.fontCali, 12), textvariable=self.regCeduV);
        self.entryRegCedu.place(x=25, y=155, width=150);
        self.regCeduV.trace("w", lambda *args: self.limitador(self.regCeduV));
        self.entryRegNom = Entry(self.ventRegis, font=(self.fontCali, 11), textvariable=self.regNomV);
        self.entryRegNom.place(x=25, y=210, width=150);
        self.entryRegApe = Entry(self.ventRegis, font=(self.fontCali, 11), textvariable=self.regApeV);
        self.entryRegApe.place(x=205, y=210, width=150);
        self.entryRegFNacim = Entry(self.ventRegis, font=(self.fontCali, 12), textvariable=self.regFechaV);
        self.entryRegFNacim.place(x=25, y=265, width=150);
        self.entryRegNick = Entry(self.ventRegis, font=(self.fontCali, 12), textvariable=self.regUserV);
        self.entryRegNick.place(x=205, y=265, width=150);
        self.entryRegTelf = Entry(self.ventRegis, font=(self.fontCali, 12), textvariable=self.regTelfV);
        self.entryRegTelf.place(x=25, y=320, width=150);
        self.regTelfV.trace("w", lambda *args: self.limitador(self.regTelfV));
        self.entryRegMail = Entry(self.ventRegis, font=(self.fontCali, 11), textvariable=self.regMailV);
        self.entryRegMail.place(x=205, y=320, width=150);
        self.entryRegPass = Entry(self.ventRegis, show="*", font=(self.fontCali, 12), textvariable=self.regPass1V);
        self.entryRegPass.place(x=25, y=375, width=150);
        self.entryRegPassA = Entry(self.ventRegis, show="*", font=(self.fontCali, 12), textvariable=self.regPass2V);
        self.entryRegPassA.place(x=205, y=375, width=150);
        # Botones
        self.botRegisAcep = Button(self.ventRegis, text="Aceptar", font=(self.fontOCR, 12),
                                   fg=self.fgColorW, bg=self.colorCorp, relief="groove",
                                   command=lambda: [self.validaBlanco(), self.ventLogin.destroy(), self.ventInicioU(),
                                                    self.insertaPersona()],
                                   cursor=self.cursorBot);
        self.botRegisAcep.place(x=40, y=420);
        self.botRegisCanc = Button(self.ventRegis, text="Cancelar", font=(self.fontOCR, 12),
                                   fg=self.fgColorW, bg=self.colorCorp, relief="groove",
                                   command=self.ventRegis.destroy, cursor=self.cursorBot);
        self.botRegisCanc.place(x=200, y=420);

    def fFrameEvento(self, frameRoot):
        self.frameEvent = Frame(frameRoot, height='300', width='600', bg=self.colorFrameTitle, bd=5, relief='raised');
        self.frameEvent.place(x=50, y=50);
        self.frameEvent1 = Frame(frameRoot, height='300', width='600', bg=self.colorFrameTitle, bd=5, relief='raised');
        self.frameEvent1.place(x=700, y=50);
        # flat, groove, raised, ridge, solid, or sunken

    def datosEditar(self):
        self.regCeduVe.set(self.regCeduV);
        self.regNomVe.set(self.regNomV);
        self.regApeVe.set(self.regApeV);
        self.regFechaVe.set(self.regFechaV);
        self.regUserVe.set(self.regUserV);
        self.regTelfVe.set(self.regTelfV);
        self.regMailVe.set(self.regMailV);
        self.regPass1Ve.set(self.regPass1V);

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
        # Frame
        self.frameDatos = Frame(Root, height='800', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameDatos.pack(fill='x');
        # Labels
        self.tituloDatos = Label(self.frameDatos, text="INFORMACIÓN DE USUARIO", fg=self.fgColorW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 20));
        self.codigoDatosA = Label(self.frameDatos, text="Código: ", fg=self.fgColorW, bg=self.colorFrameTitle,
                                 font=(self.fontOCR, 14));
        self.codigoDatosB = Label(self.frameDatos, text=self.contCodeP, fg=self.fgColorW, bg=self.colorFrameTitle,
                                  font=(self.fontCali, 14));
        self.cedulaDatos = Label(self.frameDatos, text="Cédula:", fg=self.fgColorW,
                                 bg=self.colorFrameTitle, font=(self.fontOCR, 14));
        self.nombreDatos = Label(self.frameDatos, text="Nombre:", fg=self.fgColorW, bg=self.colorFrameTitle,
                                 font=(self.fontOCR, 14));
        self.apellidoDatos = Label(self.frameDatos, text="Apellido:", fg=self.fgColorW, bg=self.colorFrameTitle,
                                   font=(self.fontOCR, 14));
        self.fechaDatos = Label(self.frameDatos, text="Fecha de Nacimiento:", fg=self.fgColorW, bg=self.colorFrameTitle,
                                font=(self.fontOCR, 14));
        self.userDatos = Label(self.frameDatos, text="Nombre de Usuario:", fg=self.fgColorW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.telfDatos = Label(self.frameDatos, text="Teléfono:", fg=self.fgColorW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.mailDatos = Label(self.frameDatos, text="Correo Electrónico:", fg=self.fgColorW, bg=self.colorFrameTitle,
                               font=(self.fontOCR, 14));
        self.passDatos = Label(self.frameDatos, text="Contraseña:", fg=self.fgColorW, bg=self.colorFrameTitle,
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
        self.entryCedu = Entry(self.frameDatos, font=(self.fontCali, 12), textvariable=self.regCeduVe);
        self.entryCedu.place(x=150, y=120, width=150);
        self.regCeduV.trace("w", lambda *args: self.limitador(self.regCeduVe));
        self.entryNom = Entry(self.frameDatos, font=(self.fontCali, 11), textvariable=self.regNomVe);
        self.entryNom.place(x=150, y=160, width=300);
        self.entryApe = Entry(self.frameDatos, font=(self.fontCali, 11), textvariable=self.regApeVe);
        self.entryApe.place(x=630, y=160, width=300);
        self.entryFNacim = Entry(self.frameDatos, font=(self.fontCali, 12), textvariable=self.regFechaVe);
        self.entryFNacim.place(x=630, y=200, width=150);
        self.entryNick = Entry(self.frameDatos, font=(self.fontCali, 12), textvariable=self.regUserVe);
        self.entryNick.place(x=280, y=280, width=150);
        self.entryTelf = Entry(self.frameDatos, font=(self.fontCali, 12), textvariable=self.regTelfVe);
        self.entryTelf.place(x=170, y=200, width=170);
        self.regTelfV.trace("w", lambda *args: self.limitador(self.regTelfV));
        self.entryMail = Entry(self.frameDatos, font=(self.fontCali, 11), textvariable=self.regMailVe);
        self.entryMail.place(x=280, y=240, width=350);
        self.entryPassA = Entry(self.frameDatos, show="*", font=(self.fontCali, 12), textvariable=self.regPass1Ve);
        self.entryPassA.place(x=630, y=280, width=150);

    def ventInicio(self):  # Inicio, Eventos, Datos
        self.ventInicioR = Tk();
        self.ventInicioR.title("Principal");  # Da título a la ventana
        self.ventInicioR.state('zoomed');  # Inicializa la veentana maximizada
        self.ventInicioR.iconbitmap("Recursos\corpcitico.ico");  # Inserta icono a la app
        self.ventInicioR.resizable(0, 0);
        # Recursos
        imgLogo = PhotoImage(file="Recursos\corpciti.png");  # Inserto Imagen
        imgWeb = PhotoImage(file="Recursos\web.png");
        self.colorFrameTitle = "gray";  # Color establecido para el frame título
        # Frames
        # Ventana Principal
        self.frameTitle = Frame(self.ventInicioR, height='105', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameTitle.pack(fill='x', expand=False);  # Ajusta el frame a la ventana(ventInicio)
        # Frame de Opciones
        self.frameOption = Frame(self.ventInicioR, height='50', background=self.colorCorp, bd=5);
        self.frameOption.pack(fill='x');
        # Frame Inicio
        self.frameHome = Frame(self.ventInicioR, height='800', bg=self.colorFrameTitle, bd=5, relief='groove');
        self.frameHome.pack(fill='x');
        self.fFrameEvento(self.frameHome);
        # Crear los elementos
        # Crear Labels y botón
        self.imagenLogo = ttk.Label(self.frameTitle, image=imgLogo, anchor="center");
        self.labelTitulo = ttk.Label(self.frameTitle,
                                     text="Corporación de Ciencia\nTecnología e Innovación del Ecuador",
                                     foreground=self.fgColorW, background=self.colorFrameTitle,
                                     font=("Imprint MT Shadow", 26),
                                     justify=CENTER);
        self.saludoEntidad = Label(self.frameOption, text="¡BIENVENIDO!",
                                   foreground=self.fgColorW, background=self.colorCorp,
                                   font=(self.fontOCR, 18),
                                   justify=CENTER);
        # Inserta y configura Labels
        self.imagenLogo.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.labelTitulo.pack(side=TOP, expand=False, padx=330, pady=0);
        self.saludoEntidad.pack(side=LEFT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        # Crea Botones
        self.botonPagMain = ttk.Button(self.frameTitle, image=imgWeb, command=self.web, cursor=self.cursorBot);
        self.botonIniUser = Button(self.frameOption, text="Inicio", font=(self.fontOCR, 12),
                                   foreground=self.fgColorW, background=self.colorCorp, relief="flat",
                                   cursor=self.cursorBot, command=lambda: [self.cambiaFrame(self.fFrameDatosU(self.ventInicioR))]);
        self.botonMiEvents = Button(self.frameOption, text="Mis Eventos", font=(self.fontOCR, 12),
                                    foreground=self.fgColorW, background=self.colorCorp, relief="flat",
                                    cursor=self.cursorBot);
        self.botonMiDato = Button(self.frameOption, text="Mis Datos", font=(self.fontOCR, 12), fg=self.fgColorW,
                                  background=self.colorCorp, relief="flat", cursor=self.cursorBot,
                                  command=lambda: [self.datosEditar(), self.fFrameDatosU(self.ventInicioR), self.cambiaFrame(self.frameHome)]);
        self.botonIniSalir = Button(self.frameOption, text="Cerrar Sesión", font=(self.fontOCR, 12),
                                    foreground=self.fgColorW, background=self.colorCorp, relief="flat",
                                    cursor=self.cursorBot);  # lambda: [self.ventInicio(self.user)]
        # Inserta Botones
        self.botonPagMain.pack(side=RIGHT, expand=False, padx=0, pady=0, ipadx=0, ipady=0);
        self.botonIniSalir.pack(side=RIGHT, expand=False, padx=20, pady=0, ipadx=0, ipady=0);
        self.botonMiDato.pack(side=RIGHT, expand=False, padx=30, pady=0, ipadx=0, ipady=0);
        self.botonMiEvents.pack(side=RIGHT, expand=False, padx=40, pady=0, ipadx=0, ipady=0);
        self.botonIniUser.pack(side=RIGHT, expand=False, padx=50, pady=0, ipadx=0, ipady=0);
        self.ventInicioR.mainloop();

    def ventInicioU(self):
        self.ventInicio();

    def ventInicioA(self):
        pass;

def main():
    mi_app = Ventana();
    return 0;


if __name__ == '__main__':
    main();
# ventInicio.resizable(1,1);#Ventana se puede redimensionar
# def validaEntry(event):
#    if all(c in "|°!#$%&/()=?¡¿'´¨*+}][{-_.:,;-+" for c in event.widget.get()):
#        label_var.set("Ingresa sólo letras o números")
# else: label_var.set("CORRECTO");
# entry1 = Entry(ventInicio)
# entry1.bind("<FocusOut>", validaEntry);
# Entry(ventInicio).pack(side=BOTTOM);
# entry1.pack(side=LEFT);
# label_var = StringVar();
# val_label = Label(ventInicio, textvariable=label_var).pack(side=LEFT);
# ventInicio.mainloop();
Re.listataUser(0);
#Re.listataAdm();