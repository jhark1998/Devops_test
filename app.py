import os
import flask
import psycopg2

app = flask.Flask(_name_)

@app.route('/live')
def live():
    try:
        db_url = os.environ.get('DATABASE_URL')
        conn = psycopg2.connect(db_url)
        conn.close()
        return 'Well done'
    except Exception:
        return 'Maintenance'

if _name_ == '_main_':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
