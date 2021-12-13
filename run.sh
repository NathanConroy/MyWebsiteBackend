
export PORT=8000
APIMM_HOST=${APIMM_HOST:-"127.0.0.1"}

FLASK_APP=api.endpoints flask run --host=$APIMM_HOST --port=$PORT

