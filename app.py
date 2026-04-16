from flask import Flask, request

app = Flask(__name__)

@app.route('/data-example', methods=['GET', 'POST'])
def handle_request():
    name = request.args.get('name', 'Guest')

    if request.method == 'POST':
        form_data = request.form.get('username')
        return f"Form submitted for: {form_data}"

    return f"Hello, {name}! Send a POST request with JSON or Form data."

if __name__ == '__main__':
    app.run(debug=True)
