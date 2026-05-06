import os

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

PROSTHESIS_TYPES = ["Todas", "Fijas", "Removibles", "Implantes CAD/CAM"]
MATERIALS = ["Todos", "Zirconia", "Cerámica", "Acrílico"]

CATALOG = [
    {
        "name": "Corona monolítica de zirconia",
        "type": "Fijas",
        "material": "Zirconia",
        "price": "$120 - $180",
        "summary": "Alta resistencia y acabado natural para rehabilitación posterior.",
        "technical": "Zirconia monolítica, ajuste digital CAD/CAM, espesor optimizado de 0.6 mm.",
        "specs": ["Morfología anatómica", "Cemento resinable", "Alta translucidez"],
        "angles": ["Vista frontal", "Vista lateral", "Oclusal", "Vista 360"],
    },
    {
        "name": "Puente dental cerámico",
        "type": "Fijas",
        "material": "Cerámica",
        "price": "$260 - $420",
        "summary": "Solución estética para restauraciones de múltiples piezas.",
        "technical": "Cerámica estratificada, preparación guiada y prueba de color por capas.",
        "specs": ["Alta estética", "Acabado biomimético", "Ajuste por escaneo"],
        "angles": ["Vista frontal", "Perfil", "Detalle marginal", "Vista 360"],
    },
    {
        "name": "Prótesis parcial flexible",
        "type": "Removibles",
        "material": "Acrílico",
        "price": "$150 - $230",
        "summary": "Ligereza, comodidad y estética para rehabilitación removible.",
        "technical": "Base flexible con retenedores discretos y diseño funcional adaptado al arco.",
        "specs": ["Ligera", "Confortable", "Fácil mantenimiento"],
        "angles": ["Vista frontal", "Extensión distal", "Detalle de retenedores", "Vista 360"],
    },
    {
        "name": "Guía quirúrgica CAD/CAM",
        "type": "Implantes CAD/CAM",
        "material": "Zirconia",
        "price": "$180 - $300",
        "summary": "Diseñada para posicionamiento preciso en implantes.",
        "technical": "Planificación digital, archivo STL, verificación de tolerancias y perforaciones guiadas.",
        "specs": ["Flujo digital", "Alta precisión", "Trazabilidad clínica"],
        "angles": ["Vista superior", "Interior", "Orificios guía", "Vista 360"],
    },
    {
        "name": "Carilla estética ultrafina",
        "type": "Fijas",
        "material": "Cerámica",
        "price": "$140 - $210",
        "summary": "Corrección estética con mínima invasión.",
        "technical": "Cerámica de alta estética con preparación conservadora y control de color.",
        "specs": ["Ultrafina", "Natural", "Conservadora"],
        "angles": ["Vista frontal", "Borde incisal", "Perfil", "Vista 360"],
    },
    {
        "name": "Placa oclusal de acrílico",
        "type": "Removibles",
        "material": "Acrílico",
        "price": "$60 - $95",
        "summary": "Control de bruxismo con ajuste cómodo y estable.",
        "technical": "Acrílico termocurado, ajuste oclusal y bordeado personalizado.",
        "specs": ["Bruxismo", "Confort nocturno", "Fácil ajuste"],
        "angles": ["Vista frontal", "Superficie oclusal", "Perfil", "Vista 360"],
    },
]

SERVICES = [
    {"title": "Citas", "text": "Agenda una valoración inicial o seguimiento clínico en línea."},
    {"title": "Presupuestos", "text": "Solicita una cotización rápida según el caso, material y complejidad."},
    {"title": "Contactos", "text": "Canales directos para consulta, seguimiento y atención personalizada."},
]

ABOUT_POINTS = [
    "Flujo digital con control de calidad en cada etapa.",
    "Comunicación directa con clínicas y doctores.",
    "Tiempos de entrega claros y seguimiento por caso.",
]

FAQS = [
    {
        "question": "¿Trabajan con archivos digitales de clínicas?",
        "answer": "Sí. Recibimos STL, fotografías clínicas y referencias para integrar el caso a nuestro flujo CAD/CAM.",
    },
    {"question": "¿Qué materiales manejan?", "answer": "Principalmente zirconia, cerámica y acrílico, según el requerimiento clínico y estético."},
    {"question": "¿Puedo solicitar cotización en línea?", "answer": "Sí. El formulario de cotización permite enviar el caso y recibir respuesta de seguimiento."},
    {"question": "¿La galería clínica requiere autorización?", "answer": "Sí. Los casos de antes y después se publican solo con autorización del paciente."},
]

CLINICAL_GALLERY = [
    {"title": "Antes y después", "label": "Autorizado", "description": "Registro comparativo de rehabilitación estética y funcional."},
    {"title": "Caso protésico", "label": "Documento clínico", "description": "Secuencia de laboratorio, prueba clínica y entrega final."},
    {"title": "Escaneo intraoral", "label": "Recursos", "description": "Material de apoyo para planificación y comunicación con clínicas."},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        catalog=CATALOG,
        services=SERVICES,
        about_points=ABOUT_POINTS,
        faqs=FAQS,
        gallery=CLINICAL_GALLERY,
        prosthesis_types=PROSTHESIS_TYPES,
        materials=MATERIALS,
    )


@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or {}
    print(f"Mensaje recibido de {data.get('email', 'sin correo')}: {data.get('message', '')}")
    return jsonify({"status": "success", "message": "Contacto recibido. Te responderemos pronto."})


@app.route("/quote", methods=["POST"])
def quote():
    data = request.get_json(silent=True) or {}
    print(f"Cotización solicitada por {data.get('name', 'sin nombre')} - {data.get('service', '')}")
    return jsonify({"status": "success", "message": "Cotización enviada correctamente."})


@app.route("/appointment", methods=["POST"])
def appointment():
    data = request.get_json(silent=True) or {}
    print(f"Cita solicitada por {data.get('name', 'sin nombre')} para {data.get('date', '')}")
    return jsonify({"status": "success", "message": "Cita solicitada correctamente."})


if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "5000"))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"
    app.run(host=host, port=port, debug=debug, threaded=True)
