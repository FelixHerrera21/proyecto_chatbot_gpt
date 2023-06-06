from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

error = False

try:
    openai.api_key = "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"
    chat_log = []
    contexto = 'Te pasaré información y te haré preguntas sobre esta: \
                "Kodit ofrece servicios sobre desarrollo web, móvil, inteligencia artificial, \
                consultoría en TI, diseño de ui/ux, ciberseguridad, (+52)5560665098 es \
                el número de la empresa, horario de 9 am a 6pm,  se ubican en: Miguel Laurent 15 Bis, Depto 404 \
                colonia del valle, Deleg Benito Juarez, CDMX, su correo es administracion@kodit.com.mx". cada que respondas quiero que \
                hables como si fueras parte de la empresa y tus respuestas sean cortas'
    chat_log.append({"role":"user", "content": contexto})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= chat_log
    )
    gpt_response = response['choices'][0]['message']['content']
    respuesta = gpt_response.strip("\n").strip()
    chat_log.append({"role":"assistant", "content": respuesta})
except:
    error = True

@app.route('/api/transform', methods=['POST'])
def transform_text():
    if error:
        response = {'data': "", 'message': "error con la API ChatGPT", 'error': error}
        return jsonify(response)
    else:
        try:
            #print(request.get_json())
            data = request.get_json()  # Obtener los datos JSON enviados en la solicitud
            input_text = data['text']  # Obtener el texto de entrada del campo 'text'

            chat_log.append({"role":"user", "content": input_text})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages= chat_log
            )
            gpt_response = response['choices'][0]['message']['content']
            respuesta = gpt_response.strip("\n").strip()
            chat_log.append({"role":"assistant", "content": respuesta})
            #print("chatbot: "+ respuesta)
            response = {'data': respuesta, 'message': "OK", 'error': error}

            return jsonify(response)
        except:
            response = {'data': "", 'message': "error al consultar API", 'error': True}
            return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    #app.run(port=5000)