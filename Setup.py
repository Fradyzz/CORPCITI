from distutils.core import setup;
import py2exe;

setup(name="CORPCITI",
      version="1.0",
      description="Software que maneja eventos",
      author="Bradog",
      author_email="fradyzz@hotmail.com",
      url="N/A",
      license="N/A",
      scripts=["Interfaz","Clases.py", "Conexion", "Repositorio"],
               console = ["Interfaz","Clases.py", "Conexion", "Repositorio"],
                          options = {"py2exe": {"bundle_files": 4}},
                                    zipfile = None);