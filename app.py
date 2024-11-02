from flask import Flask, render_template
from apiHandler.router import tender_bp

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(tender_bp, url_prefix='/api')


# Define a route for the root URL
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)


