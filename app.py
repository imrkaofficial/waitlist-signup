from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        if email:
            with open('waitlist.txt', 'a') as f:
                f.write(email + '\n')
            return jsonify(message="Thank you for joining the waitlist!", success=True)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7001))
    app.run(debug=True, host='0.0.0.0', port=port)
