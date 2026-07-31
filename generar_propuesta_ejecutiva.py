# -*- coding: utf-8 -*-
"""Propuesta visual Observatorio CTi: compacta, flujo full-width, KPIs + MVP."""
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent

def fmt_cop(n):
    return f"${n:,.0f}".replace(",", ".")

# Flujo compacto (cabe completo en viewport)
FLOW = [
    {"id": "demanda", "n": 1, "titulo": "Demanda", "fase": "Entrada", "x": 20, "y": 150, "w": 100, "h": 56, "tipo": "entrada",
     "proceso": "Priorizar necesidades de información del CMA.",
     "actividades": ["Recibir solicitudes", "Priorizar estudios", "Alinear con CEITTO"],
     "entradas": "Solicitudes institucionales", "salidas": "Alcance priorizado",
     "responsable": "Analista de datos · área solicitante"},
    {"id": "fuentes", "n": 2, "titulo": "Fuentes", "fase": "Captura", "x": 150, "y": 50, "w": 100, "h": 56, "tipo": "dato",
     "proceso": "Buscar en fuentes secundarias nacionales e internacionales.",
     "actividades": ["Seleccionar bases VT/IC", "Consultar repositorios", "Registrar evidencias"],
     "entradas": "Alcance y palabras clave", "salidas": "Conocimiento explícito",
     "responsable": "Analista de datos"},
    {"id": "tacito", "n": 3, "titulo": "Tácito", "fase": "Captura", "x":.150, "y": 250, "w": 100, "h": 56, "tipo": "dato",
     "proceso": "Capturar conocimiento de actores clave.",
     "actividades": ["Entrevistas", "Eventos y foros", "Registrar necesidades"],
     "entradas": "Actores y eventos", "salidas": "Conocimiento tácito",
     "responsable": "Analista de datos"},
    {"id": "captura", "n": 4, "titulo": "Captura", "fase": "Proceso", "x": 280, "y": 150, "w": 100, "h": 56, "tipo": "proceso",
     "proceso": "Integrar información con instrumentos de captura.",
     "actividades": ["Aplicar instrumentos", "Homogeneizar formatos", "Clasificar por tema"],
     "entradas": "Explícito + tácito", "salidas": "Base estructurada",
     "responsable": "Analista de datos"},
    {"id": "tratamiento", "n": 5, "titulo": "Tratamiento", "fase": "Proceso", "x": 410, "y": 150, "w": 100, "h": 56, "tipo": "proceso",
     "proceso": "Organizar, cuantificar y procesar la información.",
     "actividades": ["Validar datos", "Consolidar indicadores", "Preparar insumos"],
     "entradas": "Base estructurada", "salidas": "Dataset tratado",
     "responsable": "Analista de datos"},
    {"id": "vtic", "n": 6, "titulo": "VT / IC", "fase": "Análisis", "x": 540, "y": 50, "w": 100, "h": 56, "tipo": "proceso",
     "proceso": "Ejecutar vigilancia tecnológica e inteligencia competitiva.",
     "actividades": ["Estudios VT/IC", "Patentabilidad", "Análisis de entorno"],
     "entradas": "Dataset tratado", "salidas": "Informes VT/IC",
     "responsable": "Analista de datos · CEITTO"},
    {"id": "tendencias", "n": 7, "titulo": "Tendencias", "fase": "Análisis", "x": 540, "y": 250, "w": 100, "h": 56, "tipo": "proceso",
     "proceso": "Identificar tendencias y oportunidades en CTi.",
     "actividades": ["Monitorear señales", "Detectar oportunidades", "Leer necesidades"],
     "entradas": "Dataset tratado", "salidas": "Mapa de tendencias",
     "responsable": "Analista de datos"},
    {"id": "productos", "n": 8, "titulo": "Productos", "fase": "Salida", "x": 670, "y": 150, "w": 100, "h": 56, "tipo": "salida",
     "proceso": "Empaquetar información de alto valor.",
     "actividades": ["Boletines", "Reportes", "Asesorías"],
     "entradas": "Resultados de análisis", "salidas": "Productos accionables",
     "responsable": "Analista de datos · CEITTO"},
    {"id": "difusion", "n": 9, "titulo": "Difusión", "fase": "Salida", "x": 800, "y": 150, "w": 100, "h": 56, "tipo": "salida",
     "proceso": "Divulgar oportunidades y fortalecer capacidades CTIC.",
     "actividades": ["Canales institucionales", "Charlas y encuentros", "Actores estratégicos"],
     "entradas": "Productos", "salidas": "Comunidad informada",
     "responsable": "Observatorio · comunicaciones"},
    {"id": "decision", "n": 10, "titulo": "Decisión", "fase": "Cierre", "x": 930, "y": 150, "w": 100, "h": 56, "tipo": "salida",
     "proceso": "Apoyar decisiones con evidencia y cerrar el ciclo.",
     "actividades": ["Entrega a dirección", "Retroalimentar ciclo", "Ajustar prioridades"],
     "entradas": "Productos difundidos", "salidas": "Decisiones · nueva demanda",
     "responsable": "Dependencias usuarias"},
]

# fix typo x =.150
FLOW[2]["x"] = 150

FLOW_EDGES = [
    ("demanda", "fuentes"), ("demanda", "tacito"),
    ("fuentes", "captura"), ("tacito", "captura"),
    ("captura", "tratamiento"),
    ("tratamiento", "vtic"), ("tratamiento", "tendencias"),
    ("vtic", "productos"), ("tendencias", "productos"),
    ("productos", "difusion"), ("difusion", "decision"),
    ("decision", "demanda"),
]

OBJ = [
    {"n": "01", "t": "Identificar tendencias CTi", "s": "Monitoreo permanente",
     "d": "Detectar tendencias en Ciencia, Tecnología e Innovación relevantes para el CMA."},
    {"n": "02", "t": "Definir captura de datos", "s": "Instrumentos y calidad",
     "d": "Definir instrumentos para capturar y procesar información confiable y trazable."},
    {"n": "03", "t": "Observar el entorno", "s": "Industria, academia e investigación",
     "d": "Leer necesidades de industria, academia e investigación para aportar al desarrollo empresarial."},
    {"n": "04", "t": "Apoyar decisiones", "s": "Información de alto valor",
     "d": "Entregar alertas, boletines y estudios VT/IC a las dependencias del CMA."},
]

PILARES = [
    {"t": "Alerta", "d": "Recopilar información del entorno para adaptarse a tiempo."},
    {"t": "Tendencias", "d": "Entregar señales útiles a las áreas de CTi."},
    {"t": "Oportunidad", "d": "Detectar financiamiento, negocios y temas prioritarios."},
]

VENTAJAS = [
    {"t": "Financiamiento", "d": "Oportunidades para proyectos y nuevos negocios"},
    {"t": "Anticipación", "d": "Adelantarse a cambios del entorno"},
    {"t": "Alertas", "d": "Monitoreo permanente por temática"},
    {"t": "Mercado", "d": "Necesidades de industria"},
    {"t": "Tendencias", "d": "Sectores de interés"},
    {"t": "Estrategia", "d": "Decisiones con evidencia"},
    {"t": "Innovación", "d": "Acelerar la innovación"},
]

PLAN = [
    {"fase": "01", "t": "Diseño", "items": [
        "Procedimiento, objetivos y flujo",
        "Instrumento de oportunidades CTi",
        "Plan de acción 2026-2027",
        "Mecanismos de captura y divulgación",
        "Primer boletín piloto",
    ]},
    {"fase": "02", "t": "Necesidades", "items": [
        "Facultades e Investigación/Extensión",
        "CEITTO: innovación, PI, emprendimiento",
        "Direcciones y Bienestar",
        "Boletines piloto 1 y 2",
        "Instrumentos de demanda industria",
    ]},
    {"fase": "03", "t": "Modelo", "items": [
        "Marco conceptual del Observatorio",
        "Diagnóstico estructural",
        "Organización y sostenibilidad",
        "Sistemas y fuentes de información",
        "Informes, difusión y conocimiento",
    ]},
]

SERVICIOS = [
    {"t": "Tendencias", "d": "Áreas de oportunidad en CTi"},
    {"t": "Monitoreo", "d": "Necesidades de industria y academia"},
    {"t": "VT / IC", "d": "Estudios a la medida"},
    {"t": "Prospectiva", "d": "Escenarios futuros"},
    {"t": "Patentabilidad", "d": "Estado de la técnica"},
    {"t": "Capacitación", "d": "Asesoría en VT/IC"},
    {"t": "Estado del arte", "d": "Apoyo a investigación"},
    {"t": "Transferencia", "d": "Modelos de negocio"},
]

CANALES = [
    "Convocatorias", "Eventos", "Mural", "Cátedra", "Buzón", "Afiches",
    "Charlas", "Reuniones", "Actores", "Publicaciones", "Jornadas", "Medios",
]

ESTUDIOS = [
    {
        "id": "camara",
        "t": "Cámara de Comercio",
        "d": "Análisis RNT en 5 subregiones de Antioquia",
        "metric": "5",
        "metric_l": "subregiones",
        "tag": "Territorio · RNT",
        "blurb": "Informe interactivo de análisis del Registro Nacional de Turismo por subregiones, con lectura territorial para decisión empresarial e institucional.",
        "evidencias": [
            {"tipo": "html", "label": "Análisis RNT subregiones", "src": "evidencias/camara/analisis-rnt-subregiones.html"},
        ],
    },
    {
        "id": "magdalena",
        "t": "Magdalena medio",
        "d": "Paisaje ganadero y desarrollo territorial",
        "metric": "8+",
        "metric_l": "entregables locales",
        "tag": "Territorio · agro",
        "blurb": "Estudios del paisaje ganadero del Magdalena Medio: atractivos, ruta Puerto Berrío-Maceo, benchmarking, modelo de negocio y taller PCG. La plataforma web se abre en pestaña nueva.",
        "evidencias": [
            {"tipo": "html", "label": "Atractivos turísticos", "src": "evidencias/magdalena/atractivos-turisticos.html"},
            {"tipo": "html", "label": "Dashboard taller PCG", "src": "evidencias/magdalena/dashboard-taller-pcg.html"},
            {"tipo": "html", "label": "Informe taller PCG", "src": "evidencias/magdalena/informe-taller-pcg.html"},
            {"tipo": "html", "label": "Ruta Puerto Berrío-Maceo", "src": "evidencias/magdalena/ruta-puerto-berrio-maceo.html"},
            {"tipo": "html", "label": "Análisis RNT Puerto Berrío", "src": "evidencias/magdalena/analisis-rnt-puerto-berrio.html"},
            {"tipo": "html", "label": "Rutas proyectadas", "src": "evidencias/magdalena/rutas-proyectadas.html"},
            {"tipo": "html", "label": "Modelo de negocio", "src": "evidencias/magdalena/modelo-negocio.html"},
            {"tipo": "html", "label": "Benchmarking PCC", "src": "evidencias/magdalena/benchmarking-pcc.html"},
            {"tipo": "html", "label": "Mapa georreferenciación", "src": "evidencias/magdalena/mapa-georreferenciacion.html"},
            {"tipo": "url", "label": "Plataforma web (Vercel)", "src": "https://mgdalena-medio.vercel.app/"},
        ],
    },
    {
        "id": "do",
        "t": "Denominación de origen",
        "d": "Tapetusa artesanal y reconocimiento DOP",
        "metric": "12+",
        "metric_l": "anexos y tableros",
        "tag": "DOP · CEITTO",
        "blurb": "Expediente técnico con percepción territorial, tableros Power BI, misión técnica, infografías y guías para autoridades y productores.",
        "evidencias": [
            {"tipo": "html", "label": "Infografía Tapetusa", "src": "evidencias/do/infografia-tapetusa-profesional.html"},
            {"tipo": "html", "label": "Infografía actualizada", "src": "evidencias/do/infografia-tapetusa-actualizada.html"},
            {"tipo": "pdf", "label": "Tableros Power BI", "src": "evidencias/do/anexo-4-screenshot-tableros-power-bi.pdf"},
            {"tipo": "pdf", "label": "Gráfico de resultados", "src": "evidencias/do/anexo-1-gr-fico-de-resultados.pdf"},
            {"tipo": "pdf", "label": "Tabla de resultados", "src": "evidencias/do/anexo-1-tabla-de-resultados.pdf"},
            {"tipo": "pdf", "label": "Percepción municipios", "src": "evidencias/do/anexo-3-an-lisis-de-percepci-n-de-los-municipios.pdf"},
            {"tipo": "pdf", "label": "Matriz diagnóstico", "src": "evidencias/do/anexo-5-matriz-diagnostico-de-los-municipios.pdf"},
            {"tipo": "pdf", "label": "Informe misión técnica DOP", "src": "evidencias/do/anexo-8-informe-final-misi-n-t-cnica-dop.pdf"},
            {"tipo": "pdf", "label": "Evidencia del viaje", "src": "evidencias/do/anexo-9-evidencia-del-viaje.pdf"},
            {"tipo": "pdf", "label": "BPM Tapetusa", "src": "evidencias/do/bpm-tapetusa.pdf"},
        ],
    },
    {
        "id": "penol",
        "t": "Peñol",
        "d": "RNT territorial y potencial turístico",
        "metric": "2",
        "metric_l": "informes HTML",
        "tag": "Turismo · RNT",
        "blurb": "Webscraping del RNT y reporte turístico del municipio de Peñol como apoyo a la lectura competitiva del destino.",
        "evidencias": [
            {"tipo": "html", "label": "Informe webscraping Peñol", "src": "evidencias/penol/informe-webscraping-penol.html"},
            {"tipo": "html", "label": "Informe turístico Peñol", "src": "evidencias/penol/informe-turistico-penol.html"},
        ],
    },
    {
        "id": "comfama",
        "t": "Comfama",
        "d": "Madurez de la Ruta Lechera San Pedro",
        "metric": "1",
        "metric_l": "informe de madurez",
        "tag": "Rutas · turismo",
        "blurb": "Diagnóstico de madurez de la ruta lechera / San Pedro como insumo de vigilancia e inteligencia para el entorno turístico.",
        "evidencias": [
            {"tipo": "html", "label": "Informe madurez Ruta San Pedro", "src": "evidencias/comfama/informe-madurez-ruta-san-pedro.html"},
        ],
    },
    {
        "id": "convocatorias",
        "t": "Convocatorias",
        "d": "Radar de oportunidades de financiación",
        "metric": "30+",
        "metric_l": "oportunidades/mes (meta)",
        "tag": "Radar · I+D+i",
        "blurb": "ConvoRadar opera como dashboard en vivo. Por seguridad del navegador no se embebe: ábrelo en una pestaña nueva para ver el tablero completo.",
        "evidencias": [
            {"tipo": "url", "label": "ConvoRadar dashboard", "src": "https://convocaradar-web.vercel.app/dashboard"},
            {"tipo": "url", "label": "ConvoRadar inicio", "src": "https://convocaradar-web.vercel.app/"},
        ],
    },
    {
        "id": "investigacion",
        "t": "Investigación",
        "d": "Proyectos finalizados con evidencia entregable",
        "metric": "N",
        "metric_l": "cierres documentados",
        "tag": "Proyectos",
        "blurb": "Capacidad demostrada para cerrar estudios VT/IC con productos accionables para dependencias y aliados.",
        "evidencias": [],
    },
]

LINEAS = [
    {"t": "Gestión empresarial", "d": "Productividad y competitividad"},
    {"t": "VT / IC", "d": "Vigilancia e inteligencia"},
    {"t": "Patentabilidad", "d": "Estado de la técnica"},
]

CAPACIDADES = [
    {"t": "Analista de datos", "d": "Un perfil con experiencia para operar el Observatorio."},
    {"t": "Software especializado", "d": "Acceso a herramientas de análisis y vigilancia."},
    {"t": "Red Innruta", "d": "Inteligencia competitiva y sus plataformas."},
    {"t": "Red Secopind", "d": "Propiedad intelectual · ICIPC."},
]

# Dedicación del equipo: 1 ago – 15 dic = 4 meses + 15 días ≈ 4,5 meses
MESES_TALENTO = 4.5
PERIODO_TALENTO = "ago – 15 dic"

TALENTO = [
    {
        "ini": "JM", "nombre": "José Mario López Gómez",
        "rol": "Docente ocasional · Facultad de Administración · apoyo y articulación CEITTO / TI",
        "dedica": "10 horas de apoyo", "cop": 3_750_000,
    },
    {
        "ini": "JP", "nombre": "Julián Esteban Pineda Montoya",
        "rol": "Analista de datos · escalamiento y operación de ConvocaRadar-IA",
        "dedica": "Medio tiempo · CEITTO", "cop": 2_200_000,
    },
    {
        "ini": "CJ", "nombre": "Consultor Junior",
        "rol": "Apoyo en pruebas, documentación y soporte de la plataforma",
        "dedica": "Por demanda · CEITTO", "cop": 450_000,
    },
]
# Ruta de escalamiento de ConvocaRadar-IA: de local a infraestructura TI del CMA
ESCALADO = [
    {
        "n": "01", "t": "Alistamiento y diagnóstico",
        "meta": "CEITTO + Gestión de Tecnología e Informática del CMA",
        "acts": [
            "Inventario técnico de ConvocaRadar-IA: código, dependencias, base de datos y tareas de scraping",
            "Levantamiento de requisitos con el área TI del CMA: capacidad, red y seguridad",
            "Definición de la arquitectura destino en la infraestructura institucional",
            "Plan de trabajo con riesgos, tiempos y responsables",
        ],
        "out": "Documento de arquitectura y plan de escalamiento aprobado por TI",
    },
    {
        "n": "02", "t": "Preparación de infraestructura",
        "meta": "Aprovisionamiento en el ecosistema tecnológico Colmayor",
        "acts": [
            "Aprovisionamiento de servidor o máquina virtual y base de datos institucional",
            "Configuración de red, dominio y certificados SSL del CMA",
            "Políticas de acceso, roles y cumplimiento de Ley 1581 (datos personales)",
            "Conexión del repositorio GitHub al despliegue continuo (CI/CD)",
        ],
        "out": "Ambientes institucionales de desarrollo y producción listos",
    },
    {
        "n": "03", "t": "Migración y despliegue",
        "meta": "Traslado de la plataforma desde el entorno local",
        "acts": [
            "Empaquetado y migración del código desde el entorno local",
            "Migración de la base de datos y de las fuentes de convocatorias",
            "Programación de scraping y clasificación con IA en el servidor institucional",
            "Integración de autenticación y usuarios institucionales",
        ],
        "out": "ConvocaRadar-IA operando en la infraestructura del CMA",
    },
    {
        "n": "04", "t": "Pruebas y validación",
        "meta": "Verificación funcional, técnica y con usuarios",
        "acts": [
            "Pruebas funcionales de búsqueda, filtros y alertas de convocatorias",
            "Pruebas de carga y rendimiento del scraping programado",
            "Pruebas de seguridad, respaldo y recuperación",
            "Validación con usuarios de CEITTO, investigación y extensión (UAT)",
        ],
        "out": "Acta de pruebas con visto bueno de TI y CEITTO",
    },
    {
        "n": "05", "t": "Producción y soporte",
        "meta": "Operación estable con soporte del equipo CEITTO",
        "acts": [
            "Puesta en producción con monitoreo y respaldos automáticos",
            "Capacitación a usuarios y documentación de operación",
            "Soporte y mejora continua a cargo del equipo CEITTO",
            "Indicadores de uso y ampliación de fuentes nacionales e internacionales",
        ],
        "out": "Plataforma institucional estable con soporte permanente",
    },
]

# --- Versión ejecutiva (resumen para decisión) ---
BENEFICIOS_EXEC = [
    {"t": "Decisión con evidencia", "d": "Tableros PDI L1–L4 y alertas ejecutivas en días, no en semanas."},
    {"t": "Convocatorias trazables", "d": "Radar nacional e internacional con embudo hasta cierre y productos."},
    {"t": "Calidad y acreditación", "d": "Expedientes con dato oficial, reportado o propuesto, listos para CNA."},
    {"t": "Transparencia y riesgo", "d": "Linaje del dato, evidencia y soporte frente a mapas de riesgos G+."},
    {"t": "Capacidad instalada", "d": "DGX Spark + CEITTO para VT/IC, IA local y servicios externos."},
    {"t": "Conecta institucional", "d": "Articula facultades, Distrito, redes y transferencia (ruta OTRI)."},
]

COMPUTO_USO = [
    {"t": "IA local segura", "d": "Inferencia y ajuste de modelos en campus, sin depender solo de nube."},
    {"t": "ConvocaRadar-IA", "d": "Scraping, clasificación y alertas de convocatorias N/I en producción."},
    {"t": "Analítica institucional", "d": "Tableros de PDI, permanencia, semilleros y venta de servicios."},
    {"t": "VT / IC a la medida", "d": "Estudios territoriales y sectoriales con entrega HTML/PDF/tablero."},
    {"t": "Respaldo continuo", "d": "UPS Eaton + nodo siempre disponible para agentes y reportes."},
]


# Cronograma Gantt 2026-2: 1 ago – 18 dic (140 días). start/end = día 0-index desde 1 ago.
GANTT_MESES = [
    {"id": "ago", "label": "Agosto", "days": 31, "start": 0},
    {"id": "sep", "label": "Septiembre", "days": 30, "start": 31},
    {"id": "oct", "label": "Octubre", "days": 31, "start": 61},
    {"id": "nov", "label": "Noviembre", "days": 30, "start": 92},
    {"id": "dic", "label": "Dic (1–18)", "days": 18, "start": 122},
]
GANTT_TOTAL_DIAS = 140  # 31+30+31+30+18

GANTT_2026_2 = [
    {
        "id": "g1", "t": "Alistamiento y diagnóstico",
        "start": 0, "end": 30, "resp": "CEITTO + TI",
        "desc": "Inventario ConvocaRadar-IA, requisitos TI, arquitectura destino y plan de riesgos.",
        "entregables": [
            "Documento de arquitectura aprobado",
            "Inventario técnico de la plataforma",
            "Plan de trabajo ago–dic con responsables",
        ],
    },
    {
        "id": "g2", "t": "Aprovisionamiento DGX Spark + UPS",
        "start": 14, "end": 60, "resp": "TI · Compras",
        "desc": "Recepción, instalación y puesta en marcha del nodo de IA y respaldo eléctrico.",
        "entregables": [
            "DGX Spark en operación en campus",
            "Eaton DX2000LAN configurado",
            "Acta de recepción técnica",
        ],
    },
    {
        "id": "g3", "t": "Migración ConvocaRadar-IA a TI",
        "start": 31, "end": 80, "resp": "Julián · TI",
        "desc": "Despliegue desde entorno local a infraestructura Colmayor, CI/CD e identidades.",
        "entregables": [
            "Ambientes desarrollo y producción",
            "ConvocaRadar-IA en infra CMA",
            "Accesos institucionales configurados",
        ],
    },
    {
        "id": "g4", "t": "Piloto bienestar → permanencia",
        "start": 61, "end": 106, "resp": "CEITTO · Bienestar",
        "desc": "Caso demostrativo que conecta evidencia de bienestar con trayectoria estudiantil.",
        "entregables": [
            "Tablero piloto validado",
            "Indicadores de permanencia cargados",
            "Informe de hallazgos del piloto",
        ],
    },
    {
        "id": "g5", "t": "Integración indicadores PDI",
        "start": 75, "end": 126, "resp": "CEITTO · Planeación",
        "desc": "Tablero ejecutivo L1, L2 y L4 con lectura IES Distrito y leyenda Oficial/Reportado/Propuesto.",
        "entregables": [
            "Tablero ejecutivo PDI",
            "Radar de convocatorias operativo",
            "Diccionario de indicadores mínimos",
        ],
    },
    {
        "id": "g6", "t": "Pruebas, UAT y ajustes",
        "start": 101, "end": 133, "resp": "Junior · TI · CEITTO",
        "desc": "Pruebas funcionales, de carga, seguridad y validación con usuarios.",
        "entregables": [
            "Acta de pruebas con visto bueno",
            "Lista de hallazgos y ajustes",
            "Checklist de seguridad y respaldos",
        ],
    },
    {
        "id": "g7", "t": "Capacitación y cierre 2026-2",
        "start": 122, "end": 139, "resp": "José Mario · Julián",
        "desc": "Formación a usuarios, documentación de operación y proyección 2027.",
        "entregables": [
            "Sesiones de capacitación registradas",
            "Manual de operación v1",
            "Acta de cierre y proyección 2027",
        ],
    },
]

CRONO_2026_2 = GANTT_2026_2  # compat

MINIMO_OP = [
    "DGX Spark + Eaton DX2000LAN en operación",
    "ConvocaRadar-IA desplegado en infraestructura TI del CMA",
    "Un tablero ejecutivo (PDI / convocatorias / piloto)",
    "Equipo CEITTO con dedicación activa (JM 10 h + Julián MT + Junior)",
    "Leyenda Oficial / Reportado / Propuesto en indicadores",
]

PROYECCION_2027 = [
    {"t": "Autofinanciamiento", "d": "Ampliar venta de servicios VT/IC y estudios a terceros."},
    {"t": "Dominios separados", "d": "Internacionalización, Graduados y Centro de Lenguas con dueños de dato."},
    {"t": "Ruta OTRI", "d": "Avanzar reconocimiento Minciencias de transferencia de resultados."},
    {"t": "Red Innruta", "d": "Consolidar ingreso y uso de plataformas de inteligencia competitiva."},
    {"t": "Más plataformas", "d": "Pipeline de productos digitales alineados al PDI y al Distrito."},
]

QUE_SIGUE = [
    {"plat": "ConvocaRadar-IA", "foco": "Vigilancia de convocatorias nacionales e internacionales", "estado": "En escalamiento a TI Colmayor"},
    {"plat": "Tablero PDI ejecutivo", "foco": "L1, L2 y L4 con indicadores IES Distrito y alertas", "estado": "Por diseñar · 2026-2"},
    {"plat": "Piloto permanencia", "foco": "Bienestar → graduación y éxito académico", "estado": "Caso demostrativo"},
    {"plat": "Observatorio VT/IC", "foco": "Estudios territoriales y sectoriales con evidencia", "estado": "Trayectoria demostrada"},
    {"plat": "Ruta OTRI / transferencia", "foco": "Gestión de PI, licenciamiento y spin-offs (TRL 6–9)", "estado": "Línea estratégica"},
    {"plat": "Suite Innruta", "foco": "Inteligencia competitiva y vigilancia tecnológica en red", "estado": "Ingreso a la red"},
]

PERFIL_IDONEIDAD = [
    {"t": "Analista de datos CEITTO", "d": "Opera plataformas, limpia datos y entrega tableros/reportes."},
    {"t": "Articulación académica", "d": "Docente ocasional Fac. Administración (10 h) conecta demanda institucional."},
    {"t": "Soporte junior", "d": "Pruebas, documentación y acompañamiento de usuarios."},
    {"t": "TI Colmayor", "d": "Infraestructura, seguridad, identidad y continuidad del servicio."},
]

ALIANZAS = [
    {
        "t": "Ruta OTRI · Minciencias",
        "d": "Reconocimiento de Oficinas de Transferencia de Resultados de Investigación: transferencia TRL 6–9, PI, spin-offs y articulación U–empresa.",
        "url": "https://minciencias.gov.co/reconocimiento-actores/reconocimiento-oficinas-transferencia-resultados-investigacion-otri",
        "tag": "Certificación / reconocimiento",
    },
    {
        "t": "Red Innruta",
        "d": "Ingreso a la red de inteligencia competitiva: plataformas, buenas prácticas y colaboración en VT/IC.",
        "url": "https://www.linkedin.com/in/innruta-red-ic-41343016b/",
        "tag": "Alianza estratégica",
    },
    {
        "t": "Red Secopind · ICIPC",
        "d": "Propiedad intelectual y vigilancia tecnológica con referentes del ecosistema.",
        "url": "",
        "tag": "Red técnica",
    },
    {
        "t": "Conecta CEITTO",
        "d": "Mecanismo de articulación con facultades, investigación, extensión, Distrito y aliados externos.",
        "url": "",
        "tag": "Gobernanza interna",
    },
]

PLAN_DISENO = [
    {"n": "01", "t": "Diseño", "items": [
        "Procedimiento, objetivos y flujo del Observatorio",
        "Instrumento de oportunidades CTi",
        "Plan de acción 2026-2027",
        "Mecanismos de captura y divulgación",
    ]},
    {"n": "02", "t": "Necesidades", "items": [
        "Facultades, Investigación y Extensión",
        "CEITTO: innovación, PI y emprendimiento",
        "Direcciones y Bienestar (piloto)",
        "Demanda de industria y territorio",
    ]},
    {"n": "03", "t": "Modelo", "items": [
        "Gobernanza de datos (Oficial / Reportado / Propuesto)",
        "MVP en DGX Spark + ConvocaRadar-IA",
        "Indicadores mínimos PDI y Distrito",
        "Ruta de alianzas OTRI / Innruta",
    ]},
]



# Contextualizado a Colmayor (PDI 2024-2028, CNA, CEITTO, Alcaldía de Medellín)
PROBLEMAS = [
    {
        "id": "P1", "tipo": "alerta", "titulo": "Información dispersa",
        "colmayor": "Académico, administrativo y de entorno en sistemas separados",
        "desc": "En Colmayor, los datos de facultades, investigación, extensión, bienestar y planeación suelen vivir en formatos y sistemas distintos. Eso dificulta el seguimiento del Plan Indicativo y retrasa reportes para dirección, MIPG y autoevaluación.",
        "efecto": "Se pierde trazabilidad, se duplican esfuerzos y las decisiones llegan tarde.",
    },
    {
        "id": "P2", "tipo": "alerta", "titulo": "Convocatorias sin trazabilidad",
        "colmayor": "Oportunidades de I+D+i, extensión y CEITTO",
        "desc": "Sin mapeo continuo, grupos, semilleros y el CEITTO (emprendimiento, innovación, transferencia y propiedad intelectual) detectan tarde convocatorias locales, nacionales e internacionales.",
        "efecto": "Se reducen postulaciones oportunas y la articulación con el entorno productivo de Medellín y Antioquia.",
    },
    {
        "id": "P3", "tipo": "alerta", "titulo": "Entorno cambiante",
        "colmayor": "Políticas públicas, tecnología y territorio",
        "desc": "Como institución adscrita a la Alcaldía de Medellín, Colmayor necesita leer cambios educativos, tecnológicos y normativos que afectan programas, extensión, internacionalización y acompañamiento territorial (incluido Presupuesto Participativo).",
        "efecto": "Sin vigilancia estructurada (UNE 166006, ISO 56002, ISO 31000) la adaptación institucional llega con retraso.",
    },
    {
        "id": "P4", "tipo": "neutral", "titulo": "Brecha analítica",
        "colmayor": "Acreditación CNA y calidad académica",
        "desc": "El aseguramiento de la calidad y la renovación de acreditación exigen evidencia consolidada. La brecha analítica limita indicadores CNA, rankings y la investigación aplicada con el sector productivo.",
        "efecto": "Más carga manual en autoevaluación y menor capacidad de anticipar hallazgos de calidad.",
    },
    {
        "id": "P5", "tipo": "neutral", "titulo": "Gobernanza de datos",
        "colmayor": "Confianza institucional y ecosistema tecnológico",
        "desc": "Hace falta un marco formal de privacidad (Ley 1581), roles de datos y criterios éticos para usar información e inteligencia analítica con confianza, en línea con la Línea 3 del PDI (gestión integral de la información).",
        "efecto": "Sin gobierno claro, es difícil integrar fuentes y sostener una cultura de datos alineada al PETIC.",
    },
    {
        "id": "P6", "tipo": "solucion", "titulo": "Respuesta del Observatorio",
        "colmayor": "Capacidad permanente de inteligencia institucional",
        "desc": "El Observatorio CTi articula arquitectura de datos, gobierno de información, tableros ejecutivos y productos de vigilancia tecnológica e inteligencia competitiva para las dependencias del CMA.",
        "efecto": "Pasa de reportes fragmentados a evidencia útil para planeación, calidad, investigación y extensión.",
    },
]

# Ventajas no monetarias alineadas al Plan de Desarrollo 2024-2028
VENTAJAS_PDI = [
    {
        "linea": "L1",
        "nombre": "Academia transformadora de vidas",
        "foco": "Diversidad, equidad, calidad e inclusión",
        "indicadores": [
            {"t": "Evidencia para autoevaluación CNA", "m": "Expedientes de calidad con datos trazables por factor"},
            {"t": "Tiempo de reporte académico", "m": "Meta orientativa: reducir al menos 20% el tiempo de consolidación"},
            {"t": "Permanencia y graduación", "m": "Tableros de bienestar y éxito académico (piloto del Observatorio)"},
            {"t": "Apoyo a decanos y programas", "m": "Respuesta a solicitudes de información en máximo 5 días hábiles"},
        ],
    },
    {
        "linea": "L2",
        "nombre": "Intercambio de saberes",
        "foco": "Investigación, innovación, emprendimiento y proyección social",
        "indicadores": [
            {"t": "Convocatorias detectadas a tiempo", "m": "Meta orientativa: al menos 30 oportunidades mapeadas al mes"},
            {"t": "Productos VT/IC para el entorno", "m": "Al menos 2 reportes de inteligencia al mes"},
            {"t": "Articulación con sector productivo", "m": "Estudios y alertas útiles a extensión y CEITTO"},
            {"t": "Apoyo a grupos y semilleros", "m": "Estado del arte y vigilancia para proyectos y postulaciones"},
        ],
    },
    {
        "linea": "L3",
        "nombre": "Ecosistema tecnológico Colmayor",
        "foco": "Interoperabilidad, información y mejora continua",
        "indicadores": [
            {"t": "Fuentes institucionales integradas", "m": "Meta orientativa: al menos 5 fuentes al mes 6"},
            {"t": "Disponibilidad de tableros", "m": "Meta: disponibilidad igual o superior a 99,5%"},
            {"t": "Cultura de datos", "m": "Procedimientos, catálogo de fuentes y roles documentados (PETIC)"},
            {"t": "Continuidad operativa", "m": "Infraestructura TI con respaldo energético y garantía en sitio"},
        ],
    },
    {
        "linea": "L4",
        "nombre": "Sostenibilidad y gestión humana",
        "foco": "Planeación, capacidad instalada e identidad institucional",
        "indicadores": [
            {"t": "Soporte al Plan Indicativo", "m": "Datos oportunos para seguimiento de líneas y metas"},
            {"t": "Decisiones directivas con evidencia", "m": "Meta orientativa: al menos 3 decisiones documentadas por trimestre"},
            {"t": "Uso compartido de capacidad", "m": "Computador de alto rendimiento disponible para Observatorio y otros procesos priorizados"},
            {"t": "Transparencia operativa", "m": "Trazabilidad de fuentes, productos y responsables"},
        ],
    },
]



# Agenda institucional + indicadores IES Distrito + riesgos (observaciones Felipe)
# Período de referencia indicadores: Plan Indicativo IES Distrito · corte jun-2026
AGENDA_INST = [
    {
        "id": "l1",
        "linea": "L1",
        "nombre": "Academia transformadora de vidas",
        "foco": "Calidad, trayectorias estudiantiles y agenda de estudios",
        "programas": [
            "Experiencias formativas significativas",
            "Transformación pedagógica e innovación educativa",
            "Autoevaluación y acreditación de alta calidad",
            "Trayectorias estudiantiles, permanencia y graduación",
        ],
        "estudios": [
            {"a": "2024", "t": "Avances en la evaluación del impacto de la docencia (ventana 2018-2023)"},
            {"a": "2022", "t": "Resultados Saber Pro y Saber TyT · Colmayor (2017-2022)"},
            {"a": "2022", "t": "Análisis de valor agregado · Saber Pro 2019-2020"},
            {"a": "2022", "t": "Caracterización de la población estudiantil (2018-2021)"},
            {"a": "2022", "t": "Evaluación de impacto de la formación de pregrado en graduados"},
        ],
        "indicadores": [
            {"cod": "1.2.1.4", "t": "Matrícula educación superior", "meta": "10.500 plan", "logro": "6.622", "u": "estudiantes"},
            {"cod": "1.2.1.10", "t": "Permanencia estudiantil", "meta": "4.781", "logro": "5.938*", "u": "intervenciones"},
            {"cod": "1.2.13", "t": "Acreditación institucional vigente", "meta": "1", "logro": "1", "u": "vigente"},
            {"cod": "1.2.15", "t": "Programas con acreditación de alta calidad", "meta": "10 (2026)", "logro": "1", "u": "programas"},
            {"cod": "1.2.2.10", "t": "Seguridad alimentaria Colmayor", "meta": "1", "logro": "1", "u": "estrategia"},
        ],
        "aporte": "Tablero oficial de cobertura, éxito académico y evidencia para autoevaluación CNA, alimentado por la Agenda de Estudios Institucionales.",
    },
    {
        "id": "l2",
        "linea": "L2",
        "nombre": "Intercambio de saberes",
        "foco": "Investigación, extensión, PMO y Plan Indicativo Distrital",
        "programas": [
            "Investigación e innovación formativa",
            "Innovación, transferencia y emprendimiento",
            "Nuevos talentos y formación avanzada",
            "Territorio, proyección social y extensión",
            "Formación para la vida y el trabajo",
            "Mundo sin fronteras (internacionalización)",
        ],
        "dominios": [
            {"t": "Internacionalización", "d": "Movilidad, bilingüismo y competencias globales (dominio separado)"},
            {"t": "Graduados", "d": "Inserción laboral, pertinencia e impacto de la formación"},
            {"t": "Centro de Lenguas", "d": "Estrategias de bilingüismo y competencias lingüísticas"},
        ],
        "estudios": [
            {"a": "2022", "t": "Evaluación del impacto de la Internacionalización (2017-2021)"},
            {"a": "2022", "t": "Evaluación de impacto en formación de pregrado · egresados"},
            {"a": "2015", "t": "Estudios de pertinencia e inserción laboral por programa"},
            {"a": "2020", "t": "Evaluaciones de impacto por programa académico (cohortes 2014-2018)"},
        ],
        "indicadores": [
            {"cod": "1.2.6.2", "t": "Semilleros de investigación activos", "meta": "14 (2026)", "logro": "14", "u": "semilleros"},
            {"cod": "1.2.6.3", "t": "Estudiantes en semilleros", "meta": "402 (2026)", "logro": "410", "u": "estudiantes"},
            {"cod": "1.2.6.4", "t": "Publicaciones indexadas", "meta": "40 (2026)", "logro": "15", "u": "publicaciones"},
            {"cod": "1.2.7.1", "t": "Emprendimientos base tecnológica/ICC", "meta": "6 (2026)", "logro": "3", "u": "emprendimientos"},
            {"cod": "1.2.7.4", "t": "Proyectos I+D+i alianza cuádruple hélice", "meta": "1 (2026)", "logro": "1", "u": "proyectos"},
            {"cod": "1.2.1.14", "t": "Estrategia de internacionalización", "meta": "1", "logro": "1", "u": "estrategia"},
        ],
        "pmo": [
            "Embudo: convocatoria → comité → aprobación → ejecución → cierre",
            "Tiempo de respuesta al comité y productos entregables",
            "Acompañamiento técnico real (PMO activa, no vacía)",
            "Lectura del Plan Indicativo Distrital + aporte Colmayor",
        ],
        "aporte": "Radar de convocatorias, productos de investigación y dominios separados (Intl / Graduados / Lenguas) con lectura Distrital.",
    },
    {
        "id": "l4",
        "linea": "L4",
        "nombre": "Sostenibilidad y gestión humana integral",
        "foco": "Talento, recursos, venta de servicios y riesgos financieros",
        "programas": [
            "Gestión del talento humano",
            "Mercadeo e identidad institucional",
            "Planificación, gestión y sostenibilidad institucional",
        ],
        "estudios": [
            {"a": "PDI", "t": "Seguimiento a ingresos por venta de servicios y autofinanciamiento"},
            {"a": "PDI", "t": "Capacidad instalada del equipo CEITTO / Observatorio"},
            {"a": "MIPG", "t": "Transparencia, ética pública y atención al ciudadano"},
        ],
        "indicadores": [
            {"cod": "PDI", "t": "Ingresos por venta de servicios (meta acumulada PDI)", "meta": "$3.930 M", "logro": "en seguimiento", "u": "COP"},
            {"cod": "Obs", "t": "Costo mensual equipo CEITTO (escalamiento)", "meta": "$6.4 M", "logro": "asignado", "u": "COP/mes"},
            {"cod": "Obs", "t": "Total talento ago–15 dic (4,5 meses)", "meta": "$28.8 M", "logro": "proyectado", "u": "COP"},
            {"cod": "1.2.6.6", "t": "Plan estratégico de TIC en implementación", "meta": "1", "logro": "1", "u": "plan"},
        ],
        "aporte": "Tablero potencial → solicitado → aprobado → ejecutado → facturado → recaudado → margen, con equipo y recursos visibles.",
    },
    {
        "id": "riesgos",
        "linea": "RX",
        "nombre": "Riesgos, PINAR y gobernanza",
        "foco": "Mapas de riesgos + información dispersa + Agenda bidireccional",
        "programas": [
            "Gobernanza de datos (L3 · Gestión integral de la información)",
            "PINAR 2024: archivo, repositorios y estructura documental",
            "Agenda de Estudios Institucionales ↔ Observatorio (bidireccional)",
            "Leyenda de datos: Oficial / Reportado / Propuesto",
        ],
        "estudios": [
            {"a": "Calidad", "t": "Agenda de Estudios sobre Asuntos Institucionales (Aseguramiento de la Calidad)"},
            {"a": "PINAR", "t": "Información dispersa documentada en PINAR 2024 (informe de pares)"},
            {"a": "G+", "t": "Mapas de riesgos corrupción y gestión · seguimiento 30/04/2026"},
        ],
        "indicadores": [
            {"cod": "PDI", "t": "Modelo de gobernanza de datos implementado", "meta": "1", "logro": "1 (2025-2)", "u": "modelo"},
            {"cod": "Corr", "t": "Riesgos de corrupción Alta/Extrema mapeados", "meta": "49", "logro": "en G+", "u": "riesgos"},
            {"cod": "Gest", "t": "Riesgos de gestión (mapa institucional)", "meta": "138", "logro": "4 Alta", "u": "riesgos"},
        ],
        "riesgos": [
            {"z": "Extrema", "t": "Manipulación de plataformas tecnológicas", "a": "Trazabilidad, linaje y evidencia de accesos"},
            {"z": "Alta", "t": "Manejo indebido de la información", "a": "Catálogo de dominios, custodios y publicación controlada"},
            {"z": "Alta", "t": "Utilización indebida de información", "a": "Roles, bitácora y separación de datos sensibles"},
            {"z": "Alta", "t": "Desviación de recursos / jineteo", "a": "Flujo proyecto–presupuesto–evidencia auditables"},
            {"z": "Extrema", "t": "Desviación en asignación de beneficios", "a": "Cupos, criterios y beneficiarios trazables"},
            {"z": "Alta", "t": "Alteración u ocultamiento de información", "a": "Estados Borrador→Validado→Publicado"},
            {"z": "Clave", "t": "Baja integración / difícil acceso a sistemas", "a": "Interoperabilidad y repositorio de indicadores"},
            {"z": "Clave", "t": "Pérdida de archivo e información", "a": "PINAR, expediente electrónico y KPI→soporte"},
        ],
        "aporte": "El Observatorio no sustituye el control interno: aporta transparencia, evidencia y alertas ejecutivas sobre riesgos de información y recursos.",
    },
]

KPIS = [
    {"id": "KPI-01", "dim": "operativa", "nombre": "Disponibilidad del servidor", "meta": "≥ 99% mensual"},
    {"id": "KPI-02", "dim": "operativa", "nombre": "Tiempo de integración de datos", "meta": "< 2 horas/día"},
    {"id": "KPI-03", "dim": "operativa", "nombre": "Disponibilidad de tableros", "meta": "≥ 99,5%"},
    {"id": "KPI-04", "dim": "operativa", "nombre": "Recuperación ante fallo energético", "meta": "0 pérdida de datos"},
    {"id": "KPI-05", "dim": "analitica", "nombre": "Convocatorias mapeadas/mes", "meta": "≥ 30"},
    {"id": "KPI-06", "dim": "analitica", "nombre": "Reportes de inteligencia/mes", "meta": "≥ 2"},
    {"id": "KPI-07", "dim": "analitica", "nombre": "Fuentes de datos integradas", "meta": "≥ 5 al mes 6"},
    {"id": "KPI-08", "dim": "analitica", "nombre": "Tiempo respuesta directivos", "meta": "≤ 5 días hábiles"},
    {"id": "KPI-09", "dim": "analitica", "nombre": "Precisión clasificación convocatorias", "meta": "≥ 85%"},
    {"id": "KPI-10", "dim": "roi", "nombre": "Valor convocatorias postuladas", "meta": "≥ COP 30M adjudicadas"},
    {"id": "KPI-11", "dim": "roi", "nombre": "Tasa conversión convocatorias", "meta": "≥ 30% postulación"},
    {"id": "KPI-12", "dim": "roi", "nombre": "Ahorro herramientas externalizadas", "meta": "≥ 70% reducción"},
    {"id": "KPI-13", "dim": "roi", "nombre": "Reducción horas recopilación manual", "meta": "≥ 40%"},
    {"id": "KPI-14", "dim": "roi", "nombre": "Ingresos servicios externos", "meta": "≥ COP 10M año 1"},
    {"id": "KPI-15", "dim": "roi", "nombre": "Propuestas comerciales enviadas", "meta": "≥ 2 al mes 6"},
    {"id": "KPI-16", "dim": "roi", "nombre": "Reducción tiempo acreditación", "meta": "≥ 20%"},
    {"id": "KPI-17", "dim": "roi", "nombre": "Decisiones con evidencia", "meta": "≥ 3/trimestre"},
    {"id": "KPI-18", "dim": "sostenibilidad", "nombre": "ROI acumulado hardware", "meta": "≥ 50% al mes 6"},
    {"id": "KPI-19", "dim": "sostenibilidad", "nombre": "Punto de equilibrio", "meta": "mes 6–14"},
    {"id": "KPI-20", "dim": "sostenibilidad", "nombre": "Índice autofinanciamiento", "meta": "≥ 30% al mes 6"},
]

DIM_LABEL = {
    "operativa": "Operativa",
    "analitica": "Analítica",
    "roi": "ROI",
    "sostenibilidad": "Sostenibilidad",
}

HW = {
    "ws": {
        "titulo": "NVIDIA DGX Spark · supercomputador personal de IA",
        "specs": [
            "Superchip NVIDIA GB10 Grace Blackwell (CPU Arm 20 núcleos: 10× Cortex-X925 + 10× Cortex-A725)",
            "Hasta 1 PFLOP de desempeño de IA (FP4) · Tensor Cores 5.ª generación",
            "128 GB LPDDR5x de memoria unificada coherente (273 GB/s)",
            "SSD NVMe M.2 4 TB con autocifrado · NVIDIA DGX OS",
            "ConnectX-7 200 Gbps · 10 GbE · Wi-Fi 7 · BT 5.4 · 4× USB-C · HDMI 2.1a",
            "Formato compacto 150×150×50,5 mm · 1,2 kg · PSU 240 W (TDP GB10 140 W)",
            "Proveedor Colombia: Clones y Periféricos (oferta jul-2026)",
        ],
        "cop": 29420000,
        "list_cop": 31479000,
        "img": "media/dgx-spark.jpg",
        "url": "https://clonesyperifericos.com/comprar/pc-nvidia-dgx-spark-20-core-arm-10-cortex-x925-10-cortex-a725-arm-128gb-lpddr5x/",
    },
    "ups": {
        "titulo": "Eaton DX2000LAN",
        "specs": [
"Online doble conversión",
            "2000 VA / 1800 W · factor de potencia 0,9",
            "Autonomía 5–15 min según carga",
            "Pantalla LCD · USB · ranura NMC / LAN",
            "Cubre consumo estimado del DGX Spark (PSU 240 W)",
            "Torre · instalación rápida",
            "Respaldo eléctrico continuo para el nodo DGX",
        ],
        "cop": 2_400_000,
        "img": "media/eaton-dx2000lan.jpg",
    },
}

_ws = HW["ws"]["cop"]
_ups = HW["ups"]["cop"]
_ia = 4_500_000 + 7_600_000  # antes: red/conectividad + implementación
_total = _ws + _ups + _ia
PRESUPUESTO = {
    "total": _total,
    "lineas": [
        {"nombre": "NVIDIA DGX Spark (Clones y Periféricos)", "valor": _ws, "pct": round(_ws / _total * 100, 1)},
        {"nombre": "UPS Eaton DX2000LAN", "valor": _ups, "pct": round(_ups / _total * 100, 1)},
        {"nombre": "Implementación de IA", "valor": _ia, "pct": round(_ia / _total * 100, 1)},
    ],
}

FUENTES = ["Scopus", "ScienceDirect", "IEEE", "EBSCO", "Embase", "Reaxys", "Engineering Village", "e-libro"]


def node_cx(n):
    return n["x"] + n["w"] / 2


def node_cy(n):
    return n["y"] + n["h"] / 2


def edge_d(a, b, cyclic=False):
    ax, ay, bx, by = node_cx(a), node_cy(a), node_cx(b), node_cy(b)
    if cyclic:
        return f"M {ax} {ay + 28} C {ax} {ay + 120}, {bx} {by + 120}, {bx} {by + 28}"
    mx = (ax + bx) / 2
    return f"M {ax} {ay} C {mx} {ay}, {mx} {by}, {bx} {by}"


nmap = {n["id"]: n for n in FLOW}
edges_svg = []
for a, b in FLOW_EDGES:
    cyclic = a == "decision" and b == "demanda"
    edges_svg.append(
        f'<path class="{"flecha ciclo" if cyclic else "flecha"}" d="{edge_d(nmap[a], nmap[b], cyclic)}" marker-end="url(#{ "arrowC" if cyclic else "arrow" })"/>'
    )
if True:
    edges_svg.append('<text class="lbl-ciclo" x="480" y="345">Ciclo de mejora continua</text>')

nodes_svg = []
for n in FLOW:
    nodes_svg.append(f'''<g class="nodo" data-id="{n['id']}" transform="translate({n['x']},{n['y']})">
      <rect class="hit" width="{n['w']}" height="{n['h']}" fill="transparent"/>
      <rect class="caja caja-{n['tipo']}" width="{n['w']}" height="{n['h']}" rx="10"/>
      <circle class="badge" cx="13" cy="13" r="10"/>
      <text class="badge-n" x="13" y="17">{n['n']}</text>
      <text class="fase" x="{n['w']/2}" y="20">{n['fase']}</text>
      <text class="tit" x="{n['w']/2}" y="38">{n['titulo']}</text>
    </g>''')

f0 = FLOW[0]
OBJETIVO_CLARO = (
    "Identificar tendencias y oportunidades en Ciencia, Tecnología e Innovación "
    "para el CMA, transformando información del entorno en insumos para la decisión institucional."
)

kpi_cards = "".join(
    f'''<article class="kpi" data-dim="{k['dim']}">
      <div class="kpi-top"><span class="kid">{k['id']}</span><span class="kdim">{DIM_LABEL[k['dim']]}</span></div>
      <h4>{k['nombre']}</h4>
      <p>{k['meta']}</p>
    </article>'''
    for k in KPIS
)

html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Observatorio CTi | Propuesta | CEITTO Colmayor</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet"/>
<style>
:root {{
  --bg:#f6faff; --surface:#fff; --alt:#eef4fc; --ink:#151c22; --charcoal:#2C3339;
  --mute:#4E5A64; --orange:#F39A1A; --teal:#00B3AF; --teal-deep:#006a67; --primary:#875200;
  --line:rgba(44,51,57,.12); --shadow:0 10px 28px rgba(44,51,57,.08);
  --r:12px; --font:"Inter",system-ui,sans-serif; --display:"Hanken Grotesk",Georgia,serif;
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;scroll-padding-top:72px}}
html{{scroll-behavior:smooth;scroll-padding-top:76px}}
body{{font-family:var(--font);background:var(--bg);color:var(--ink);font-size:17px;line-height:1.55;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
.wrap{{max-width:1140px;margin:0 auto;padding:0 clamp(.9rem,3vw,1.25rem)}}
nav{{position:fixed;inset:0 0 auto;z-index:100;background:rgba(44,51,57,.95);backdrop-filter:blur(12px);border-bottom:3px solid var(--orange)}}
nav .wrap{{height:64px;display:flex;align-items:center;justify-content:space-between;gap:1rem}}
.brand{{display:flex;align-items:center;gap:.65rem}}
.brand img{{height:40px}}
.brand b{{color:#fff;font-size:.88rem;display:block}}
.brand span{{color:rgba(255,255,255,.68);font-size:.7rem}}
.nav-links{{display:flex;gap:.15rem;flex-wrap:wrap}}
.nav-links a{{color:rgba(255,255,255,.75);text-decoration:none;font-size:.78rem;font-weight:500;padding:.35rem .5rem;border-radius:6px}}
.nav-links a:hover,.nav-links a.on{{color:#fff;background:rgba(255,255,255,.12)}}
.menu{{display:none;background:transparent;border:1px solid rgba(255,255,255,.3);color:#fff;padding:.35rem .6rem;border-radius:6px}}

/* HERO + animated “video-like” background */
.hero{{min-height:92vh;display:grid;place-items:end stretch;position:relative;overflow:hidden;color:#fff}}
.hero-media{{
  position:absolute;inset:-8%;
  background:url("media/hero-data.jpg") center/cover no-repeat;
  animation:drift 22s ease-in-out infinite alternate;
  will-change:transform;
}}
.hero-scan{{
  position:absolute;inset:0;pointer-events:none;opacity:.35;
  background:repeating-linear-gradient(180deg,transparent 0 3px,rgba(0,179,175,.07) 3px 4px);
  animation:scan 8s linear infinite;
}}
.hero-glow{{
  position:absolute;width:55%;height:55%;border-radius:50%;filter:blur(60px);opacity:.35;
  background:radial-gradient(circle,rgba(0,179,175,.55),transparent 70%);
  top:10%;right:5%;animation:pulse 7s ease-in-out infinite alternate;
}}
.hero-glow2{{
  position:absolute;width:40%;height:40%;border-radius:50%;filter:blur(50px);opacity:.28;
  background:radial-gradient(circle,rgba(243,154,26,.5),transparent 70%);
  bottom:5%;left:0;animation:pulse 9s ease-in-out infinite alternate-reverse;
}}
@keyframes drift{{from{{transform:scale(1.05) translate(0,0)}}to{{transform:scale(1.18) translate(-3%,2%)}}}}
@keyframes scan{{from{{transform:translateY(-8%)}}to{{transform:translateY(8%)}}}}
@keyframes pulse{{from{{opacity:.2;transform:scale(.95)}}to{{opacity:.42;transform:scale(1.08)}}}}
.hero-scrim{{
  position:absolute;inset:0;
  background:linear-gradient(115deg,rgba(21,28,34,.93) 0%,rgba(21,28,34,.72) 48%,rgba(21,28,34,.4) 100%),
             linear-gradient(180deg,rgba(21,28,34,.2),rgba(21,28,34,.88));
}}
.hero-inner{{position:relative;z-index:1;padding:8.5rem 0 3.5rem;width:100%}}
.chip{{display:inline-flex;align-items:center;gap:.45rem;background:rgba(243,154,26,.18);border:1px solid rgba(243,154,26,.4);color:#ffc56f;font-size:.78rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;padding:.4rem .8rem;border-radius:999px;margin-bottom:1.1rem}}
.chip i{{width:8px;height:8px;border-radius:50%;background:var(--orange);animation:pulse 1.6s ease-in-out infinite}}
.hero h1{{font-family:var(--display);font-weight:800;letter-spacing:-.03em;font-size:clamp(2.4rem,5vw,3.7rem);line-height:1.08;max-width:15ch;margin-bottom:1rem;text-shadow:0 2px 20px rgba(0,0,0,.35)}}
.hero h1 em{{font-style:normal;color:var(--orange)}}
.hero-lead{{font-size:1.12rem;color:rgba(255,255,255,.9);margin-bottom:.85rem;font-weight:500}}
.hero-obj{{font-size:1.08rem;color:rgba(255,255,255,.84);max-width:52ch;line-height:1.55;margin-bottom:2rem;border-left:3px solid var(--orange);padding-left:1rem}}
.hero-metrics{{display:grid;grid-template-columns:repeat(4,minmax(0,150px));gap:.7rem}}
.metric{{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.2);backdrop-filter:blur(10px);border-radius:var(--r);padding:1rem .85rem}}
.metric b{{display:block;font-family:var(--display);font-size:1.85rem;color:var(--orange);line-height:1}}
.metric span{{font-size:.8rem;color:rgba(255,255,255,.82)}}

section{{padding:4.5rem 0}}
.section-alt{{background:linear-gradient(180deg,var(--alt),var(--bg))}}
.kicker{{color:var(--teal);font-size:.8rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-bottom:.45rem}}
h2{{font-family:var(--display);font-size:clamp(1.7rem,2.8vw,2.2rem);letter-spacing:-.02em;color:var(--charcoal);margin-bottom:.4rem}}
.sub{{color:var(--mute);font-size:1.02rem;max-width:54ch;margin-bottom:1.6rem}}

.bento{{display:grid;gap:.85rem}}
.bento-4{{grid-template-columns:repeat(4,1fr)}}
.bento-3{{grid-template-columns:repeat(3,1fr)}}
.card{{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:1.2rem 1.1rem;box-shadow:var(--shadow);transition:.2s}}
.card:hover{{transform:translateY(-2px);border-color:rgba(0,179,175,.35)}}
.card .glyph{{width:42px;height:42px;border-radius:10px;display:grid;place-items:center;background:linear-gradient(145deg,rgba(0,179,175,.15),rgba(243,154,26,.1));color:var(--teal-deep);font-family:var(--display);font-weight:800;margin-bottom:.65rem}}
.card h3{{font-family:var(--display);font-size:1.05rem;margin-bottom:.3rem}}
.card p{{font-size:.92rem;color:var(--mute)}}
.obj-card{{cursor:pointer;text-align:left;font:inherit;color:inherit;width:100%}}
.obj-card.on{{border-top:3px solid var(--orange)}}
.obj-panel{{margin-top:1rem;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--teal);border-radius:var(--r);padding:1.1rem 1.25rem}}
.obj-panel strong{{display:block;font-family:var(--display);font-size:1.1rem;margin-bottom:.3rem}}
.obj-panel p{{font-size:1rem;color:var(--mute)}}

/* FLOW full width, no crop */
.flow-shell{{background:var(--surface);border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow);overflow:hidden}}
.flow-bar{{display:flex;justify-content:space-between;gap:.75rem;flex-wrap:wrap;padding:.75rem 1rem;border-bottom:1px solid var(--line);background:var(--alt);font-size:.85rem;color:var(--mute)}}
.flow-legend{{display:flex;gap:.85rem;flex-wrap:wrap}}
.flow-legend span{{display:inline-flex;align-items:center;gap:.35rem}}
.dot{{width:10px;height:10px;border-radius:3px}}
.flow-canvas{{width:100%;padding:.5rem .75rem 0;background:linear-gradient(180deg,#fbfdff,#eef4fc);overflow-x:auto;-webkit-overflow-scrolling:touch}}
#diagrama{{width:100%;height:auto;display:block;max-height:min(42vh,380px);min-width:0}}
.flecha{{fill:none;stroke:#7f93a6;stroke-width:1.6;opacity:.8}}
.flecha.ciclo{{stroke:var(--orange);stroke-dasharray:6 4;opacity:.75}}
.lbl-ciclo{{fill:var(--orange);font-size:11px;font-weight:700;text-anchor:middle;font-family:Inter,sans-serif}}
.nodo{{cursor:pointer}}
.nodo .caja{{stroke:var(--charcoal);stroke-width:1.4;transition:.15s}}
.nodo:hover .caja,.nodo.activo .caja{{stroke:var(--teal);stroke-width:2.4;filter:drop-shadow(0 4px 10px rgba(0,179,175,.25))}}
.nodo.activo .caja{{stroke:var(--orange)}}
.caja-entrada{{fill:#dff7f6}}.caja-proceso{{fill:#fff}}.caja-dato{{fill:#eef7e8}}.caja-salida{{fill:#fff4e5}}
.badge{{fill:var(--charcoal)}}.nodo.activo .badge{{fill:var(--orange)}}
.badge-n{{fill:#fff;font-size:9px;font-weight:700;text-anchor:middle;font-family:Inter,sans-serif}}
.fase{{fill:var(--mute);font-size:7.5px;font-weight:700;text-anchor:middle;text-transform:uppercase;font-family:Inter,sans-serif}}
.tit{{fill:var(--charcoal);font-size:11px;font-weight:700;text-anchor:middle;font-family:Inter,sans-serif}}
.flow-detail{{display:grid;grid-template-columns:56px 1fr;gap:.9rem;padding:1rem 1.15rem 1.2rem;border-top:1px solid var(--line)}}
.flow-step{{width:52px;height:52px;border-radius:12px;background:var(--charcoal);color:#fff;display:grid;place-items:center;font-family:var(--display);font-weight:800;font-size:1.2rem}}
.flow-detail h3{{font-family:var(--display);font-size:1.2rem;margin-bottom:.2rem}}
.flow-detail .proceso{{font-size:.98rem;margin-bottom:.7rem;font-weight:500}}
.flow-grid{{display:grid;grid-template-columns:1.2fr 1fr 1fr;gap:.65rem}}
.flow-box{{background:var(--alt);border-radius:10px;padding:.7rem .85rem;border:1px solid var(--line)}}
.flow-box h4{{font-size:.72rem;text-transform:uppercase;letter-spacing:.05em;color:var(--teal-deep);margin-bottom:.3rem}}
.flow-box ul{{margin-left:1rem;font-size:.88rem;color:var(--mute)}}
.flow-box p{{font-size:.88rem;color:var(--mute)}}

.plan{{display:grid;grid-template-columns:repeat(3,1fr);gap:.85rem}}
.plan-col{{background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:1.15rem;box-shadow:var(--shadow)}}
.plan-col header{{display:flex;align-items:center;gap:.65rem;margin-bottom:.8rem}}
.plan-col .ph{{width:42px;height:42px;border-radius:50%;background:var(--charcoal);color:#fff;display:grid;place-items:center;font-family:var(--display);font-weight:800;border:3px solid var(--orange);font-size:.9rem}}
.plan-col h3{{font-family:var(--display);font-size:1.1rem}}
.plan-col ul{{list-style:none;display:grid;gap:.35rem}}
.plan-col li{{font-size:.9rem;color:var(--mute);padding:.5rem .65rem;background:var(--alt);border-radius:8px;border-left:3px solid var(--teal)}}

.split{{display:grid;grid-template-columns:1fr 1fr;gap:.85rem}}
.know{{border-radius:14px;padding:1.4rem;color:#fff}}
.know.ex{{background:linear-gradient(145deg,#006a67,#00B3AF)}}
.know.ta{{background:linear-gradient(145deg,#875200,#F39A1A)}}
.know h3{{font-family:var(--display);font-size:1.25rem;margin-bottom:.7rem}}
.know ul{{list-style:none;display:grid;gap:.4rem}}
.know li{{font-size:.95rem;background:rgba(255,255,255,.14);padding:.65rem .8rem;border-radius:10px}}

.canal-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:.45rem}}
.canal-grid button{{border:1px solid var(--line);background:var(--surface);color:var(--ink);font:600 .88rem var(--font);padding:.7rem .8rem;border-radius:10px;cursor:pointer;text-align:left}}
.canal-grid button:hover,.canal-grid button.on{{background:var(--charcoal);color:#fff}}

.servicios{{display:grid;grid-template-columns:repeat(4,1fr);gap:.65rem}}
.svc{{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:1rem;text-align:left;font:inherit;color:inherit;cursor:pointer;box-shadow:var(--shadow)}}
.svc:hover,.svc.on{{border-left:3px solid var(--orange)}}
.svc b{{display:block;font-family:var(--display);font-size:1rem;margin-bottom:.25rem}}
.svc span{{font-size:.85rem;color:var(--mute)}}

/* VIZ Valor Plan Canales Servicios */
.valor-stage{{display:grid;grid-template-columns:1.05fr .95fr;gap:1.1rem;margin-top:1.4rem}}
.pillar-stack{{display:grid;gap:.7rem}}
.pillar-btn{{display:grid;grid-template-columns:56px 1fr;gap:.9rem;align-items:center;width:100%;text-align:left;font:inherit;color:inherit;cursor:pointer;border:1px solid var(--line);background:var(--surface);border-radius:16px;padding:1rem 1.1rem;box-shadow:var(--shadow);transition:.25s;position:relative;overflow:hidden}}
.pillar-btn::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--teal);transform:scaleY(0);transition:.25s}}
.pillar-btn:hover,.pillar-btn.on{{transform:translateX(4px);border-color:rgba(0,179,175,.4)}}
.pillar-btn.on{{background:var(--charcoal);color:#fff}}
.pillar-btn.on::before{{transform:scaleY(1);background:var(--orange)}}
.pillar-btn.on p{{color:rgba(255,255,255,.72)}}
.pillar-ico{{width:56px;height:56px;border-radius:14px;display:grid;place-items:center;background:linear-gradient(145deg,rgba(0,179,175,.18),rgba(243,154,26,.12));font-family:var(--display);font-weight:800;font-size:1.2rem;color:var(--teal-deep)}}
.pillar-btn.on .pillar-ico{{background:rgba(243,154,26,.2);color:var(--orange)}}
.pillar-btn h3{{font-family:var(--display);font-size:1.15rem;margin-bottom:.2rem}}
.pillar-btn p{{font-size:.92rem;color:var(--mute);margin:0}}
.valor-panel{{background:linear-gradient(160deg,var(--charcoal),#1a3338);color:#fff;border-radius:18px;padding:1.6rem 1.5rem;border-top:4px solid var(--orange);display:flex;flex-direction:column;justify-content:center;min-height:220px}}
.valor-panel .eyebrow{{color:var(--orange);font-size:.75rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;margin-bottom:.5rem}}
.valor-panel h3{{font-family:var(--display);font-size:1.45rem;margin-bottom:.55rem}}
.valor-panel p{{color:rgba(255,255,255,.78);font-size:1.02rem}}
.adv-rail{{display:grid;grid-template-columns:repeat(7,1fr);gap:.55rem;margin-top:1.1rem}}
.adv-chip{{border:1px solid var(--line);background:var(--surface);border-radius:14px;padding:1rem .65rem;cursor:pointer;text-align:center;font:inherit;color:inherit;transition:.25s;box-shadow:var(--shadow);min-height:110px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.45rem}}
.adv-chip:hover,.adv-chip.on{{background:var(--charcoal);color:#fff;transform:translateY(-4px);border-color:var(--charcoal)}}
.adv-chip .av{{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;background:rgba(0,179,175,.15);color:var(--teal-deep);font-family:var(--display);font-weight:800;font-size:.85rem}}
.adv-chip.on .av{{background:rgba(243,154,26,.25);color:var(--orange)}}
.adv-chip b{{font-family:var(--display);font-size:.82rem;line-height:1.2}}
.adv-chip span{{font-size:.72rem;color:var(--mute);line-height:1.25}}
.adv-chip.on span{{color:rgba(255,255,255,.7)}}
.adv-spotlight{{margin-top:.85rem;background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--teal);border-radius:12px;padding:1rem 1.2rem;display:none}}
.adv-spotlight.show{{display:block;animation:fadeUp .3s ease}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
.roadmap{{margin-top:1.5rem}}
.roadmap-track{{display:grid;grid-template-columns:repeat(3,1fr);gap:0;position:relative}}
.roadmap-track::before{{content:"";position:absolute;top:28px;left:12%;right:12%;height:3px;background:linear-gradient(90deg,var(--teal),var(--orange));opacity:.35;z-index:0}}
.road-step{{position:relative;z-index:1;background:transparent;border:none;cursor:pointer;padding:0 .4rem;text-align:center;font:inherit;color:inherit}}
.road-dot{{width:56px;height:56px;border-radius:50%;margin:0 auto .85rem;display:grid;place-items:center;background:var(--surface);border:3px solid var(--teal);font-family:var(--display);font-weight:800;color:var(--charcoal);box-shadow:var(--shadow);transition:.25s}}
.road-step:hover .road-dot,.road-step.on .road-dot{{background:var(--charcoal);color:#fff;border-color:var(--orange);transform:scale(1.08)}}
.road-step h3{{font-family:var(--display);font-size:1.15rem;margin-bottom:.25rem}}
.road-step .hint{{font-size:.82rem;color:var(--mute)}}
.road-panel{{margin-top:1.25rem;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:1.35rem 1.4rem;box-shadow:var(--shadow);display:grid;grid-template-columns:auto 1fr;gap:1.1rem}}
.road-badge{{width:64px;height:64px;border-radius:16px;background:var(--charcoal);color:#fff;display:grid;place-items:center;font-family:var(--display);font-weight:800;font-size:1.2rem;border-bottom:4px solid var(--orange)}}
.road-panel h3{{font-family:var(--display);font-size:1.25rem;margin-bottom:.75rem}}
.road-items{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:.5rem;list-style:none;padding:0}}
.road-items li{{font-size:.92rem;color:var(--mute);padding:.7rem .85rem;background:var(--alt);border-radius:10px;border-left:3px solid var(--teal);opacity:0;transform:translateY(8px);animation:fadeUp .35s ease forwards}}
.canal-stage{{display:grid;grid-template-columns:260px 1fr;gap:1.25rem;margin-top:1.4rem;align-items:center}}
.canal-hub{{aspect-ratio:1;border-radius:50%;background:var(--charcoal);color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:1.4rem;border:4px solid var(--orange);box-shadow:0 0 0 12px rgba(243,154,26,.08),var(--shadow);position:relative;overflow:hidden}}
.canal-hub::before{{content:"";position:absolute;inset:16%;border:1px dashed rgba(0,179,175,.35);border-radius:50%;animation:spinSlow 24s linear infinite}}
@keyframes spinSlow{{to{{transform:rotate(360deg)}}}}
.canal-hub .hub-label{{font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:var(--orange);font-weight:700;margin-bottom:.4rem;position:relative}}
.canal-hub h3{{font-family:var(--display);font-size:1.15rem;position:relative;line-height:1.25;margin-bottom:.35rem}}
.canal-hub p{{font-size:.86rem;color:rgba(255,255,255,.72);position:relative}}
.canal-mosaic{{display:grid;grid-template-columns:repeat(4,1fr);gap:.55rem}}
.canal-tile{{aspect-ratio:1.05;border:1px solid var(--line);background:var(--surface);border-radius:14px;cursor:pointer;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.45rem;font:inherit;color:inherit;transition:.25s;box-shadow:var(--shadow);padding:.55rem}}
.canal-tile:hover,.canal-tile.on{{background:linear-gradient(160deg,var(--charcoal),#163d3c);color:#fff;transform:translateY(-3px);border-color:transparent}}
.canal-tile .ci{{width:38px;height:38px;border-radius:11px;display:grid;place-items:center;background:linear-gradient(145deg,rgba(0,179,175,.16),rgba(243,154,26,.12));font-family:var(--display);font-weight:800;font-size:.85rem;color:var(--teal-deep)}}
.canal-tile.on .ci{{background:rgba(243,154,26,.25);color:var(--orange)}}
.canal-tile b{{font-family:var(--display);font-size:.8rem;text-align:center;line-height:1.2}}
.svc-mosaic{{display:grid;grid-template-columns:repeat(4,1fr);gap:.7rem;margin-top:1.3rem}}
.svc-tile{{position:relative;overflow:hidden;border:1px solid var(--line);background:var(--surface);border-radius:16px;padding:1.15rem;cursor:pointer;text-align:left;font:inherit;color:inherit;transition:.3s;box-shadow:var(--shadow);display:flex;flex-direction:column;justify-content:flex-end;min-height:138px}}
.svc-tile::after{{content:"";position:absolute;inset:auto -30% -50%;height:80%;background:radial-gradient(circle,rgba(0,179,175,.2),transparent 65%);transition:.35s}}
.svc-tile:nth-child(1),.svc-tile:nth-child(6){{grid-column:span 2;min-height:158px;background:linear-gradient(145deg,#2C3339,#006a67);color:#fff;border:none}}
.svc-tile:nth-child(1) span,.svc-tile:nth-child(6) span{{color:rgba(255,255,255,.75)}}
.svc-tile:nth-child(1) .sn,.svc-tile:nth-child(6) .sn{{color:var(--orange)}}
.svc-tile:hover,.svc-tile.on{{transform:translateY(-4px)}}
.svc-tile.on{{outline:2px solid var(--orange)}}
.svc-tile .sn{{position:relative;z-index:1;font-size:.68rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:.4rem}}
.svc-tile b{{position:relative;z-index:1;font-family:var(--display);font-size:1.1rem;margin-bottom:.25rem}}
.svc-tile span{{position:relative;z-index:1;font-size:.88rem;color:var(--mute)}}
.svc-detail{{margin-top:.85rem;padding:1rem 1.15rem;background:var(--alt);border-radius:12px;border-left:4px solid var(--orange);font-size:1rem;color:var(--mute);display:none}}
.svc-detail.show{{display:block;animation:fadeUp .3s ease}}

/* Problematica + Ventajas PDI */
.prob-stage{{display:grid;grid-template-columns:1fr 1.05fr;gap:1.1rem;margin-top:1.4rem;align-items:start}}
.prob-list{{display:grid;gap:.55rem}}
.prob-btn{{
  width:100%;text-align:left;font:inherit;color:inherit;cursor:pointer;border:1px solid var(--line);
  background:var(--surface);border-radius:14px;padding:.95rem 1rem;display:grid;grid-template-columns:48px 1fr;gap:.75rem;align-items:center;
  box-shadow:var(--shadow);transition:.22s;position:relative;overflow:hidden;
}}
.prob-btn::before{{content:"";position:absolute;left:0;top:0;bottom:0;width:4px;background:var(--orange);transform:scaleY(0);transition:.22s}}
.prob-btn.solucion::before{{background:var(--teal)}}
.prob-btn:hover,.prob-btn.on{{transform:translateX(3px);border-color:rgba(0,179,175,.35)}}
.prob-btn.on{{background:var(--charcoal);color:#fff}}
.prob-btn.on::before{{transform:scaleY(1)}}
.prob-btn.on .prob-meta{{color:rgba(255,255,255,.7)}}
.prob-id{{width:48px;height:48px;border-radius:12px;display:grid;place-items:center;font-family:var(--display);font-weight:800;background:rgba(243,154,26,.15);color:var(--primary)}}
.prob-btn.solucion .prob-id{{background:rgba(0,179,175,.15);color:var(--teal-deep)}}
.prob-btn.on .prob-id{{background:rgba(243,154,26,.25);color:var(--orange)}}
.prob-btn h3{{font-family:var(--display);font-size:1.02rem;margin-bottom:.15rem}}
.prob-meta{{font-size:.82rem;color:var(--mute)}}
.prob-panel{{
  background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:1.4rem 1.35rem;box-shadow:var(--shadow);
  border-top:4px solid var(--orange);min-height:280px;
}}
.prob-panel.solucion{{border-top-color:var(--teal)}}
.prob-panel .tag{{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--orange);margin-bottom:.55rem}}
.prob-panel.solucion .tag{{color:var(--teal-deep)}}
.prob-panel h3{{font-family:var(--display);font-size:1.35rem;margin-bottom:.55rem}}
.prob-panel p{{font-size:.98rem;color:var(--mute);margin-bottom:.75rem}}
.prob-panel .efecto{{background:var(--alt);border-radius:12px;padding:.85rem 1rem;border-left:3px solid var(--teal);font-size:.95rem;color:var(--ink)}}
.ctx-bar{{display:flex;flex-wrap:wrap;gap:.45rem;margin-top:1rem}}
.ctx-bar span{{font-size:.8rem;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:.35rem .75rem;color:var(--mute);font-weight:500}}
.pdi-stage{{margin-top:1.4rem}}
.pdi-tabs{{display:grid;grid-template-columns:repeat(4,1fr);gap:.55rem;margin-bottom:1rem}}
.pdi-tab{{
  border:1px solid var(--line);background:var(--surface);border-radius:14px;padding:1rem .85rem;cursor:pointer;
  text-align:left;font:inherit;color:inherit;transition:.22s;box-shadow:var(--shadow);min-height:108px;
}}
.pdi-tab:hover,.pdi-tab.on{{background:var(--charcoal);color:#fff;border-color:var(--charcoal);transform:translateY(-2px)}}
.pdi-tab .ln{{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:.35rem}}
.pdi-tab.on .ln{{color:var(--orange)}}
.pdi-tab h3{{font-family:var(--display);font-size:.95rem;line-height:1.25;margin-bottom:.3rem}}
.pdi-tab p{{font-size:.8rem;color:var(--mute);margin:0}}
.pdi-tab.on p{{color:rgba(255,255,255,.7)}}
.pdi-panel{{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:1.35rem;box-shadow:var(--shadow)}}
.pdi-panel h3{{font-family:var(--display);font-size:1.3rem;margin-bottom:.35rem}}
.pdi-panel .foco{{color:var(--mute);font-size:.95rem;margin-bottom:1rem}}
.pdi-inds{{display:grid;grid-template-columns:repeat(2,1fr);gap:.65rem;list-style:none;padding:0;margin:0}}
.pdi-inds li{{background:var(--alt);border-radius:12px;padding:1rem;border-top:3px solid var(--teal);opacity:0;transform:translateY(8px);animation:fadeUp .35s ease forwards}}
.pdi-inds li:nth-child(2),.pdi-inds li:nth-child(4){{border-top-color:var(--orange)}}
.pdi-inds b{{display:block;font-family:var(--display);font-size:.98rem;margin-bottom:.3rem;color:var(--charcoal)}}
.pdi-inds span{{font-size:.88rem;color:var(--mute)}}

/* Talento humano + escalado ConvocaRadar */
.talento-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:.85rem;margin-top:1.5rem}}
.persona{{
  position:relative;overflow:hidden;background:var(--surface);border:1px solid var(--line);border-radius:18px;
  padding:1.5rem 1.35rem 1.35rem;box-shadow:var(--shadow);transition:.25s;
}}
.persona::before{{content:"";position:absolute;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,var(--teal),var(--orange))}}
.persona:hover{{transform:translateY(-4px)}}
.persona .avatar{{
  width:64px;height:64px;border-radius:18px;display:grid;place-items:center;margin-bottom:.9rem;
  background:linear-gradient(145deg,var(--charcoal),#163d3c);color:var(--orange);
  font-family:var(--display);font-weight:800;font-size:1.3rem;border-bottom:3px solid var(--orange);
}}
.persona h3{{font-family:var(--display);font-size:1.15rem;line-height:1.25;margin-bottom:.3rem}}
.persona .rol{{font-size:.9rem;color:var(--mute);margin-bottom:.85rem;min-height:2.6em}}
.persona .dedica{{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--teal-deep);background:rgba(0,179,175,.12);padding:.3rem .6rem;border-radius:999px;margin-bottom:.75rem}}
.persona .cop{{font-family:var(--display);font-size:1.5rem;font-weight:800;color:var(--primary)}}
.persona .cop small{{display:block;font-family:var(--font);font-size:.75rem;font-weight:500;color:var(--mute);margin-top:.15rem}}
.persona .total{{
  margin-top:.85rem;padding-top:.85rem;border-top:1px dashed var(--line);
  font-family:var(--display);font-size:1.25rem;font-weight:800;color:var(--teal-deep);
}}
.persona .total small{{display:block;font-family:var(--font);font-size:.72rem;font-weight:500;color:var(--mute);margin-top:.15rem}}
.talento-totals{{
  display:grid;grid-template-columns:repeat(4,1fr);gap:.75rem;margin-top:1rem;
}}
.talento-tot{{
  background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:1rem 1.1rem;
  box-shadow:var(--shadow);border-top:3px solid var(--orange);
}}
.talento-tot.team{{border-top-color:var(--teal);background:linear-gradient(145deg,var(--charcoal),#163d3c);color:#fff}}
.talento-tot .lab{{font-size:.72rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--mute);margin-bottom:.35rem}}
.talento-tot.team .lab{{color:rgba(255,255,255,.7)}}
.talento-tot .val{{font-family:var(--display);font-size:1.2rem;font-weight:800;color:var(--primary)}}
.talento-tot.team .val{{color:var(--orange)}}
.talento-tot .hint{{font-size:.75rem;color:var(--mute);margin-top:.25rem}}
.talento-tot.team .hint{{color:rgba(255,255,255,.65)}}
@media(max-width:1000px){{.talento-totals{{grid-template-columns:1fr 1fr}}}}
@media(max-width:700px){{.talento-totals{{grid-template-columns:1fr}}}}
.talento-note{{
  margin-top:1rem;background:var(--alt);border:1px solid var(--line);border-left:4px solid var(--teal);
  border-radius:12px;padding:1rem 1.2rem;font-size:.95rem;color:var(--mute);
}}
.esc-stage{{display:grid;grid-template-columns:300px 1fr;gap:1rem;margin-top:1.5rem;align-items:start}}
.esc-steps{{display:grid;gap:.5rem}}
.esc-step{{
  width:100%;text-align:left;font:inherit;color:inherit;cursor:pointer;border:1px solid var(--line);
  background:var(--surface);border-radius:14px;padding:.9rem 1rem;display:grid;grid-template-columns:44px 1fr;gap:.7rem;
  align-items:center;box-shadow:var(--shadow);transition:.22s;position:relative;
}}
.esc-step:hover,.esc-step.on{{background:var(--charcoal);color:#fff;transform:translateX(4px)}}
.esc-step .num{{
  width:44px;height:44px;border-radius:12px;display:grid;place-items:center;font-family:var(--display);
  font-weight:800;background:rgba(0,179,175,.14);color:var(--teal-deep);
}}
.esc-step.on .num{{background:rgba(243,154,26,.25);color:var(--orange)}}
.esc-step h3{{font-family:var(--display);font-size:.98rem;margin-bottom:.1rem}}
.esc-step p{{font-size:.78rem;color:var(--mute);margin:0}}
.esc-step.on p{{color:rgba(255,255,255,.7)}}
.esc-panel{{
  background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:1.4rem 1.35rem;
  box-shadow:var(--shadow);border-top:4px solid var(--teal);min-height:320px;
}}
.esc-panel .fase-tag{{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--teal-deep);margin-bottom:.5rem}}
.esc-panel h3{{font-family:var(--display);font-size:1.35rem;margin-bottom:.65rem}}
.esc-acts{{list-style:none;display:grid;gap:.5rem;padding:0;margin:0 0 .9rem}}
.esc-acts li{{
  background:var(--alt);border-radius:10px;padding:.75rem .9rem;border-left:3px solid var(--teal);
  font-size:.93rem;color:var(--mute);opacity:0;transform:translateY(8px);animation:fadeUp .35s ease forwards;
}}
.esc-acts li:nth-child(2n){{border-left-color:var(--orange)}}
.esc-out{{
  background:linear-gradient(145deg,var(--charcoal),#163d3c);color:#fff;border-radius:12px;padding:.9rem 1.1rem;
  font-size:.93rem;border-left:4px solid var(--orange);
}}
.esc-out b{{color:var(--orange)}}
.talento-plat{{
  display:flex;flex-wrap:wrap;gap:.5rem;align-items:center;margin-top:1rem;
}}
.talento-plat a{{
  display:inline-flex;align-items:center;gap:.4rem;background:var(--charcoal);color:#fff;text-decoration:none;
  font-weight:600;font-size:.88rem;border-radius:999px;padding:.55rem 1rem;
}}
.talento-plat a:hover{{background:var(--teal-deep)}}
.talento-plat span{{font-size:.85rem;color:var(--mute)}}
@media(max-width:1000px){{.talento-grid{{grid-template-columns:1fr 1fr}}.esc-stage{{grid-template-columns:1fr}}}}
@media(max-width:700px){{.talento-grid{{grid-template-columns:1fr}}.esc-panel{{min-height:0}}}}



.hw-grid{{display:grid;grid-template-columns:1fr 1fr;gap:.85rem;margin-bottom:1rem;align-items:stretch}}
.hw,.hw.ups{{
  display:flex;flex-direction:column;height:100%;box-sizing:border-box;
}}
.hw-photo{{
  width:100%;height:220px;object-fit:contain;object-position:center;
  background:linear-gradient(145deg,#f4f7f7,#e8eeee);
  border-radius:12px;margin:0 0 1rem;display:block;border:1px solid var(--line);padding:.5rem;
}}
.hw ul{{flex:1 1 auto;margin-bottom:.85rem}}
.hw .price{{margin-top:auto}}
.hw-link{{
  display:inline-flex;align-items:center;gap:.35rem;margin-top:.55rem;font-size:.82rem;font-weight:600;
  color:var(--teal-deep);text-decoration:none;
}}
.hw-link:hover{{text-decoration:underline}}
.hw-usd{{font-size:.78rem;color:var(--mute);margin-top:.25rem}}
@media(max-width:800px){{.hw-photo{{height:180px}}}}


/* Exec summary */
.exec-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:.75rem;margin-top:1.2rem}}
.exec-card{{
  background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:1.1rem 1.15rem;
  box-shadow:var(--shadow);border-top:3px solid var(--teal);
}}
.exec-card:nth-child(3n+2){{border-top-color:var(--orange)}}
.exec-card h3{{font-family:var(--display);font-size:1.05rem;margin-bottom:.35rem}}
.exec-card p{{font-size:.9rem;color:var(--mute);margin:0;line-height:1.4}}
.gantt-wrap{{margin-top:1.2rem;background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:1.1rem 1.15rem;box-shadow:var(--shadow)}}
.gantt-head{{display:flex;justify-content:space-between;align-items:baseline;gap:1rem;margin-bottom:.85rem;flex-wrap:wrap}}
.gantt-head h3{{font-family:var(--display);font-size:1.2rem;margin:0}}
.gantt-head .rango{{font-size:.85rem;color:var(--mute)}}
.gantt-months{{display:grid;grid-template-columns:220px 1fr;gap:.5rem;margin-bottom:.35rem}}
.gantt-months .lab{{font-size:.72rem;color:transparent}}
.gantt-months .track{{display:grid;grid-template-columns:31fr 30fr 31fr 30fr 18fr;gap:0;border-bottom:1px solid var(--line)}}
.gantt-months .track span{{
  text-align:center;font-size:.72rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
  color:var(--teal-deep);padding:.35rem 0;border-left:1px dashed rgba(0,0,0,.08);
}}
.gantt-months .track span:first-child{{border-left:none}}
.gantt-rows{{display:grid;gap:.4rem}}
.gantt-row{{
  display:grid;grid-template-columns:220px 1fr;gap:.5rem;align-items:center;cursor:pointer;
  border:1px solid transparent;border-radius:10px;padding:.2rem .25rem;transition:.2s;
}}
.gantt-row:hover,.gantt-row.on{{background:var(--alt);border-color:var(--line)}}
.gantt-row .meta h4{{font-size:.88rem;margin:0 0 .1rem;font-family:var(--display);line-height:1.2}}
.gantt-row .meta p{{font-size:.72rem;color:var(--mute);margin:0}}
.gantt-bar-track{{
  position:relative;height:34px;background:rgba(0,0,0,.03);border-radius:8px;overflow:hidden;
  border:1px solid var(--line);
}}
.gantt-bar{{
  position:absolute;top:5px;height:22px;border-radius:7px;background:linear-gradient(90deg,var(--teal),var(--teal-deep));
  box-shadow:0 2px 6px rgba(0,100,90,.25);display:flex;align-items:center;padding:0 .55rem;
  color:#fff;font-size:.68rem;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;
  transition:transform .2s, filter .2s;
}}
.gantt-row:nth-child(2n) .gantt-bar{{background:linear-gradient(90deg,var(--orange),#c45c26)}}
.gantt-row.on .gantt-bar{{transform:scaleY(1.12);filter:brightness(1.08)}}
.gantt-panel{{
  margin-top:.9rem;background:linear-gradient(145deg,var(--charcoal),#163d3c);color:#fff;
  border-radius:12px;padding:1rem 1.15rem;border-left:4px solid var(--orange);min-height:120px;
}}
.gantt-panel .tag{{font-size:.68rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--orange)}}
.gantt-panel h4{{font-family:var(--display);font-size:1.15rem;margin:.25rem 0 .4rem}}
.gantt-panel .desc{{font-size:.9rem;color:rgba(255,255,255,.78);margin:0 0 .65rem}}
.gantt-panel .ent{{list-style:none;padding:0;margin:0;display:grid;gap:.35rem}}
.gantt-panel .ent li{{
  background:rgba(255,255,255,.08);border-radius:8px;padding:.5rem .7rem;font-size:.86rem;
  border-left:3px solid var(--teal);
}}
.gantt-panel .ent li b{{color:var(--orange)}}
.gantt-legend{{display:flex;gap:1rem;flex-wrap:wrap;margin-top:.75rem;font-size:.78rem;color:var(--mute)}}
.gantt-legend i{{display:inline-block;width:14px;height:10px;border-radius:3px;margin-right:.35rem;vertical-align:middle}}
.gantt-legend .a{{background:var(--teal)}}
.gantt-legend .b{{background:var(--orange)}}
@media(max-width:900px){{
  .gantt-months,.gantt-row{{grid-template-columns:1fr}}
  .gantt-months .lab,.gantt-row .meta{{margin-bottom:.25rem}}
}}
.min-list{{display:grid;grid-template-columns:1fr 1fr;gap:.45rem;list-style:none;padding:0;margin:1rem 0 0}}
.min-list li{{background:var(--alt);border-radius:10px;padding:.7rem .85rem;border-left:3px solid var(--teal);font-size:.9rem;color:var(--mute)}}
.qs-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:.7rem;margin-top:1.1rem}}
.qs-card{{
  background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:1.1rem;box-shadow:var(--shadow);
}}
.qs-card .st{{font-size:.68rem;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--teal-deep)}}
.qs-card h3{{font-family:var(--display);font-size:1.05rem;margin:.35rem 0}}
.qs-card p{{font-size:.88rem;color:var(--mute);margin:0}}
.ali-grid{{display:grid;grid-template-columns:1fr 1fr;gap:.75rem;margin-top:1.1rem}}
.ali-card{{
  background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:1.15rem;box-shadow:var(--shadow);
  display:flex;flex-direction:column;gap:.4rem;
}}
.ali-card .tag{{align-self:flex-start;font-size:.68rem;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
  background:rgba(0,179,175,.12);color:var(--teal-deep);padding:.25rem .55rem;border-radius:999px}}
.ali-card h3{{font-family:var(--display);font-size:1.1rem;margin:0}}
.ali-card p{{font-size:.9rem;color:var(--mute);margin:0;flex:1}}
.ali-card a{{font-size:.85rem;font-weight:600;color:var(--teal-deep);text-decoration:none}}
.ali-card a:hover{{text-decoration:underline}}
.plan-exec{{display:grid;grid-template-columns:repeat(3,1fr);gap:.7rem;margin-top:1rem}}
.plan-exec article{{background:var(--alt);border-radius:12px;padding:1rem;border-top:3px solid var(--orange)}}
.plan-exec .n{{font-size:.72rem;font-weight:800;color:var(--orange)}}
.plan-exec h3{{font-family:var(--display);font-size:1.05rem;margin:.2rem 0 .5rem}}
.plan-exec ul{{list-style:none;padding:0;margin:0;display:grid;gap:.3rem}}
.plan-exec li{{font-size:.86rem;color:var(--mute)}}
.two-col{{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.2rem}}
@media(max-width:1000px){{
  .exec-grid,.qs-grid,.plan-exec
  .ali-grid,.two-col,.min-list{{grid-template-columns:1fr}}
}}
@media(max-width:700px){{
  .exec-grid,.qs-grid,.plan-exec
}}

/* Agenda institucional L1/L2/L4 + riesgos */
.agenda-stage{{margin-top:1.4rem}}
.agenda-tabs{{display:grid;grid-template-columns:repeat(4,1fr);gap:.55rem;margin-bottom:1rem}}
.agenda-tab{{
  border:1px solid var(--line);background:var(--surface);border-radius:14px;padding:1rem .85rem;
  cursor:pointer;text-align:left;font:inherit;color:inherit;transition:.22s;box-shadow:var(--shadow);min-height:112px;
}}
.agenda-tab:hover,.agenda-tab.on{{background:var(--charcoal);color:#fff;border-color:var(--charcoal);transform:translateY(-2px)}}
.agenda-tab .ln{{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:.35rem}}
.agenda-tab.on .ln{{color:var(--orange)}}
.agenda-tab h3{{font-family:var(--display);font-size:.95rem;line-height:1.25;margin-bottom:.3rem}}
.agenda-tab p{{font-size:.8rem;color:var(--mute);margin:0}}
.agenda-tab.on p{{color:rgba(255,255,255,.7)}}
.agenda-panel{{
  background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:1.35rem 1.4rem;
  box-shadow:var(--shadow);border-top:4px solid var(--teal);min-height:380px;
}}
.agenda-panel .foco{{color:var(--mute);margin:.35rem 0 1rem;font-size:.95rem}}
.agenda-grid{{display:grid;grid-template-columns:1.1fr 1fr;gap:1rem}}
.agenda-block h4{{
  font-family:var(--display);font-size:1rem;margin:0 0 .55rem;display:flex;align-items:center;gap:.4rem;
}}
.agenda-block h4 span{{
  font-family:var(--font);font-size:.68rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
  background:rgba(0,179,175,.12);color:var(--teal-deep);padding:.2rem .5rem;border-radius:999px;
}}
.agenda-list{{list-style:none;padding:0;margin:0 0 .9rem;display:grid;gap:.4rem}}
.agenda-list li{{
  background:var(--alt);border-radius:10px;padding:.65rem .8rem;font-size:.88rem;color:var(--mute);
  border-left:3px solid var(--teal);
}}
.agenda-list li.yr{{border-left-color:var(--orange)}}
.agenda-list li b{{color:var(--ink);font-weight:700}}
.agenda-list li .yr-tag{{
  display:inline-block;font-size:.68rem;font-weight:700;color:var(--orange);margin-right:.35rem;
}}
.kpi-mini{{display:grid;grid-template-columns:1fr 1fr;gap:.5rem;margin-bottom:.9rem}}
.kpi-mini .k{{
  background:var(--alt);border-radius:12px;padding:.75rem .8rem;border-top:3px solid var(--teal);
}}
.kpi-mini .k:nth-child(2n){{border-top-color:var(--orange)}}
.kpi-mini .cod{{font-size:.68rem;font-weight:700;letter-spacing:.04em;color:var(--teal-deep)}}
.kpi-mini .kt{{font-size:.86rem;font-weight:600;margin:.2rem 0 .35rem;line-height:1.25}}
.kpi-mini .meta{{font-size:.75rem;color:var(--mute)}}
.kpi-mini .log{{font-family:var(--display);font-size:1.05rem;font-weight:800;color:var(--primary)}}
.dom-row{{display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem;margin-bottom:.9rem}}
.dom-card{{
  background:linear-gradient(145deg,var(--charcoal),#163d3c);color:#fff;border-radius:12px;padding:.8rem .85rem;
  border-left:3px solid var(--orange);
}}
.dom-card b{{display:block;color:var(--orange);font-size:.82rem;margin-bottom:.25rem}}
.dom-card span{{font-size:.78rem;color:rgba(255,255,255,.78);line-height:1.35}}
.risk-grid{{display:grid;grid-template-columns:1fr 1fr;gap:.45rem;margin-bottom:.9rem}}
.risk-item{{
  background:var(--alt);border-radius:10px;padding:.7rem .8rem;border-left:3px solid #c45c26;
}}
.risk-item .rz{{
  display:inline-block;font-size:.65rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;
  color:#fff;background:#c45c26;padding:.15rem .4rem;border-radius:4px;margin-bottom:.3rem;
}}
.risk-item .rz.Clave{{background:var(--teal-deep)}}
.risk-item .rz.Alta{{background:#b45309}}
.risk-item .rz.Extrema{{background:#9f1239}}
.risk-item b{{display:block;font-size:.86rem;margin-bottom:.2rem}}
.risk-item span{{font-size:.78rem;color:var(--mute)}}
.agenda-aporte{{
  margin-top:.4rem;background:linear-gradient(145deg,var(--charcoal),#163d3c);color:#fff;
  border-radius:12px;padding:.9rem 1.1rem;font-size:.92rem;border-left:4px solid var(--orange);
}}
.agenda-aporte b{{color:var(--orange)}}
.agenda-legend{{
  display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1rem;align-items:center;
}}
.agenda-legend .pill{{
  font-size:.72rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
  padding:.35rem .7rem;border-radius:999px;border:1px solid var(--line);background:var(--surface);
}}
.agenda-legend .pill.off{{border-color:var(--teal);color:var(--teal-deep)}}
.agenda-legend .pill.rep{{border-color:var(--orange);color:#b45309}}
.agenda-legend .pill.prop{{border-color:var(--mute);color:var(--mute)}}
.agenda-legend .note{{font-size:.82rem;color:var(--mute)}}
.agenda-src{{
  margin-top:.85rem;font-size:.8rem;color:var(--mute);border-top:1px dashed var(--line);padding-top:.7rem;
}}
.agenda-src a{{color:var(--teal-deep);font-weight:600}}
@media(max-width:1100px){{
  .agenda-tabs{{grid-template-columns:1fr 1fr}}
  .agenda-grid{{grid-template-columns:1fr}}
  .dom-row{{grid-template-columns:1fr}}
  .risk-grid{{grid-template-columns:1fr}}
}}
@media(max-width:700px){{
  .agenda-tabs{{grid-template-columns:1fr}}
  .kpi-mini{{grid-template-columns:1fr}}
}}

/* KPIs */
.kpi-tabs{{display:flex;gap:.4rem;flex-wrap:wrap;margin-bottom:1.1rem}}
.kpi-tab{{border:1px solid var(--line);background:var(--surface);color:var(--mute);padding:.45rem .85rem;border-radius:999px;cursor:pointer;font:600 .85rem var(--font)}}
.kpi-tab.on{{background:var(--teal);color:#fff;border-color:var(--teal)}}
.kpi-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:.65rem}}
.kpi{{background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:1rem;box-shadow:var(--shadow);border-top:3px solid var(--teal);transition:.2s}}
.kpi[data-dim="roi"]{{border-top-color:var(--orange)}}
.kpi[data-dim="sostenibilidad"]{{border-top-color:var(--primary)}}
.kpi[data-dim="operativa"]{{border-top-color:var(--teal-deep)}}
.kpi:hover{{transform:translateY(-2px)}}
.kpi-top{{display:flex;justify-content:space-between;align-items:center;margin-bottom:.4rem}}
.kid{{font-size:.72rem;font-weight:700;color:var(--orange)}}
.kdim{{font-size:.68rem;color:var(--mute);text-transform:uppercase;letter-spacing:.04em}}
.kpi h4{{font-size:.95rem;font-family:var(--display);margin-bottom:.3rem;line-height:1.3}}
.kpi p{{font-size:.88rem;color:var(--teal-deep);font-weight:600}}

/* Hardware + budget */
.hw-grid{{display:grid;grid-template-columns:1fr 1fr;gap:.85rem;margin-bottom:1rem;align-items:stretch}}
.hw,.hw.ups{{display:flex;flex-direction:column;height:100%;box-sizing:border-box;background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:1.25rem;box-shadow:var(--shadow)}}
.hw .tag{{display:inline-block;font-size:.7rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--teal);background:rgba(0,179,175,.12);padding:.25rem .55rem;border-radius:6px;margin-bottom:.55rem}}
.hw.ups .tag{{color:var(--primary);background:rgba(243,154,26,.12)}}
.hw h3{{font-family:var(--display);font-size:1.15rem;margin-bottom:.65rem}}
.hw ul{{list-style:none;display:grid;gap:.35rem;margin-bottom:.75rem;flex:1 1 auto}}
.hw li{{font-size:.9rem;color:var(--mute);padding:.35rem 0;border-bottom:1px solid var(--line)}}
.hw .price{{font-family:var(--display);font-size:1.35rem;color:var(--primary);font-weight:800;margin-top:auto}}
.budget{{background:var(--charcoal);color:#fff;border-radius:16px;padding:1.5rem;border-top:4px solid var(--orange)}}
.budget .total{{font-family:var(--display);font-size:clamp(2rem,3vw,2.6rem);color:var(--orange);margin:.2rem 0 1rem}}
.budget-row{{display:grid;grid-template-columns:1fr auto auto;gap:.75rem;align-items:center;padding:.55rem 0;border-bottom:1px solid rgba(255,255,255,.1);font-size:.92rem}}
.budget-row:last-child{{border-bottom:none}}
.budget-row .bar{{height:6px;background:rgba(255,255,255,.12);border-radius:999px;overflow:hidden;margin-top:.35rem}}
.budget-row .fill{{height:100%;background:linear-gradient(90deg,var(--teal),var(--orange))}}

.lineas{{display:grid;grid-template-columns:repeat(3,1fr);gap:.85rem}}
.linea{{border-radius:14px;padding:1.4rem;color:#fff;min-height:120px}}
.linea:nth-child(1){{background:linear-gradient(150deg,#2C3339,#006a67)}}
.linea:nth-child(2){{background:linear-gradient(150deg,#2C3339,#875200)}}
.linea:nth-child(3){{background:linear-gradient(150deg,#2C3339,#00B3AF)}}
.linea h3{{font-family:var(--display);font-size:1.15rem;margin-bottom:.3rem}}
.linea p{{opacity:.8;font-size:.92rem}}

.estudios{{display:none}}
.tray-section{{padding:4.5rem 0 5rem;background:linear-gradient(165deg,#1a2228 0%,#2C3339 45%,#163d3c 100%);color:#fff;position:relative;overflow:hidden}}
.tray-section::before{{content:"";position:absolute;inset:auto -20% -40% 40%;height:70%;background:radial-gradient(circle,rgba(243,154,26,.22),transparent 60%);pointer-events:none}}
.tray-section::after{{content:"";position:absolute;top:0;left:0;right:0;height:4px;background:linear-gradient(90deg,var(--teal),var(--orange))}}
.tray-section .kicker{{color:var(--orange)}}
.tray-section h2{{color:#fff;font-size:clamp(1.9rem,3.4vw,2.8rem);max-width:16ch}}
.tray-section .sub{{color:rgba(255,255,255,.72);max-width:42rem}}
.tray-stats{{display:grid;grid-template-columns:repeat(4,1fr);gap:.7rem;margin:1.5rem 0 1.6rem}}
.tray-stat{{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:1rem 1.05rem;backdrop-filter:blur(6px)}}
.tray-stat b{{display:block;font-family:var(--display);font-size:1.7rem;color:var(--orange);line-height:1.1}}
.tray-stat span{{font-size:.82rem;color:rgba(255,255,255,.68)}}
.tray-rail{{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:.45rem;margin-bottom:1.1rem}}
.tray-chip{{
  border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.05);color:#fff;border-radius:14px;
  padding:.85rem .6rem;cursor:pointer;text-align:left;font:inherit;transition:.25s;min-height:92px;
}}
.tray-chip:hover,.tray-chip.on{{background:#fff;color:var(--charcoal);transform:translateY(-3px);border-color:#fff}}
.tray-chip .n{{display:block;font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal);margin-bottom:.25rem}}
.tray-chip.on .n{{color:var(--orange)}}
.tray-chip b{{display:block;font-family:var(--display);font-size:.86rem;line-height:1.2;margin-bottom:.2rem}}
.tray-chip span{{font-size:.72rem;color:rgba(255,255,255,.6);line-height:1.25}}
.tray-chip.on span{{color:var(--mute)}}
.tray-stage{{display:grid;grid-template-columns:1.15fr .85fr;gap:1rem;align-items:stretch}}
.tray-preview{{
  position:relative;border-radius:18px;overflow:hidden;min-height:380px;background:#0f1418;
  border:1px solid rgba(255,255,255,.12);box-shadow:0 20px 50px rgba(0,0,0,.35);
}}
.tray-preview iframe{{width:100%;height:100%;min-height:380px;border:0;background:#fff}}
.tray-fallback{{
  position:absolute;inset:0;display:flex;flex-direction:column;align-items:flex-start;justify-content:flex-end;
  padding:1.5rem;background:
    linear-gradient(180deg,rgba(15,20,24,.15),rgba(15,20,24,.92)),
    radial-gradient(circle at 80% 20%,rgba(0,179,175,.35),transparent 45%),
    radial-gradient(circle at 20% 80%,rgba(243,154,26,.3),transparent 40%);
}}
.tray-fallback .badge{{font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--orange);margin-bottom:.55rem}}
.tray-fallback h3{{font-family:var(--display);font-size:1.45rem;margin-bottom:.4rem}}
.tray-fallback p{{color:rgba(255,255,255,.75);font-size:.95rem;margin-bottom:1rem;max-width:34ch}}
.tray-fallback a,.tray-ev a,.tray-side a.cta-ev{{
  display:inline-flex;align-items:center;gap:.4rem;background:var(--orange);color:#1a2228;font-weight:700;
  text-decoration:none;border-radius:999px;padding:.65rem 1.05rem;font-size:.9rem;
}}
.tray-side{{
  background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:18px;padding:1.35rem 1.3rem;
  display:flex;flex-direction:column;gap:.75rem;
}}
.tray-side .tag{{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--teal)}}
.tray-side h3{{font-family:var(--display);font-size:1.45rem;line-height:1.2}}
.tray-side .metric-row{{display:flex;align-items:baseline;gap:.55rem}}
.tray-side .metric-row b{{font-family:var(--display);font-size:2.4rem;color:var(--orange);line-height:1}}
.tray-side .metric-row span{{color:rgba(255,255,255,.65);font-size:.9rem}}
.tray-side p{{color:rgba(255,255,255,.75);font-size:.95rem}}
.tray-ev{{display:grid;gap:.45rem;margin-top:.35rem}}
.tray-ev button,.tray-ev a.chip{{
  width:100%;text-align:left;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.05);
  color:#fff;border-radius:12px;padding:.7rem .85rem;cursor:pointer;font:inherit;display:flex;justify-content:space-between;gap:.5rem;align-items:center;text-decoration:none;
}}
.tray-ev button:hover,.tray-ev button.on,.tray-ev a.chip:hover{{background:#fff;color:var(--charcoal)}}
.tray-ev .kind{{font-size:.68rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;opacity:.7}}
@media(max-width:1100px){{
  .tray-rail{{grid-template-columns:repeat(4,minmax(0,1fr))}}
  .tray-stats{{grid-template-columns:1fr 1fr}}
  .nav-links a{{font-size:.72rem;padding:.3rem .4rem}}
}}
@media(max-width:1000px){{
  .valor-stage,.roadmap-track,.canal-stage,.svc-mosaic,.canal-mosaic,.prob-stage,.pdi-inds,
  .bento-4,.bento-3,.plan,.split,.lineas,.piloto,.hero-metrics,.flow-grid,.servicios,.hw-grid,
  .adv-rail{{grid-template-columns:1fr 1fr}}
  .pdi-tabs{{grid-template-columns:1fr 1fr}}
  .svc-tile:nth-child(1),.svc-tile:nth-child(6){{grid-column:span 1}}
  .canal-mosaic{{grid-template-columns:repeat(3,1fr)}}
  .roadmap-track::before{{display:none}}
  .servicios{{grid-template-columns:1fr 1fr}}
  .budget-row{{grid-template-columns:1fr auto;gap:.4rem .75rem}}
  .budget-row span{{grid-column:2;justify-self:end}}
}}
@media(max-width:900px){{
  .nav-links{{display:none;position:absolute;top:64px;left:0;right:0;background:var(--charcoal);padding:.85rem 1rem 1.1rem;flex-direction:column;gap:.15rem;border-bottom:3px solid var(--orange);max-height:calc(100vh - 64px);overflow-y:auto}}
  .nav-links.open{{display:flex}}
  .nav-links a{{font-size:.95rem;padding:.7rem .75rem}}
  .menu{{display:inline-flex;align-items:center;gap:.35rem;cursor:pointer;font:600 .85rem var(--font)}}
  .tray-stage{{grid-template-columns:1fr}}
  .tray-rail{{
    display:flex;grid-template-columns:none;overflow-x:auto;gap:.5rem;padding-bottom:.55rem;
    scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;
  }}
  .tray-chip{{min-width:158px;flex:0 0 158px;scroll-snap-align:start;min-height:88px}}
  .tray-preview,.tray-preview iframe{{min-height:280px}}
  .prob-stage{{grid-template-columns:1fr}}
  .adv-rail{{
    display:flex;grid-template-columns:none;overflow-x:auto;gap:.5rem;padding-bottom:.4rem;
    scroll-snap-type:x mandatory;-webkit-overflow-scrolling:touch;
  }}
  .adv-chip{{min-width:120px;flex:0 0 120px;scroll-snap-align:start}}
}}
@media(max-width:700px){{
  body{{font-size:16px}}
  .bento-4,.bento-3,.plan,.split,.lineas,.piloto,.hero-metrics,.flow-grid,.servicios,.hw-grid,
  .pdi-tabs,.pdi-inds,.canal-stage,.canal-mosaic,.svc-mosaic,.valor-stage,.roadmap-track,.road-panel,
  .prob-stage,.tray-stats{{grid-template-columns:1fr}}
  .hero{{min-height:auto}}
  .hero-inner{{padding:6.5rem 0 2.4rem}}
  .hero h1{{max-width:none;font-size:clamp(1.75rem,8vw,2.4rem)}}
  .hero-metrics{{grid-template-columns:1fr 1fr;max-width:100%}}
  .metric{{padding:.85rem .7rem}}
  .metric b{{font-size:1.45rem}}
  .hero-obj{{font-size:1rem;margin-bottom:1.4rem}}
  .section-alt,section{{padding-top:3.2rem;padding-bottom:3.2rem}}
  .flow-detail{{grid-template-columns:1fr}}
  .flow-bar{{font-size:.78rem}}
  #diagrama{{max-height:none;min-width:780px}}
  .flow-canvas{{padding-bottom:.5rem}}
  .budget{{padding:1.15rem}}
  .budget .total{{font-size:clamp(1.6rem,8vw,2.2rem)}}
  .budget-row{{grid-template-columns:1fr;gap:.25rem}}
  .budget-row span,.budget-row strong{{justify-self:start}}
  .cta{{padding:3rem 0}}
  .cta blockquote{{padding:0 .25rem}}
  .tray-section{{padding:3.2rem 0 3.6rem}}
  .tray-stat b{{font-size:1.35rem}}
  .pdi-tab{{min-height:0}}
  .prob-panel{{min-height:0}}
  .canal-hub{{max-width:220px;margin:0 auto}}
  .marquee-track{{gap:1.25rem;animation-duration:36s}}
}}
@media(max-width:420px){{
  .hero-metrics{{gap:.45rem}}
  .brand b{{font-size:.9rem}}
  .brand span{{font-size:.68rem}}
  .tray-chip{{min-width:140px;flex-basis:140px}}
}}

.piloto{{display:grid;grid-template-columns:.8fr 1.2fr;gap:1rem}}
.piloto-visual{{border-radius:14px;min-height:200px;background:url("media/hero-data.jpg") center/cover;position:relative}}
.piloto-visual::after{{content:"PILOTO";position:absolute;left:1rem;bottom:1rem;font-family:var(--display);font-weight:800;color:#fff;letter-spacing:.08em;background:rgba(44,51,57,.8);padding:.4rem .7rem;border-radius:8px;border-left:3px solid var(--orange);font-size:.9rem}}
.piloto-copy{{border-radius:14px;background:var(--charcoal);color:#fff;padding:1.75rem;display:flex;flex-direction:column;justify-content:center}}
.piloto-copy h3{{font-family:var(--display);font-size:1.3rem;line-height:1.3;margin-bottom:.6rem}}
.piloto-copy p{{color:rgba(255,255,255,.75);font-size:.98rem}}

.cta{{padding:4.2rem 0;text-align:center;background:var(--charcoal);border-top:4px solid var(--orange)}}
.cta blockquote{{font-family:var(--display);font-size:clamp(1.3rem,2.4vw,1.75rem);color:#fff;max-width:22em;margin:0 auto;line-height:1.35}}
.cta strong{{color:var(--orange)}}
.cta cite{{display:block;margin-top:1rem;font-style:normal;font-size:1rem;color:rgba(255,255,255,.68);font-family:var(--font)}}

.progress{{position:fixed;top:64px;left:0;height:3px;width:0;z-index:101;background:linear-gradient(90deg,var(--teal),var(--orange))}}
.reveal{{opacity:0;transform:translateY(16px);transition:.5s}}.reveal.on{{opacity:1;transform:none}}
.marquee{{overflow:hidden;border-block:1px solid var(--line);background:var(--surface)}}
.marquee-track{{display:flex;gap:2rem;width:max-content;padding:.9rem 0;animation:marquee 28s linear infinite}}
.marquee-track span{{font-family:var(--display);font-weight:700;font-size:.9rem;color:var(--mute)}}
@keyframes marquee{{to{{transform:translateX(-50%)}}}}

</style>
</head>
<body>
<div class="progress" id="bar"></div>
<nav>
  <div class="wrap">
    <div class="brand">
      <img src="logo-colmayor-blanco.png" alt="Colmayor"/>
      <div><b>Observatorio CTi</b><span>CEITTO · Colmayor</span></div>
    </div>
    <button class="menu" id="menu" type="button">Menú</button>
    <div class="nav-links" id="links">
      <a href="#inicio">Inicio</a>
      <a href="#beneficios">Beneficios</a>
      <a href="#computo">Cómputo</a>
      <a href="#flujo">Flujo</a>
      <a href="#kpis">KPIs</a>
      <a href="#plan">Plan 2026-2</a>
      <a href="#talento">Equipo</a>
      <a href="#alianzas">Alianzas</a>
      <a href="#estudios">Trayectoria</a>
      <a href="#hardware">Presupuesto</a>
      <a href="#sigue">Qué sigue</a>
    </div>
  </div>
</nav>

<header class="hero" id="inicio">
  <div class="hero-media" aria-hidden="true"></div>
  <div class="hero-glow" aria-hidden="true"></div>
  <div class="hero-glow2" aria-hidden="true"></div>
  <div class="hero-scan" aria-hidden="true"></div>
  <div class="hero-scrim" aria-hidden="true"></div>
  <div class="hero-inner">
    <div class="wrap">
      <div class="chip"><i></i> Observatorio de Ciencia, Tecnología e Innovación</div>
      <h1>De datos del entorno a <em>decisión</em> estratégica</h1>
      <p class="hero-lead">Versión ejecutiva · 2026-2 · CEITTO Colmayor</p>
      <p class="hero-obj"><strong>Objetivo:</strong> {OBJETIVO_CLARO}</p>
      <div class="hero-metrics">
        <div class="metric"><b>4</b><span>Objetivos</span></div>
        <div class="metric"><b>10</b><span>Etapas</span></div>
        <div class="metric"><b>20</b><span>KPIs MVP</span></div>
        <div class="metric"><b>{round(PRESUPUESTO['total']/1_000_000, 1):g}M</b><span>Presupuesto MVP</span></div>
      </div>
    </div>
  </div>
</header>


<section id="beneficios" class="section-alt">
  <div class="wrap reveal">
    <p class="kicker">Valor ejecutivo</p>
    <h2>Beneficios de adoptar el Observatorio</h2>
    <p class="sub">Resumen alineado al Plan de Desarrollo 2024-2028 (L1, L2 y L4) y a la operación CEITTO.</p>
    <div class="exec-grid">
      {''.join(f'<article class="exec-card"><h3>{b["t"]}</h3><p>{b["d"]}</p></article>' for b in BENEFICIOS_EXEC)}
    </div>
  </div>
</section>

<section id="computo">
  <div class="wrap reveal">
    <p class="kicker">Infraestructura solicitada</p>
    <h2>Qué hace el equipo de cómputo</h2>
    <p class="sub">NVIDIA DGX Spark + Eaton DX2000LAN: nodo de IA local para el Observatorio y ConvocaRadar-IA.</p>
    <div class="exec-grid">
      {''.join(f'<article class="exec-card"><h3>{c["t"]}</h3><p>{c["d"]}</p></article>' for c in COMPUTO_USO)}
    </div>
    <p class="agenda-src" style="margin-top:1rem">Detalle técnico y presupuesto en <a href="#hardware">Presupuesto MVP</a>. Proveedor: Clones y Periféricos.</p>
  </div>
</section>

<section id="flujo">
  <div class="wrap reveal">
    <p class="kicker">Operación</p>
    <h2>Diagrama de flujo del Observatorio CTi</h2>
    <p class="sub">Vista completa del ciclo. Clic en cada etapa para detalle del proceso.</p>
    <div class="flow-shell">
      <div class="flow-bar">
        <div class="flow-legend">
          <span><i class="dot" style="background:#dff7f6;border:1px solid #2C3339"></i>Entrada</span>
          <span><i class="dot" style="background:#eef7e8;border:1px solid #2C3339"></i>Captura</span>
          <span><i class="dot" style="background:#fff;border:1px solid #2C3339"></i>Proceso / análisis</span>
          <span><i class="dot" style="background:#fff4e5;border:1px solid #2C3339"></i>Salida / decisión</span>
        </div>
        <span>Clic en cada etapa</span>
      </div>
      <div class="flow-canvas">
        <svg id="diagrama" viewBox="0 0 1050 360" preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#7f93a6"/></marker>
            <marker id="arrowC" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7 Z" fill="#F39A1A"/></marker>
          </defs>
          {''.join(edges_svg)}
          {''.join(nodes_svg)}
        </svg>
      </div>
      <div class="flow-detail" id="flowDetail">
        <div class="flow-step">{f0['n']}</div>
        <div>
          <h3>{f0['titulo']} · {f0['fase']}</h3>
          <p class="proceso">{f0['proceso']}</p>
          <div class="flow-grid">
            <div class="flow-box"><h4>Actividades</h4><ul>{''.join(f'<li>{a}</li>' for a in f0['actividades'])}</ul></div>
            <div class="flow-box"><h4>Entradas / salidas</h4><p><strong>En:</strong> {f0['entradas']}<br/><strong>Out:</strong> {f0['salidas']}</p></div>
            <div class="flow-box"><h4>Responsable</h4><p>{f0['responsable']}</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section-alt" id="kpis">
  <div class="wrap reveal">
    <p class="kicker">Indicadores MVP</p>
    <h2>20 KPIs en 4 dimensiones</h2>
    <p class="sub">Marco de gestión del observatorio: operativa, analítica, ROI y sostenibilidad.</p>
    <div class="kpi-tabs" id="kpiTabs">
      <button class="kpi-tab on" data-dim="all" type="button">Todos (20)</button>
      <button class="kpi-tab" data-dim="operativa" type="button">Operativa (4)</button>
      <button class="kpi-tab" data-dim="analitica" type="button">Analítica (5)</button>
      <button class="kpi-tab" data-dim="roi" type="button">ROI (8)</button>
      <button class="kpi-tab" data-dim="sostenibilidad" type="button">Sostenibilidad (3)</button>
    </div>
    <div class="kpi-grid" id="kpiGrid">{kpi_cards}</div>
  </div>
</section>

<section id="plan" class="section-alt">
  <div class="wrap reveal">
    <p class="kicker">Plan de diseño · 2026-2</p>
    <h2>Diseño, cronograma y mínimo operativo</h2>
    <p class="sub">Hoja de ruta corta para poner en marcha el Observatorio en el semestre.</p>
    <div class="plan-exec">
      {''.join('<article><div class="n">Fase {n}</div><h3>{title}</h3><ul>{items}</ul></article>'.format(n=ph["n"], title=ph["t"], items=''.join(f'<li>· {i}</li>' for i in ph["items"])) for ph in PLAN_DISENO)}
    </div>
        <h3 style="font-family:var(--display);font-size:1.25rem;margin:1.6rem 0 .4rem">Cronograma 2026-2</h3>
    <p class="sub" style="margin-top:0">Del 1 de agosto al 18 de diciembre. Clic en cada barra para ver entregables.</p>
    <div class="gantt-wrap" id="ganttWrap">
      <div class="gantt-head">
        <h3>Cronograma operativo</h3>
        <span class="rango">1 ago 2026 → 18 dic 2026 · {GANTT_TOTAL_DIAS} días</span>
      </div>
      <div class="gantt-months">
        <div class="lab">Actividad</div>
        <div class="track">{''.join(f'<span>{m["label"]}</span>' for m in GANTT_MESES)}</div>
      </div>
      <div class="gantt-rows" id="ganttRows">
        {''.join('<div class="gantt-row{on}" data-i="{i}" role="button" tabindex="0"><div class="meta"><h4>{t}</h4><p>{resp} · día {d0}–{d1}</p></div><div class="gantt-bar-track"><div class="gantt-bar" style="left:{left}%;width:{width}%">{t}</div></div></div>'.format(on=(' on' if i==0 else ''), i=i, t=g['t'], resp=g['resp'], d0=g['start']+1, d1=g['end']+1, left=round(g['start']/GANTT_TOTAL_DIAS*100, 2), width=round((g['end']-g['start']+1)/GANTT_TOTAL_DIAS*100, 2)) for i,g in enumerate(GANTT_2026_2))}
      </div>
      <aside class="gantt-panel" id="ganttPanel">
        <div class="tag">Entregables · {GANTT_2026_2[0]['resp']}</div>
        <h4>{GANTT_2026_2[0]['t']}</h4>
        <p class="desc">{GANTT_2026_2[0]['desc']}</p>
        <ul class="ent">{''.join(f'<li><b>Entregable:</b> {e}</li>' for e in GANTT_2026_2[0]['entregables'])}</ul>
      </aside>
      <div class="gantt-legend"><span><i class="a"></i>Fases técnicas / despliegue</span><span><i class="b"></i>Piloto, integración y cierre</span></div>
    </div>
    <div class="two-col">
      <div>
        <h3 style="font-family:var(--display);font-size:1.15rem;margin:0 0 .35rem">Mínimo operativo</h3>
        <ul class="min-list">{''.join(f'<li>{x}</li>' for x in MINIMO_OP)}</ul>
      </div>
      <div>
        <h3 style="font-family:var(--display);font-size:1.15rem;margin:0 0 .35rem">Proyección 2027</h3>
        <div class="exec-grid" style="grid-template-columns:1fr;margin-top:.5rem">
          {''.join(f'<article class="exec-card"><h3>{x["t"]}</h3><p>{x["d"]}</p></article>' for x in PROYECCION_2027[:3])}
        </div>
      </div>
    </div>
  </div>
</section>

<section id="perfil">
  <div class="wrap reveal">
    <p class="kicker">Capacidad humana</p>
    <h2>Perfil de idoneidad</h2>
    <p class="sub">Roles mínimos para operar el Observatorio con calidad y continuidad.</p>
    <div class="exec-grid" style="grid-template-columns:repeat(4,1fr)">
      {''.join(f'<article class="exec-card"><h3>{x["t"]}</h3><p>{x["d"]}</p></article>' for x in PERFIL_IDONEIDAD)}
    </div>
    <p class="agenda-src">Detalle de dedicación y costos en <a href="#talento">Equipo</a>.</p>
  </div>
</section>

<section id="alianzas" class="section-alt">
  <div class="wrap reveal">
    <p class="kicker">Ecosistema</p>
    <h2>Convenios y alianzas estratégicas</h2>
    <p class="sub">Conecta CEITTO con redes de VT/IC y la ruta de reconocimiento OTRI de Minciencias.</p>
    <div class="ali-grid">
      {''.join(f'<article class="ali-card"><span class="tag">{a["tag"]}</span><h3>{a["t"]}</h3><p>{a["d"]}</p>' + (f'<a href="{a["url"]}" target="_blank" rel="noopener">Ver referencia →</a>' if a.get("url") else "") + '</article>' for a in ALIANZAS)}
    </div>
  </div>
</section>

<section class="tray-section" id="estudios">
  <div class="wrap reveal">
    <p class="kicker">Trayectoria demostrada</p>
    <h2>Estudios VT/IC realizados con evidencia</h2>
    <p class="sub">Casos reales entregados desde CEITTO: reportes interactivos, tableros, anexos técnicos y dashboards en operación.</p>
    <div class="tray-stats">
      <div class="tray-stat"><b>{len(ESTUDIOS)}</b><span>Estudios priorizados</span></div>
      <div class="tray-stat"><b>{sum(len(e['evidencias']) for e in ESTUDIOS)}</b><span>Evidencias enlazadas</span></div>
      <div class="tray-stat"><b>HTML · PDF · Web</b><span>Formatos de entrega</span></div>
      <div class="tray-stat"><b>CEITTO</b><span>Capacidad instalada</span></div>
    </div>
    <div class="tray-rail" id="trayRail">
      {''.join(f'''<button class="tray-chip{' on' if i==0 else ''}" type="button" data-i="{i}">
        <span class="n">0{i+1}</span>
        <b>{e['t']}</b>
        <span>{e['d']}</span>
      </button>''' for i,e in enumerate(ESTUDIOS))}
    </div>
    <div class="tray-stage">
      <div class="tray-preview" id="trayPreview"></div>
      <aside class="tray-side" id="traySide"></aside>
    </div>
  </div>
</section>

<section id="talento">
  <div class="wrap reveal">
    <p class="kicker">Talento humano</p>
    <h2>Equipo CEITTO para el escalamiento y soporte</h2>
    <p class="sub">El escalamiento de la plataforma de vigilancia tecnológica con el área de TI y el soporte de la propuesta estarán a cargo del CEITTO.</p>
    <div class="talento-grid">
      {''.join(f'''<article class="persona">
        <div class="avatar">{p['ini']}</div>
        <h3>{p['nombre']}</h3>
        <p class="rol">{p['rol']}</p>
        <span class="dedica">{p['dedica']}</span>
        <div class="cop">{fmt_cop(p['cop'])}<small>dedicación mensual</small></div>
        <div class="total">{fmt_cop(int(p['cop'] * MESES_TALENTO))}<small>total {PERIODO_TALENTO} ({MESES_TALENTO:g} meses)</small></div>
      </article>''' for p in TALENTO)}
    </div>
    <div class="talento-totals">
      {''.join(f'''<div class="talento-tot">
        <div class="lab">{p['nombre']}</div>
        <div class="val">{fmt_cop(int(p['cop'] * MESES_TALENTO))}</div>
        <div class="hint">{fmt_cop(p['cop'])}/mes × {MESES_TALENTO:g}</div>
      </div>''' for p in TALENTO)}
      <div class="talento-tot team">
        <div class="lab">Total equipo</div>
        <div class="val">{fmt_cop(int(sum(p['cop'] for p in TALENTO) * MESES_TALENTO))}</div>
        <div class="hint">{PERIODO_TALENTO} · {MESES_TALENTO:g} meses</div>
      </div>
    </div>
    <div class="talento-note">
      <strong>Período de dedicación: 1 de agosto al 15 de diciembre ({MESES_TALENTO:g} meses).</strong>
      Mensual del equipo: {fmt_cop(sum(p['cop'] for p in TALENTO))}. Total del período: {fmt_cop(int(sum(p['cop'] for p in TALENTO) * MESES_TALENTO))}.
    </div>
    <div class="talento-plat">
      <a href="https://github.com/julian8811/ConvocaRadar-IA" target="_blank" rel="noopener">ConvocaRadar-IA en GitHub</a>
      <a href="https://convocaradar-web.vercel.app/dashboard" target="_blank" rel="noopener">Dashboard en vivo</a>
      <span>Plataforma de vigilancia tecnológica de convocatorias nacionales e internacionales.</span>
    </div>

    <div style="margin-top:2.6rem">
      <p class="kicker">Ruta de escalamiento</p>
      <h2 style="font-size:clamp(1.4rem,2.4vw,1.8rem)">De la operación local a la infraestructura TI del CMA</h2>
      <p class="sub">Cinco fases para llevar ConvocaRadar-IA al ecosistema tecnológico institucional, con pruebas y soporte del equipo CEITTO. Clic en cada fase.</p>
      <div class="esc-stage">
        <div class="esc-steps" id="escSteps">
          {''.join(f'''<button class="esc-step{' on' if i==0 else ''}" type="button" data-i="{i}">
            <span class="num">{e['n']}</span>
            <div><h3>{e['t']}</h3><p>{e['meta']}</p></div>
          </button>''' for i,e in enumerate(ESCALADO))}
        </div>
        <aside class="esc-panel" id="escPanel">
          <p class="fase-tag">Fase {ESCALADO[0]['n']} · {ESCALADO[0]['meta']}</p>
          <h3>{ESCALADO[0]['t']}</h3>
          <ul class="esc-acts">
            {''.join(f'<li style="animation-delay:{i*0.05}s">{a}</li>' for i,a in enumerate(ESCALADO[0]['acts']))}
          </ul>
          <div class="esc-out"><b>Entregable:</b> {ESCALADO[0]['out']}</div>
        </aside>
      </div>
    </div>
  </div>
</section>

<section id="hardware">
  <div class="wrap reveal">
    <p class="kicker">Infraestructura MVP</p>
    <h2>Configuración recomendada y presupuesto MVP</h2>
    <p class="sub">{HW['ws']['titulo']} + {HW['ups']['titulo']} · inversión total del MVP.</p>
    <div class="hw-grid">
      <article class="hw">
        <span class="tag">Clones y Periféricos</span>
        <img class="hw-photo" src="{HW['ws']['img']}" alt="NVIDIA DGX Spark" loading="lazy">
        <h3>{HW['ws']['titulo']}</h3>
        <ul>{''.join(f'<li>{s}</li>' for s in HW['ws']['specs'])}</ul>
        <div class="price">{fmt_cop(HW['ws']['cop'])}</div>
        <p class="hw-usd">Precio lista {fmt_cop(HW['ws']['list_cop'])} · oferta vigente en proveedor Colombia</p>
        <a class="hw-link" href="{HW['ws']['url']}" target="_blank" rel="noopener">Ver en Clones y Periféricos →</a>
      </article>
      <article class="hw ups">
        <span class="tag">UPS</span>
        <img class="hw-photo" src="{HW['ups']['img']}" alt="Eaton DX2000LAN" loading="lazy">
        <h3>{HW['ups']['titulo']}</h3>
        <ul>{''.join(f'<li>{s}</li>' for s in HW['ups']['specs'])}</ul>
        <div class="price">{fmt_cop(HW['ups']['cop'])}</div>
      </article>
    </div>
    <div class="budget">
      <p style="font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;opacity:.75">Presupuesto total del proyecto MVP</p>
      <div class="total">{fmt_cop(PRESUPUESTO['total'])}</div>
      {''.join(f'''<div class="budget-row">
        <div><div>{l['nombre']}</div><div class="bar"><div class="fill" style="width:{l['pct']}%"></div></div></div>
        <strong>{fmt_cop(l['valor'])}</strong>
        <span style="opacity:.7">{l['pct']}%</span>
      </div>''' for l in PRESUPUESTO['lineas'])}
    </div>
  </div>
</section>

<section id="piloto" class="section-alt">
  <div class="wrap reveal">
    <p class="kicker">Piloto</p>
    <h2>Primer caso de uso</h2>
    <div class="piloto" style="margin-top:1.2rem">
      <div class="piloto-visual"></div>
      <div class="piloto-copy">
        <h3>Indicadores de bienestar → permanencia, graduación y éxito académico</h3>
        <p>Caso demostrativo para conectar evidencia social con trayectoria estudiantil.</p>
      </div>
    </div>
  </div>
</section>


<section id="sigue" class="section-alt">
  <div class="wrap reveal">
    <p class="kicker">Hoja de ruta</p>
    <h2>Qué sigue: plataformas a diseñar</h2>
    <p class="sub">Prioridades de producto digital y su foco institucional.</p>
    <div class="qs-grid">
      {''.join(f'<article class="qs-card"><div class="st">{q["estado"]}</div><h3>{q["plat"]}</h3><p>{q["foco"]}</p></article>' for q in QUE_SIGUE)}
    </div>
    <div class="exec-grid" style="margin-top:1.2rem">
      {''.join(f'<article class="exec-card"><h3>{x["t"]}</h3><p>{x["d"]}</p></article>' for x in PROYECCION_2027[3:])}
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <blockquote>
      La inteligencia artificial <strong>no reemplaza</strong> a las personas: las <strong>complementa</strong>.
      <cite>En el Observatorio CTi, la IA refuerza el criterio de los equipos humanos y ayuda a decidir con evidencia, de forma ética y responsable.</cite>
    </blockquote>
  </div>
</section>

<script>
const PROBLEMAS = {json.dumps(PROBLEMAS, ensure_ascii=False)};
const VENTAJAS_PDI = {json.dumps(VENTAJAS_PDI, ensure_ascii=False)};
const AGENDA_INST = {json.dumps(AGENDA_INST, ensure_ascii=False)};
const FLOW={json.dumps({n["id"]:n for n in FLOW},ensure_ascii=False)};
const OBJ={json.dumps(OBJ,ensure_ascii=False)};
const PLAN_DATA = {json.dumps(PLAN, ensure_ascii=False)};
const PILARES = {json.dumps(PILARES, ensure_ascii=False)};
const VENTAJAS = {json.dumps(VENTAJAS, ensure_ascii=False)};
const SERVICIOS = {json.dumps(SERVICIOS, ensure_ascii=False)};
const ESTUDIOS = {json.dumps(ESTUDIOS, ensure_ascii=False)};
const GANTT_2026_2 = {json.dumps(GANTT_2026_2, ensure_ascii=False)};

document.getElementById('menu').onclick=()=>document.getElementById('links').classList.toggle('open');
document.querySelectorAll('#links a').forEach(a=>{{
  a.addEventListener('click',()=>document.getElementById('links').classList.remove('open'));
}});
window.addEventListener('resize',()=>{{
  if(innerWidth>900) document.getElementById('links').classList.remove('open');
}});

function trayPreviewHtml(e, ev){{
  if(!ev){{
    return `<div class="tray-fallback"><p class="badge">${{e.tag}}</p><h3>${{e.t}}</h3><p>${{e.blurb}}</p></div>`;
  }}
  if(ev.tipo==='html'){{
    return `<iframe title="${{ev.label}}" src="${{ev.src}}" loading="lazy"></iframe>`;
  }}
  if(ev.tipo==='pdf'){{
    return `<iframe title="${{ev.label}}" src="${{ev.src}}#view=FitH" loading="lazy"></iframe>
      <div style="position:absolute;right:12px;bottom:12px"><a href="${{ev.src}}" target="_blank" rel="noopener">Abrir PDF</a></div>`;
  }}
  // URLs externas no se embeben (bloquean iframe / sitio caído): tarjeta de acceso directo
  return `<div class="tray-fallback">
      <p class="badge">${{e.tag}} · acceso directo</p>
      <h3>${{ev.label}}</h3>
      <p>${{e.blurb}}</p>
      <p style="font-size:.85rem;opacity:.75;margin-bottom:1rem">Este recurso no se puede embeber aquí. Ábrelo en una pestaña nueva.</p>
      <a href="${{ev.src}}" target="_blank" rel="noopener">Abrir ${{ev.label}}</a>
    </div>`;
}}

function renderTray(i, evIdx=0){{
  const e = ESTUDIOS[i];
  const ev = e.evidencias[evIdx] || null;
  document.getElementById('trayPreview').innerHTML = trayPreviewHtml(e, ev);
  const list = e.evidencias.length
    ? e.evidencias.map((x,n)=>`<button type="button" class="${{n===evIdx?'on':''}}" data-e="${{n}}"><span>${{x.label}}</span><span class="kind">${{x.tipo}}</span></button>`).join('')
    : `<p style="color:rgba(255,255,255,.65);font-size:.9rem;margin:0">Evidencia documental de cierres de proyectos VT/IC.</p>`;
  document.getElementById('traySide').innerHTML = `
    <p class="tag">${{e.tag}}</p>
    <h3>${{e.t}}</h3>
    <div class="metric-row"><b>${{e.metric}}</b><span>${{e.metric_l}}</span></div>
    <p>${{e.blurb}}</p>
    <div class="tray-ev">${{list}}</div>
    ${{ev ? `<a class="cta-ev" href="${{ev.src}}" target="_blank" rel="noopener">Abrir evidencia completa</a>` : ''}}`;
  document.querySelectorAll('#traySide .tray-ev button').forEach(btn=>{{
    btn.onclick=()=>renderTray(i, +btn.dataset.e);
  }});
}}
document.querySelectorAll('#trayRail .tray-chip').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#trayRail .tray-chip').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    renderTray(+btn.dataset.i, 0);
  }};
}});
if(document.getElementById('trayRail')) renderTray(0,0);

const ESCALADO = {json.dumps(ESCALADO, ensure_ascii=False)};
function renderEsc(i){{
  const e = ESCALADO[i];
  const panel = document.getElementById('escPanel');
  if(!panel) return;
  panel.innerHTML = `
    <p class="fase-tag">Fase ${{e.n}} · ${{e.meta}}</p>
    <h3>${{e.t}}</h3>
    <ul class="esc-acts">${{e.acts.map((a,n)=>`<li style="animation-delay:${{n*0.05}}s">${{a}}</li>`).join('')}}</ul>
    <div class="esc-out"><b>Entregable:</b> ${{e.out}}</div>`;
}}
document.querySelectorAll('#escSteps .esc-step').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#escSteps .esc-step').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    renderEsc(+btn.dataset.i);
  }};
}});

function renderProb(i){{
  const p = PROBLEMAS[i];
  const panel = document.getElementById('probPanel');
  if(!panel) return;
  panel.className = 'prob-panel' + (p.tipo==='solucion' ? ' solucion' : '');
  panel.innerHTML = `<p class="tag">Contexto Colmayor</p><h3>${{p.titulo}}</h3><p>${{p.desc}}</p><div class="efecto"><strong>Implicación:</strong> ${{p.efecto}}</div>`;
}}
document.querySelectorAll('#probList .prob-btn').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#probList .prob-btn').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    renderProb(+btn.dataset.i);
  }};
}});

function renderPdi(i){{
  const v = VENTAJAS_PDI[i];
  const panel = document.getElementById('pdiPanel');
  if(!panel) return;
  panel.innerHTML = `
    <h3>${{v.nombre}}</h3>
    <p class="foco">${{v.foco}}</p>
    <ul class="pdi-inds">${{v.indicadores.map((ind,n)=>`<li style="animation-delay:${{n*0.05}}s"><b>${{ind.t}}</b><span>${{ind.m}}</span></li>`).join('')}}</ul>`;
}}
document.querySelectorAll('#pdiTabs .pdi-tab').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#pdiTabs .pdi-tab').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    renderPdi(+btn.dataset.i);
  }};
}});


function renderAgenda(i){{
  const a = AGENDA_INST[i];
  const panel = document.getElementById('agendaPanel');
  if(!panel || !a) return;
  const estudios = (a.estudios||[]).map(e=>`<li class="yr"><span class="yr-tag">${{e.a}}</span>${{e.t}}</li>`).join('');
  const programas = (a.programas||[]).map(p=>`<li>${{p}}</li>`).join('');
  const inds = (a.indicadores||[]).map(k=>`
    <div class="k">
      <div class="cod">${{k.cod}}</div>
      <div class="kt">${{k.t}}</div>
      <div class="log">${{k.logro}}</div>
      <div class="meta">Meta ${{k.meta}} · ${{k.u}}</div>
    </div>`).join('');
  const dominios = a.dominios
    ? `<div class="dom-row">${{a.dominios.map(d=>`<div class="dom-card"><b>${{d.t}}</b><span>${{d.d}}</span></div>`).join('')}}</div>`
    : '';
  const pmo = a.pmo
    ? `<div class="agenda-block"><h4>PMO activa <span>acompañamiento</span></h4><ul class="agenda-list">${{a.pmo.map(x=>`<li>${{x}}</li>`).join('')}}</ul></div>`
    : '';
  const riesgos = a.riesgos
    ? `<div class="agenda-block"><h4>Riesgos priorizados <span>corrupción · gestión</span></h4><div class="risk-grid">${{a.riesgos.map(r=>`<div class="risk-item"><span class="rz ${{r.z}}">${{r.z}}</span><b>${{r.t}}</b><span>Aporte del Observatorio: ${{r.a}}</span></div>`).join('')}}</div></div>`
    : '';
  panel.innerHTML = `
    <p class="ln" style="font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--teal)">${{a.linea}}</p>
    <h3 style="font-family:var(--display);font-size:1.35rem;margin:.2rem 0">${{a.nombre}}</h3>
    <p class="foco">${{a.foco}}</p>
    ${{dominios}}
    <div class="agenda-grid">
      <div>
        <div class="agenda-block"><h4>Programas / ejes <span>PDI</span></h4><ul class="agenda-list">${{programas}}</ul></div>
        <div class="agenda-block"><h4>Agenda de estudios <span>institucional</span></h4><ul class="agenda-list">${{estudios}}</ul></div>
        ${{pmo}}
      </div>
      <div>
        <div class="agenda-block"><h4>Indicadores IES Distrito <span>jun-2026</span></h4><div class="kpi-mini">${{inds}}</div></div>
        ${{riesgos}}
      </div>
    </div>
    <div class="agenda-aporte"><b>Aporte del Observatorio:</b> ${{a.aporte}}</div>`;
}}
document.querySelectorAll('#agendaTabs .agenda-tab').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#agendaTabs .agenda-tab').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    renderAgenda(+btn.dataset.i);
  }};
}});
if(document.getElementById('agendaTabs')) renderAgenda(0);



function renderFlow(id){{
  const d=FLOW[id];
  document.getElementById('flowDetail').innerHTML=`
    <div class="flow-step">${{d.n}}</div>
    <div>
      <h3>${{d.titulo}} · ${{d.fase}}</h3>
      <p class="proceso">${{d.proceso}}</p>
      <div class="flow-grid">
        <div class="flow-box"><h4>Actividades</h4><ul>${{d.actividades.map(a=>`<li>${{a}}</li>`).join('')}}</ul></div>
        <div class="flow-box"><h4>Entradas / salidas</h4><p><strong>En:</strong> ${{d.entradas}}<br/><strong>Out:</strong> ${{d.salidas}}</p></div>
        <div class="flow-box"><h4>Responsable</h4><p>${{d.responsable}}</p></div>
      </div>
    </div>`;
}}
document.querySelectorAll('.nodo').forEach(n=>{{
  n.onclick=()=>{{document.querySelectorAll('.nodo').forEach(x=>x.classList.remove('activo'));n.classList.add('activo');renderFlow(n.dataset.id);}};
}});
document.querySelector('.nodo')?.classList.add('activo');

document.querySelectorAll('.obj-card').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('.obj-card').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    const o=OBJ[+btn.dataset.i];
    document.getElementById('objPanel').innerHTML=`<strong>${{o.t}}</strong><p>${{o.d}}</p>`;
  }};
}});

document.querySelectorAll('#kpiTabs .kpi-tab').forEach(tab=>{{
  tab.onclick=()=>{{
    document.querySelectorAll('#kpiTabs .kpi-tab').forEach(t=>t.classList.remove('on'));
    tab.classList.add('on');
    const dim=tab.dataset.dim;
    document.querySelectorAll('#kpiGrid .kpi').forEach(k=>{{
      k.style.display=(dim==='all'||k.dataset.dim===dim)?'':'none';
    }});
  }};
}});

/* Valor pillars */
document.querySelectorAll('#pillarStack .pillar-btn').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#pillarStack .pillar-btn').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    const p=PILARES[+btn.dataset.i];
    document.getElementById('valorPanel').innerHTML=`<p class="eyebrow">Pilar activo</p><h3>${{p.t}}</h3><p>${{p.d}}</p>`;
  }};
}});

/* Ventajas chips */
document.querySelectorAll('#advRail .adv-chip').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#advRail .adv-chip').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    const v=VENTAJAS[+btn.dataset.i];
    const spot=document.getElementById('advSpot');
    spot.classList.add('show');
    spot.innerHTML=`<strong>${{v.t}}</strong>: ${{v.d}}`;
  }};
}});

/* Roadmap / Plan */
function renderRoad(i){{
  const p=PLAN_DATA[i];
  document.querySelectorAll('#roadTrack .road-step').forEach((b,idx)=>b.classList.toggle('on',idx===i));
  document.getElementById('roadPanel').innerHTML=`
    <div class="road-badge">${{p.fase}}</div>
    <div>
      <h3>${{p.t}}</h3>
      <ul class="road-items">${{p.items.map((it,j)=>`<li style="animation-delay:${{j*0.05}}s">${{it}}</li>`).join('')}}</ul>
    </div>`;
}}
document.querySelectorAll('#roadTrack .road-step').forEach(btn=>{{
  btn.onclick=()=>renderRoad(+btn.dataset.i);
}});

/* Canales mosaic */
document.querySelectorAll('#canalMosaic .canal-tile').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#canalMosaic .canal-tile').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    document.getElementById('canalTitle').textContent=btn.dataset.c;
    document.getElementById('canalDesc').textContent='Medio de divulgación para fortalecer capacidades institucionales en CTi.';
  }};
}});

/* Servicios mosaic */
document.querySelectorAll('#svcMosaic .svc-tile').forEach(btn=>{{
  btn.onclick=()=>{{
    document.querySelectorAll('#svcMosaic .svc-tile').forEach(b=>b.classList.remove('on'));
    btn.classList.add('on');
    const s=SERVICIOS[+btn.dataset.i];
    const d=document.getElementById('svcDetail');
    d.classList.add('show');
    d.innerHTML=`<strong>${{s.t}}</strong>: ${{s.d}}`;
  }};
}});

const io=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting)e.target.classList.add('on');}}),{{threshold:.1}});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
const secs=[...document.querySelectorAll('section[id],header[id]')];
const links=[...document.querySelectorAll('.nav-links a')];
window.addEventListener('scroll',()=>{{
  const max=document.documentElement.scrollHeight-innerHeight;
  document.getElementById('bar').style.width=`${{(scrollY/max)*100}}%`;
  let cur=secs[0]?.id;
  secs.forEach(s=>{{if(scrollY>=s.offsetTop-110)cur=s.id;}});
  links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')===`#${{cur}}`));
}});

function renderGantt(i){{
  const g = GANTT_2026_2[i];
  const panel = document.getElementById('ganttPanel');
  if(!panel || !g) return;
  panel.innerHTML = `
    <div class="tag">Entregables · ${{g.resp}}</div>
    <h4>${{g.t}}</h4>
    <p class="desc">${{g.desc}}</p>
    <ul class="ent">${{g.entregables.map(e=>`<li><b>Entregable:</b> ${{e}}</li>`).join('')}}</ul>`;
}}
document.querySelectorAll('#ganttRows .gantt-row').forEach(row=>{{
  const activate=()=>{{
    document.querySelectorAll('#ganttRows .gantt-row').forEach(r=>r.classList.remove('on'));
    row.classList.add('on');
    renderGantt(+row.dataset.i);
  }};
  row.addEventListener('click', activate);
  row.addEventListener('keydown', e=>{{ if(e.key==='Enter'||e.key===' '){{ e.preventDefault(); activate(); }} }});
}});
if(document.getElementById('ganttRows')) renderGantt(0);

</script>
</body>
</html>
'''

(OUT / "ejecutiva.html").write_text(html, encoding="utf-8")
assert "Seleccione un objetivo" not in html
assert "no reemplaza" in html
assert "DGX Spark" in html
assert "Eaton DX2000LAN" in html
assert "dgx-spark.jpg" in html
assert "Implementación de IA" in html
assert "Red y conectividad" not in html
assert "Dell Precision" not in html
assert "Workstation" not in html
assert "NVIDIA DGX Spark" in html
assert "Academia transformadora" in html
assert 'id="estudios"' in html
assert 'id="talento"' in html
assert "Julián Esteban Pineda Montoya" in html
assert "ConvocaRadar-IA" in html
assert html.count("esc-step") >= 5
assert "evidencias/camara" in html
assert "mgdalena-medio.vercel.app" in html
assert "convocaradar-web.vercel.app" in html
assert "\u2014" not in html
assert OBJETIVO_CLARO.split()[0] in html
assert 'id="beneficios"' in html
assert 'id="sigue"' in html
assert 'id="alianzas"' in html
assert 'José Mario López Gómez' in html
assert '10 horas' in html
assert 'OTRI' in html
assert 'Innruta' in html
assert 'id="computo"' in html
assert 'id="flujo"' in html
assert 'id="kpis"' in html
assert 'id="plan"' in html
assert 'id="perfil"' in html
assert 'id="hardware"' in html
assert '29.420.000' in html
assert 'Mínimo operativo' in html
assert 'Cronograma 2026-2' in html
assert "ganttRows" in html
assert "Entregable" in html
print("OK", OUT / "ejecutiva.html", "total", PRESUPUESTO["total"])

