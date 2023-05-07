
from dbhelpers import conn_exe_close
from apihelpers import verify_endpoints_info, add_for_patch
from flask import Flask, request, make_response
import dbcreds

from endpoints import email

app = Flask(__name__)


@app.post('/api/email-post')
def email_post():
    return email.post()






if(dbcreds.production_mode == True):
    import bjoern #type: ignore
    bjoern.run(app,'0.0.0.0',5001)
    print('Running in PRODUCTION MODE')
else:
    from flask_cors import CORS
    CORS(app)
    print('Running in TESTING MODE')
    app.run(debug=True)


