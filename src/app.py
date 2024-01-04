from flask import Flask, jsonify
from data_csv import descargar_csv, lee_datos
from carga_bd import insertar_datos
from api_pos_code import consult_and_store
import gdown
from respuestas import resultado, resultado_data

import json

app= Flask(__name__)

@app.route('/', methods=['GET'] )
def ping():
    return jsonify({
        'Response': 'Hola',
        'Fin': 'La Logre'
    })

@app.route('/csv', methods=['GET'] )
def micro1():
    datos_csv= descargar_csv()
    pt1 = lee_datos()
    pt2= insertar_datos(pt1)
    return jsonify({'cantidad': len(pt1) })

@app.route('/receive-data', methods=['GET'])
def micro2():
    datos_csv= consult_and_store()
    datos_totales = json.loads(resultado_data())
    datos_csv_json= jsonify({'ultimo_id': datos_csv})
    rta = json.loads(resultado())

    return jsonify({'ULTIMO ID PROCESADO': datos_csv_json.json , 'DATOS ERROREOS': rta, 'RESULTADOS CONSULTA': datos_totales })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000,debug=True)

