import firebase_admin
from firebase_admin import credentials, messaging, auth, firestore

from backendApi.settings import BASE_DIR
from datetime import datetime

cred = credentials.Certificate(BASE_DIR /"serviceAccountKey.json")
#cred = credentials.Certificate('C:/Users/Camilo/proyectos/Quiosco/backendApi/serviceAccountKey.json')
firebaseApp = firebase_admin.initialize_app(cred)

def sendPush(titulo, mensaje, token, dataObject = None):
    try:
        mensajeAux = messaging.MulticastMessage(
            notification = messaging.Notification(
                title = titulo,
                body = mensaje
            ),
            data =  dataObject,
            tokens = token,
        )

        response = messaging.send_each_for_multicast(mensajeAux)
        print(datetime.now())
        print("okkkkkkkkkkk*************************************************", response)
    except BaseException as err:
        print ("errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr" + str(err))


