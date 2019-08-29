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

create table ugestorapp (
	id int,
	nombre varchar(255),
	fechainicio Date,
	fechafin Date,
	iddisenador int);

	create table ugestorapp.modelo (
		idModelo int,
		colorojosModelo varchar(255),
    colorpielModelo varchar(255),
    estaturaModelo int
    cinturaModelo int,
	  bustoModelo int,
    tallapiesModelo int,
    pesoModelo int,
	  fechaHistoricoModelo Date,
	  idPersona);

		create table ugestorapp.Artista(
      idArtista int
     nombreArtistico varchar(255),
     generoMusical varchar(255),
     tipoArtista varchar(255)
		)
		create table ugestorapp.Disenador(
			idDisenador int
		 pasaporteDisenador varchar(255),
		 paisOrigenDisenador varchar(255)
		)
