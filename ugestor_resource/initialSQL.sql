
CREATE DATABASE ugestor
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;
CREATE SCHEMA ugestorapp
  AUTHORIZATION postgres;


create table ugestorapp.persona (
	id int,
	cedula int,
	nombre varchar(255),
	apellido  varchar(255),
	paisorigen varchar(255),
	fechaNacimiento Date,
	sexo varchar(25),
	tipoDocumento varchar(15));
	create table ugestorapp.agencia(
	id int,
	nombre varchar(255),
	anocreacion Date,
	sedeproncipal varchar(255),
	idPersona int,
	correoElectronico varchar(255),
	relacionesOtrasAgencias varchar(255),
	CodAgencia varchar(255));

--create table ugestorapp.disenador (--
--id int,
--nombre varchar(255),
--fechainicio Date,
--fechafin Date,
--iddisenador int);
--ALTER USER postgres WITH ENCRYPTED PASSWORD 'xxxxxxx';
create table ugestorapp.modelo (
idModelo int,
colorojosModelo varchar(255),
colorpielModelo varchar(255),
estaturaModelo int,
cinturaModelo int,
bustoModelo int,
tallapiesModelo int,
pesoModelo int,
fechaHistoricoModelo Date,
idPersona int);

create table ugestorapp.Artista(
idArtista int,
nombreArtistico varchar(255),
generoMusical varchar(255),
tipoArtista varchar(255),
idPersona int
);
create table ugestorapp.Disenador(
idDisenador int,
pasaporteDisenador varchar(255),
paisOrigenDisenador varchar(255),
idPersona int
);
create table ugestorapp.Empleadorazo(
idEmpleadorazo int

);
create table ugestorapp.Profesional(
idProfesional int,
EgresadoUniversidadProfesional varchar(255),
estudiosProfesional varchar(255),
idPersona int
);
create table ugestorapp.Empleado (
idEmpleado int ,
fechaIngresoEmpleado varchar(255),
cargoEmpleado varchar(255),
salarioEmpleado varchar(255),
idPersona int
);
