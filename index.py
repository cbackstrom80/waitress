from flask import Flask
import uwsgidecorators
from splunk_otel.tracing import start_tracing
from opentelemetry.instrumentation.flask import FlaskInstrumentor

app = Flask(__name__)

@uwsgidecorators.postfork
def setup_tracing():
    start_tracing()
    # instrument our flask app instance eplicitly
    FlaskInstrumentor().instrument_app(app)



@app.route("/")
def hello():
    return "Hello, World!"