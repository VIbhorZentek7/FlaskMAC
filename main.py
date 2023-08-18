from flask import Flask, request, jsonify
import subprocess
app = Flask(__name__)

@app.route('/run_command', methods=['POST'])
def run_command():
    if request.method == 'POST': 
        command = "ipconfig /all"
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            print(type(result))
            return jsonify({'result': result})
        except subprocess.CalledProcessError as e:
            return jsonify({'error': str(e)})
        

if __name__ == '__main__':
    app.run(debug=True, port=3001)
