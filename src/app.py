from flask import Flask, jsonify
import redis

app= Flask(__name__)
cache= redis.Redis(host='redis',port=6379)

@app.route('/', methods=['GET'] )
def ping():
    return jsonify({
        'Response': 'Hola',
        'Fin': 'La Logre'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)