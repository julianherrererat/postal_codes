from flask import Flask, jsonify
from data_csv import descargar_csv, lee_datos
from carga_bd import insertar_datos
import gdown

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



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000,debug=True)