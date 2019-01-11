
create table docentes (
	cedula int ,
	nombre_doc  varchar(45),
	Apellido_doc varchar(45),
	celular  decimal(10,0)
    contraseña  varchar(45),
		);
ALTER TABLE docentes alter column nombre_doc set NOT NULL;
ALTER TABLE docentes alter column Apellido_docset NOT NULL;
ALTER TABLE docentes alter column contraseña set NOT NULL; 
alter table docentes add constraint docentes_pkey  primary key (cedula) ;

create table semestre(
    periodo int ,
    año  int,
    id_semestre int,
    novedades varchar(45),
    primary key(id_semestre)
	);
alter table semestre alter column periodo set not null;
alter table semestre alter column año set not null;
alter table semestre alter column periodo set not null;
create table estudiante (
   cod_estudio  int,
   nombre_est  varchar(45),
   Apellido_est varchar(45),
   quesemestre integer,
   primary key (cod_estudio)
	);
create sequence indiceEstudiante
   start with 0
  increment by 1
  minvalue 0
	;
CREATE SEQUENCE idEstudiantes  INCREMENT  BY 1
     MINVALUE 0 
     START 1   NO  CYCLE 
     OWNED BY  estudiante.cod_estudio; 

CREATE SEQUENCE se_id_semestre  INCREMENT  BY 1
     MINVALUE 0 
     START 0   NO  CYCLE 
     OWNED BY  semestre.id_semestre;
CREATE SEQUENCE se_periodo  INCREMENT  BY 1
     MINVALUE 1 
     MAXVALUE 2
     START 1     CYCLE 
     OWNED BY  semestre.periodo;
CREATE SEQUENCE se_año  INCREMENT  BY 1
     MINVALUE 0 
     START 2010  NO  CYCLE 
     OWNED BY  semestre.año;
alter table estudiante alter column cod_estudio set default nextval('indiceEstudiante') ;
alter table semestre alter column id_semestre set default nextval('se_id_semestre') ;
alter table semestre alter column año set default nextval('se_año') ;
alter table semestre alter column periodo set default nextval('se_periodo') ;


create table Docentes_en_semestre (
    id_semestre int,
    cedula_doc int ,
    primary key(id_semestre,cedula_doc),
    constraint doc_semes foreign key (id_semestre)references semestre(id_semestre) on delete restrict on update restrict,
    constraint doc_semes1 foreign key (cedula_doc) references docentes(cedula) on delete cascade on update cascade
	);

create table materia(
	cod_materia integer,
	nombre_materia varchar(45),
	Creditos integer,
	semestre_id integer,
	activo boolean,
	primary key(cod_materia),
	--constraint semestreymaterias foreign key (semestre_id) references semestre(id_semestre) on delete restrict on update cascade
 	);
alter table materia alter column cod_materia set not null;
alter table materia alter column nombre_materia set not null;
alter table materia alter column Creditos set not null;
alter table materia alter column semestre_id set not null;
alter table materia alter column activo set not null;
alter table materia alter column activo set default True;


CREATE SEQUENCE se_materia INCREMENT  BY 1
     MINVALUE 0 
     START 2010  NO  CYCLE 
     OWNED BY  semestre.año;
alter table materia alter column cod_materia set default nextval('se_materia') ;

create table estudianteYsemestre(
   id bigint,
    id_semestre integer,
    cod_estudio integer,
    primary key (id_semestre,cod_estudio),
   	constraint MateriaYEstudiantes_seme foreign key (id_semestre) references semestre(id_semestre) on delete restrict on update restrict,
  	constraint MateriaYEstudiantes_est foreign key (cod_estudio) references estudiante(cod_estudio)on delete cascade on update cascade
	);
create table MateriaYEstudiantes(
  registro bigint,
	cod_materia integer,
	cod_estudio integer,
	id_semestre integer,
primary key(id_semestre,cod_estudio,cod_materia),
constraint MateriaYEstudiantes1_seme foreign key (id_semestre,cod_estudio) references estudianteYsemestre(id_semestre,cod_estudio)on delete cascade on update cascade,
constraint MateriaYEstudiantes1_mat foreign key (cod_materia) references materia(cod_materia) on delete restrict on update cascade,
	);

create table notas(
tipodenota varchar(75),
notas integer,
cod_materia integer,
cod_estudio integer,
id_semestre integer,
cedula_doc int ,
id bigint,
porcentaje decimal(3,2),
primary key(id),
constraint MateriaYEstudiantesnotas foreign key  (id_semestre,cod_materia,cod_estudio) references MateriaYEstudiantes(id_semestre,cod_materia,cod_estudio) on delete cascade on update cascade,
constraint notas_docentes foreign key (id_semestre,cedula_doc) references Docentes_en_semestre(id_semestre,cedula_doc)  on delete cascade on update cascade);

create table bitacora(
  id_evento serial,
  Tabla varchar(30)  not null,
  Evento varchar(2550) not null,
  Usuario varchar(120),
  primary key(id_evento)
);

create or replace function Triguer()  returns trigger As$$


$$
LANGUAGE plpgsql;


create or replace function Semestre_en_Estudiante