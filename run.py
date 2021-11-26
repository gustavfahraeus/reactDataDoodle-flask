from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import datetime
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

MONGO_STRING = os.getenv("MONGO_STRING")
cluster = MongoClient(MONGO_STRING, connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1)
db = cluster["reactDataDoodle"]
collection = db["reactDataDoodle"]


@app.route('/hello', methods=['POST', 'DELETE'])
@cross_origin()
def something():
    message = request.get_json(force=True)
    try:
        userEntries = collection({'__id': message['__id']})
        if userEntries:
            latestUploadDate = ''
            for entry in userEntries:
                if latestUploadDate == '':
                    latestUploadDate = user['uploadDate']
                else:
                    if user['uploadDate'] > latestUploadDate:
                        latestUploadDate = user['uploadDate']

            date = latestUploadDate[:4]
            month = latestUploadDate[5:7]
            day = latestUploadDate[8:10]
            d = datetime.date(int(date), int(month), int(day))
            if datetime.date.today() > d + datetime.timedelta(days=1):
                collection.insert_one(message)
        else:
            return

    except:
        pass
    return jsonify("Something probably didn't go right.")



if __name__ == "__main__":
    app.run()
