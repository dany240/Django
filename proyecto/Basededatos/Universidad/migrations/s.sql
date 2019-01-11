--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5 (Debian 10.5-1.pgdg90+1)
-- Dumped by pg_dump version 10.5 (Debian 10.5-1.pgdg90+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Universidad_docentes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Universidad_docentes" (
    cedula integer NOT NULL,
    nombre_doc character varying(128) NOT NULL
);


ALTER TABLE public."Universidad_docentes" OWNER TO postgres;

--
-- Name: Universidad_estudiante; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Universidad_estudiante" (
    cod_estudio integer NOT NULL,
    nombre_est character varying(128) NOT NULL,
    "Apellido_est" character varying(128) NOT NULL,
    quesemestre integer NOT NULL
);


ALTER TABLE public."Universidad_estudiante" OWNER TO postgres;

--
-- Name: Universidad_semestre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Universidad_semestre" (
    periodo integer NOT NULL,
    ano integer NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public."Universidad_semestre" OWNER TO postgres;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO postgres;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO postgres;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO postgres;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO postgres;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO postgres;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO postgres;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: bitacora; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bitacora (
    id_evento integer NOT NULL,
    tabla character varying(30) NOT NULL,
    evento character varying(2550) NOT NULL
);


ALTER TABLE public.bitacora OWNER TO postgres;

--
-- Name: bitacora_id_evento_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bitacora_id_evento_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bitacora_id_evento_seq OWNER TO postgres;

--
-- Name: bitacora_id_evento_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bitacora_id_evento_seq OWNED BY public.bitacora.id_evento;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO postgres;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO postgres;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO postgres;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO postgres;

--
-- Name: docentes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.docentes (
    cedula bigint NOT NULL,
    nombre_doc character varying(45) NOT NULL,
    apellido_doc character varying(45) NOT NULL,
    "contraseña" character varying(45) NOT NULL,
    celular numeric(10,0) DEFAULT NULL::numeric
);


ALTER TABLE public.docentes OWNER TO postgres;

--
-- Name: docentes_en_semestre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.docentes_en_semestre (
    id_semestre integer NOT NULL,
    cedula_doc bigint NOT NULL,
    id bigint
);


ALTER TABLE public.docentes_en_semestre OWNER TO postgres;

--
-- Name: indiceestudiante; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.indiceestudiante
    START WITH 0
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.indiceestudiante OWNER TO postgres;

--
-- Name: estudiante; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estudiante (
    cod_estudio integer DEFAULT nextval('public.indiceestudiante'::regclass) NOT NULL,
    nombre_est character varying(45),
    apellido_est character varying(45),
    quesemestre integer
);


ALTER TABLE public.estudiante OWNER TO postgres;

--
-- Name: estudianteysemestre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.estudianteysemestre (
    id_semestre integer NOT NULL,
    cod_estudio integer NOT NULL,
    id bigint
);


ALTER TABLE public.estudianteysemestre OWNER TO postgres;

--
-- Name: idestudiantes; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.idestudiantes
    START WITH 1
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.idestudiantes OWNER TO postgres;

--
-- Name: idestudiantes; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.idestudiantes OWNED BY public.estudiante.cod_estudio;


--
-- Name: semestre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.semestre (
    periodo integer NOT NULL,
    "año" integer NOT NULL,
    id_semestre integer NOT NULL,
    novedades character varying(45)
);


ALTER TABLE public.semestre OWNER TO postgres;

--
-- Name: se_materia; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.se_materia
    START WITH 2010
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.se_materia OWNER TO postgres;

--
-- Name: se_materia; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.se_materia OWNED BY public.semestre."año";


--
-- Name: materia; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.materia (
    cod_materia integer DEFAULT nextval('public.se_materia'::regclass) NOT NULL,
    nombre_materia character varying(45) NOT NULL,
    creditos integer NOT NULL,
    semestre_id integer NOT NULL,
    activo boolean DEFAULT true NOT NULL
);


ALTER TABLE public.materia OWNER TO postgres;

--
-- Name: materiayestudiantes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.materiayestudiantes (
    cod_materia integer NOT NULL,
    cod_estudio integer NOT NULL,
    id_semestre integer NOT NULL,
    registro integer NOT NULL
);


ALTER TABLE public.materiayestudiantes OWNER TO postgres;

--
-- Name: materiayestudiantes_registro_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.materiayestudiantes_registro_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.materiayestudiantes_registro_seq OWNER TO postgres;

--
-- Name: materiayestudiantes_registro_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.materiayestudiantes_registro_seq OWNED BY public.materiayestudiantes.registro;


--
-- Name: notas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.notas (
    tipodenota character varying(75),
    notas integer,
    cod_materia integer,
    cod_estudio integer,
    id_semestre integer,
    cedula_doc integer,
    porcentaje numeric(3,2),
    id bigint NOT NULL
);


ALTER TABLE public.notas OWNER TO postgres;

--
-- Name: notas_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.notas_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.notas_id_seq OWNER TO postgres;

--
-- Name: notas_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.notas_id_seq OWNED BY public.notas.id;


--
-- Name: se_año; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."se_año"
    START WITH 2010
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."se_año" OWNER TO postgres;

--
-- Name: se_año; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."se_año" OWNED BY public.semestre."año";


--
-- Name: se_id_semestre; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.se_id_semestre
    START WITH 0
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.se_id_semestre OWNER TO postgres;

--
-- Name: se_id_semestre; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.se_id_semestre OWNED BY public.semestre.id_semestre;


--
-- Name: se_materiayestudiantes; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.se_materiayestudiantes
    START WITH 189
    INCREMENT BY 1
    MINVALUE 0
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.se_materiayestudiantes OWNER TO postgres;

--
-- Name: se_materiayestudiantes; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.se_materiayestudiantes OWNED BY public.semestre."año";


--
-- Name: se_periodo; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.se_periodo
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2
    CACHE 1
    CYCLE;


ALTER TABLE public.se_periodo OWNER TO postgres;

--
-- Name: se_periodo; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.se_periodo OWNED BY public.semestre.periodo;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: bitacora id_evento; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bitacora ALTER COLUMN id_evento SET DEFAULT nextval('public.bitacora_id_evento_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: materiayestudiantes registro; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.materiayestudiantes ALTER COLUMN registro SET DEFAULT nextval('public.materiayestudiantes_registro_seq'::regclass);


--
-- Name: notas id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notas ALTER COLUMN id SET DEFAULT nextval('public.notas_id_seq'::regclass);


--
-- Name: semestre periodo; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.semestre ALTER COLUMN periodo SET DEFAULT nextval('public.se_periodo'::regclass);


--
-- Name: semestre año; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.semestre ALTER COLUMN "año" SET DEFAULT nextval('public."se_año"'::regclass);


--
-- Name: semestre id_semestre; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.semestre ALTER COLUMN id_semestre SET DEFAULT nextval('public.se_id_semestre'::regclass);


--
-- Data for Name: Universidad_docentes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Universidad_docentes" (cedula, nombre_doc) FROM stdin;
\.


--
-- Data for Name: Universidad_estudiante; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Universidad_estudiante" (cod_estudio, nombre_est, "Apellido_est", quesemestre) FROM stdin;
\.


--
-- Data for Name: Universidad_semestre; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Universidad_semestre" (periodo, ano, id) FROM stdin;
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group (id, name) FROM stdin;
1	Docentes
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
1	1	25
2	1	26
3	1	27
4	1	28
5	1	29
6	1	30
7	1	31
8	1	32
9	1	33
10	1	34
11	1	35
12	1	36
13	1	37
14	1	38
15	1	39
16	1	40
17	1	41
18	1	42
19	1	43
20	1	44
21	1	45
22	1	46
23	1	47
24	1	48
25	1	49
26	1	50
27	1	51
28	1	52
29	1	53
30	1	54
31	1	55
32	1	56
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add group	2	add_group
6	Can change group	2	change_group
7	Can delete group	2	delete_group
8	Can view group	2	view_group
9	Can add permission	3	add_permission
10	Can change permission	3	change_permission
11	Can delete permission	3	delete_permission
12	Can view permission	3	view_permission
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add materiayestudiantes	7	add_materiayestudiantes
26	Can change materiayestudiantes	7	change_materiayestudiantes
27	Can delete materiayestudiantes	7	delete_materiayestudiantes
28	Can view materiayestudiantes	7	view_materiayestudiantes
29	Can add estudiante	8	add_estudiante
30	Can change estudiante	8	change_estudiante
31	Can delete estudiante	8	delete_estudiante
32	Can view estudiante	8	view_estudiante
33	Can add docentes	9	add_docentes
34	Can change docentes	9	change_docentes
35	Can delete docentes	9	delete_docentes
36	Can view docentes	9	view_docentes
37	Can add semestre	10	add_semestre
38	Can change semestre	10	change_semestre
39	Can delete semestre	10	delete_semestre
40	Can view semestre	10	view_semestre
41	Can add notas	11	add_notas
42	Can change notas	11	change_notas
43	Can delete notas	11	delete_notas
44	Can view notas	11	view_notas
45	Can add docentes en semestre	12	add_docentesensemestre
46	Can change docentes en semestre	12	change_docentesensemestre
47	Can delete docentes en semestre	12	delete_docentesensemestre
48	Can view docentes en semestre	12	view_docentesensemestre
49	Can add materia	13	add_materia
50	Can change materia	13	change_materia
51	Can delete materia	13	delete_materia
52	Can view materia	13	view_materia
53	Can add estudianteysemestre	14	add_estudianteysemestre
54	Can change estudianteysemestre	14	change_estudianteysemestre
55	Can delete estudianteysemestre	14	delete_estudianteysemestre
56	Can view estudianteysemestre	14	view_estudianteysemestre
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$120000$7fUfKfyF6B8B$xOmEa5Q5gFEUOheJQ10YqzkpySLqCIQQD21bRsQxmgo=	2018-11-21 02:11:51.668478-05	t	das24081999			solrevisdor143@gmail.com	t	t	2018-11-05 14:08:05.958935-05
2	pbkdf2_sha256$120000$WkGA7svwN2gi$scoB2b5FPMX934JT88/iA2QTTdWrztfiR5qqhuQnX0Q=	\N	f	1338940332				f	t	2018-11-26 20:52:03.682107-05
3	pbkdf2_sha256$120000$Ef02QQzmSwuq$i86KHQVCDXKHSETOG1azuojKVhQkKvhlYeQAN85b7vs=	\N	f	1343436533				f	t	2018-11-26 21:32:25.294951-05
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: bitacora; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bitacora (id_evento, tabla, evento) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2018-11-06 15:02:41.484576-05	4	Materia object (4)	1	[{"added": {}}]	13	1
2	2018-11-06 15:12:10.918404-05	1121965790	Docentes object (1121965790)	1	[{"added": {}}]	9	1
3	2018-11-06 15:12:29.724671-05	1	Docentes object (1)	3		9	1
4	2018-11-21 02:13:47.071903-05	1	Docentes	1	[{"added": {}}]	2	1
5	2018-11-26 22:18:57.490881-05	1343436533	Docentes object (1343436533)	2	[{"changed": {"fields": ["nombre_doc", "apellido_doc"]}}]	9	1
6	2018-11-26 22:33:45.731588-05	458	Año: 2453 Semestre:458 Periodo:-2 Novedad:Sin Novedades	1	[{"added": {}}]	10	1
7	2018-11-26 22:33:57.071477-05	458	Año: 2453 Semestre:458 Periodo:-2 Novedad:Sin Novedades	3		10	1
8	2018-11-26 22:34:56.038326-05	458	Año: 2012 Semestre:458 Periodo:2 Novedad:Sin Novedades	1	[{"added": {}}]	10	1
9	2018-11-26 22:35:10.545423-05	458	Año: 2012 Semestre:458 Periodo:1 Novedad:Sin Novedades	2	[{"changed": {"fields": ["periodo"]}}]	10	1
10	2018-11-26 22:39:32.450824-05	462	Año: 2012 Semestre:462 Periodo:2 Novedad:Sin Novedades	1	[{"added": {}}]	10	1
11	2018-11-27 22:55:16.743164-05	47	Año: 2018 Semestre:47 Periodo:2 Novedad:Sin novedad	1	[{"added": {}}]	10	1
12	2018-11-27 23:08:07.979872-05	50	Año: 2019 -- Semestre:1 -- Novedad: Sin novedad	1	[{"added": {}}]	10	1
13	2018-11-27 23:09:21.613011-05	50	Año: 2019 -- Semestre:2 -- Novedad: Sin novedad	1	[{"added": {}}]	10	1
14	2018-11-27 23:09:43.079813-05	50	Año: 2019 -- Semestre:1 -- Novedad: Sin novedad	1	[{"added": {}}]	10	1
15	2018-11-27 23:10:21.470856-05	50	Año: 2017 -- Semestre:2 -- Novedad: Sin novedad	1	[{"added": {}}]	10	1
16	2018-11-27 23:11:03.965835-05	50	Año: 2019 -- Semestre:1 -- Novedad: Semestre Canselado	1	[{"added": {}}]	10	1
17	2018-11-27 23:11:16.867392-05	50	Año: 2019 -- Semestre:1 -- Novedad: Semestre Canselado	2	[]	10	1
18	2018-11-27 23:11:21.923695-05	50	Año: 2494 -- Semestre:1 -- Novedad: Sin novedad	1	[{"added": {}}]	10	1
19	2018-11-27 23:13:28.803861-05	50	Año: 2018 -- Semestre:1 -- Novedad: Sin novedad	1	[{"added": {}}]	10	1
20	2018-11-27 23:23:29.782896-05	53	semestre id= 53,Año: 2000 -- Semestre:1 -- Novedad: Sin novedad	1	[{"added": {}}]	10	1
21	2018-11-27 23:23:51.684969-05	53	semestre id= 53,Año: 2001 -- Semestre:2 -- Novedad: Sin novedad	1	[{"added": {}}]	10	1
22	2018-11-28 02:32:23.4718-05	47	CodigoEstudiante  484 nombreEstudiante  fabio ApellidoEstudiante  raul Semestre_cursando  1 semestre id= 47,Año: 2018 -- Semestre:2 -- Novedad: Sin novedad	1	[{"added": {}}]	14	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	group
3	auth	permission
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	Universidad	materiayestudiantes
8	Universidad	estudiante
9	Universidad	docentes
10	Universidad	semestre
11	Universidad	notas
12	Universidad	docentesensemestre
13	Universidad	materia
14	Universidad	estudianteysemestre
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	Universidad	0001_initial	2018-11-05 14:04:22.4052-05
2	Universidad	0002_auto_20181105_1237	2018-11-05 14:04:22.498796-05
3	contenttypes	0001_initial	2018-11-05 14:04:22.650106-05
4	auth	0001_initial	2018-11-05 14:04:23.656995-05
5	admin	0001_initial	2018-11-05 14:04:23.914527-05
6	admin	0002_logentry_remove_auto_add	2018-11-05 14:04:24.053424-05
7	admin	0003_logentry_add_action_flag_choices	2018-11-05 14:04:24.077985-05
8	contenttypes	0002_remove_content_type_name	2018-11-05 14:04:24.131431-05
9	auth	0002_alter_permission_name_max_length	2018-11-05 14:04:24.164732-05
10	auth	0003_alter_user_email_max_length	2018-11-05 14:04:24.186579-05
11	auth	0004_alter_user_username_opts	2018-11-05 14:04:24.222089-05
12	auth	0005_alter_user_last_login_null	2018-11-05 14:04:24.253343-05
13	auth	0006_require_contenttypes_0002	2018-11-05 14:04:24.269406-05
14	auth	0007_alter_validators_add_error_messages	2018-11-05 14:04:24.328481-05
15	auth	0008_alter_user_username_max_length	2018-11-05 14:04:24.398121-05
16	auth	0009_alter_user_last_name_max_length	2018-11-05 14:04:24.420283-05
17	sessions	0001_initial	2018-11-05 14:04:24.622653-05
18	Universidad	0003_auto_20181230_2206	2018-12-30 22:07:04.953969-05
19	Universidad	0004_auto_20190110_1032	2019-01-10 10:34:02.801114-05
20	Universidad	0005_auto_20190110_1637	2019-01-10 16:37:27.547705-05
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
\.


--
-- Data for Name: docentes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.docentes (cedula, nombre_doc, apellido_doc, "contraseña", celular) FROM stdin;
11219657901	Julian	Perez	1234	3118022985
1121969790	Julian Rios	Perez NUñez	Julio	3118022985
1121965790	Julian Rios	Perez Nuñez	Jose	3118022985
1219657901	Ramirez leon	Perez	kalos	3118022985
\.


--
-- Data for Name: docentes_en_semestre; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.docentes_en_semestre (id_semestre, cedula_doc, id) FROM stdin;
47	1121965790	\N
51	1121969790	\N
50	11219657901	\N
53	1219657901	\N
\.


--
-- Data for Name: estudiante; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estudiante (cod_estudio, nombre_est, apellido_est, quesemestre) FROM stdin;
484	fabio	raul	1
695	Luis	carlo	1
\.


--
-- Data for Name: estudianteysemestre; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.estudianteysemestre (id_semestre, cod_estudio, id) FROM stdin;
47	484	\N
51	695	\N
\.


--
-- Data for Name: materia; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.materia (cod_materia, nombre_materia, creditos, semestre_id, activo) FROM stdin;
2485	el arroz	4	4	t
\.


--
-- Data for Name: materiayestudiantes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.materiayestudiantes (cod_materia, cod_estudio, id_semestre, registro) FROM stdin;
2485	484	47	1
\.


--
-- Data for Name: notas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.notas (tipodenota, notas, cod_materia, cod_estudio, id_semestre, cedula_doc, porcentaje, id) FROM stdin;
\.


--
-- Data for Name: semestre; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.semestre (periodo, "año", id_semestre, novedades) FROM stdin;
2	2018	47	Sin novedad
1	2019	51	Sin novedad
1	2018	50	Sin novedad
2	2001	53	Sin novedad
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 32, true);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 56, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 3, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: bitacora_id_evento_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bitacora_id_evento_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 22, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 14, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 20, true);


--
-- Name: idestudiantes; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.idestudiantes', 1, false);


--
-- Name: indiceestudiante; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.indiceestudiante', 1396, true);


--
-- Name: materiayestudiantes_registro_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.materiayestudiantes_registro_seq', 5, true);


--
-- Name: notas_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.notas_id_seq', 4, true);


--
-- Name: se_año; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."se_año"', 3427, true);


--
-- Name: se_id_semestre; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.se_id_semestre', 984, true);


--
-- Name: se_materia; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.se_materia', 3403, true);


--
-- Name: se_materiayestudiantes; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.se_materiayestudiantes', 189, false);


--
-- Name: se_periodo; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.se_periodo', 2, true);


--
-- Name: Universidad_docentes Universidad_docentes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Universidad_docentes"
    ADD CONSTRAINT "Universidad_docentes_pkey" PRIMARY KEY (cedula);


--
-- Name: Universidad_estudiante Universidad_estudiante_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Universidad_estudiante"
    ADD CONSTRAINT "Universidad_estudiante_pkey" PRIMARY KEY (cod_estudio);


--
-- Name: Universidad_semestre Universidad_semestre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Universidad_semestre"
    ADD CONSTRAINT "Universidad_semestre_pkey" PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: bitacora bitacora_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bitacora
    ADD CONSTRAINT bitacora_pkey PRIMARY KEY (id_evento);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: docentes_en_semestre docentes_en_semestre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.docentes_en_semestre
    ADD CONSTRAINT docentes_en_semestre_pkey PRIMARY KEY (id_semestre, cedula_doc);


--
-- Name: docentes docentes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.docentes
    ADD CONSTRAINT docentes_pkey PRIMARY KEY (cedula);


--
-- Name: estudiante estudiante_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estudiante
    ADD CONSTRAINT estudiante_pkey PRIMARY KEY (cod_estudio);


--
-- Name: estudianteysemestre estudianteysemestre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estudianteysemestre
    ADD CONSTRAINT estudianteysemestre_pkey PRIMARY KEY (id_semestre, cod_estudio);


--
-- Name: materia materia_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.materia
    ADD CONSTRAINT materia_pkey PRIMARY KEY (cod_materia);


--
-- Name: materiayestudiantes materiayestudiantes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.materiayestudiantes
    ADD CONSTRAINT materiayestudiantes_pkey PRIMARY KEY (cod_estudio, id_semestre, cod_materia);


--
-- Name: semestre semestre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.semestre
    ADD CONSTRAINT semestre_pkey PRIMARY KEY (id_semestre);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: docentes_en_semestre doc_semes; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.docentes_en_semestre
    ADD CONSTRAINT doc_semes FOREIGN KEY (id_semestre) REFERENCES public.semestre(id_semestre) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: docentes_en_semestre doc_semes1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.docentes_en_semestre
    ADD CONSTRAINT doc_semes1 FOREIGN KEY (cedula_doc) REFERENCES public.docentes(cedula) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: materiayestudiantes materiayestudiantes1_mat; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.materiayestudiantes
    ADD CONSTRAINT materiayestudiantes1_mat FOREIGN KEY (cod_materia) REFERENCES public.materia(cod_materia) ON UPDATE CASCADE ON DELETE RESTRICT;


--
-- Name: materiayestudiantes materiayestudiantes1_seme; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.materiayestudiantes
    ADD CONSTRAINT materiayestudiantes1_seme FOREIGN KEY (id_semestre, cod_estudio) REFERENCES public.estudianteysemestre(id_semestre, cod_estudio) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: estudianteysemestre materiayestudiantes_est; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estudianteysemestre
    ADD CONSTRAINT materiayestudiantes_est FOREIGN KEY (cod_estudio) REFERENCES public.estudiante(cod_estudio) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: estudianteysemestre materiayestudiantes_seme; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.estudianteysemestre
    ADD CONSTRAINT materiayestudiantes_seme FOREIGN KEY (id_semestre) REFERENCES public.semestre(id_semestre) ON UPDATE RESTRICT ON DELETE RESTRICT;


--
-- Name: notas materiayestudiantesnotas; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notas
    ADD CONSTRAINT materiayestudiantesnotas FOREIGN KEY (id_semestre, cod_materia, cod_estudio) REFERENCES public.materiayestudiantes(id_semestre, cod_materia, cod_estudio) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: notas notas_docentes; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.notas
    ADD CONSTRAINT notas_docentes FOREIGN KEY (id_semestre, cedula_doc) REFERENCES public.docentes_en_semestre(id_semestre, cedula_doc) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

