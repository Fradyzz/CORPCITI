USE master;
DROP DATABASE corpciti;
DROP DATABASE IF EXISTS corpciti;
CREATE DATABASE corpciti;
USE corpciti;

CREATE TABLE usuario(codigo INT IDENTITY(1,1) PRIMARY KEY, cedula VARCHAR(100) NOT NULL,
					 nombre VARCHAR(100) NOT NULL, apellido VARCHAR(100) NOT NULL,
					 fechanacim VARCHAR(30) NOT NULL, nick VARCHAR(100) NOT NULL, 
					 telefono VARCHAR(30) NOT NULL, email VARCHAR(100) NOT NULL, 
					 contrasena VARCHAR(100) NOT NULL);

CREATE TABLE administrador(codigo INT PRIMARY KEY, cedula VARCHAR(100) NOT NULL,
					 nombre VARCHAR(100) NOT NULL, apellido VARCHAR(100) NOT NULL,
					 fechanacim VARCHAR(30) NOT NULL, nick VARCHAR(100) NOT NULL, 
					 telefono VARCHAR(30) NOT NULL, email VARCHAR(100) NOT NULL, 
					 contrasena VARCHAR(100) NOT NULL);

CREATE TABLE evento(codigo INT IDENTITY(1,1) PRIMARY KEY, nombre VARCHAR(100) NOT NULL,
					descripcion VARCHAR(300) NOT NULL, lugar VARCHAR(100) NOT NULL,
					fecha VARCHAR(30) NOT NULL, hora VARCHAR(10) NOT NULL, boletos INT NOT NULL,
					codigo_admin INT NOT NULL,
					FOREIGN KEY (codigo_admin) REFERENCES administrador(codigo));

CREATE TABLE enlista(codigo INT IDENTITY(1,1) PRIMARY KEY, codigo_usuario INT NOT NULL,
                     codigo_evento INT NOT NULL,
                     FOREIGN KEY (codigo_usuario) REFERENCES usuario(codigo),
					 FOREIGN KEY (codigo_evento) REFERENCES evento(codigo));

INSERT INTO administrador VALUES ('', '', '', '', '', '', '', '');
INSERT INTO administrador VALUES (1130, '', '', '', '', '', '', '', '');

DELETE FROM usuario WHERE codigo=1 OR codigo=2;
DELETE FROM administrador WHERE codigo=1154;

SELECT * FROM usuario;
SELECT * FROM administrador;
SELECT * FROM evento;
SELECT * FROM enlista;