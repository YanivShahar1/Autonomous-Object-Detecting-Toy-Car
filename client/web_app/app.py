from flask import Flask, render_template, jsonify, send_from_directory
import os

# Load routes
from routes.car_routes import car_control_routes
from routes.image_routes import image_routes
app = Flask(__name__, static_folder='static' )

# Register the blueprint for image routes
app.register_blueprint(image_routes)
app.register_blueprint(car_control_routes)

@app.route('/static/js/<path:filename>')
def serve_js(filename):
    response = app.send_static_file(f'js/{filename}')
    response.headers['Content-Type'] = 'application/javascript'
    return response

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)



@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)



