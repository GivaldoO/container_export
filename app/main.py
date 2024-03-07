from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/create_file', methods=['POST'])
def create_file():
    data = request.get_json()

    filename = data.get('filename')
    filecontent = data.get('filecontent')

    if not filename or not filecontent:
        return jsonify({'error': 'Both filename and filecontent are required'}), 400

    file_path = os.path.join('files', filename)

    if os.path.exists(file_path):
        return jsonify({'error': f'File {filename} already exists'}), 400

    with open(file_path, 'w') as file:
        file.write(filecontent)

    return jsonify({'success': f'File {filename} created successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




    
# from flask import Flask, render_template, request, jsonify, send_file
# import os

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/create_file', methods=['POST'])
# def create_file():
#     data = request.get_json()

#     filename = data.get('filename')
#     filecontent = data.get('filecontent')

#     if not filename or not filecontent:
#         return jsonify({'error': 'Both filename and filecontent are required'}), 400

#     file_path = os.path.join('files', filename)

#     if os.path.exists(file_path):
#         return jsonify({'error': f'File {filename} already exists'}), 400

#     with open(file_path, 'w') as file:
#         file.write(filecontent)

#     return send_file(file_path, as_attachment=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


