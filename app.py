from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_temperature():
    data = request.get_json()
    temp = float(data['temperature'])
    unit = data['unit']

    if unit == 'celsius':
        celsius = temp
        fahrenheit = (temp * 9/5) + 32
        kelvin = temp + 273.15
    elif unit == 'fahrenheit':
        celsius = (temp - 32) * 5/9
        fahrenheit = temp
        kelvin = celsius + 273.15
    elif unit == 'kelvin':
        celsius = temp - 273.15
        fahrenheit = (celsius * 9/5) + 32
        kelvin = temp

    # Returning results as a JSON response
    return jsonify({
        'celsius': round(celsius, 2),
        'fahrenheit': round(fahrenheit, 2),
        'kelvin': round(kelvin, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
