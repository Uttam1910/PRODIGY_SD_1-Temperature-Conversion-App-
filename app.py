from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Temperature conversion logic
def convert_temperature(temp_value, original_unit):
    celsius, fahrenheit, kelvin = None, None, None
    
    if original_unit == 'celsius':
        fahrenheit = (temp_value * 9/5) + 32
        kelvin = temp_value + 273.15
        celsius = temp_value
    elif original_unit == 'fahrenheit':
        celsius = (temp_value - 32) * 5/9
        kelvin = (temp_value - 32) * 5/9 + 273.15
        fahrenheit = temp_value
    elif original_unit == 'kelvin':
        celsius = temp_value - 273.15
        fahrenheit = (temp_value - 273.15) * 9/5 + 32
        kelvin = temp_value

    return {
        'celsius': round(celsius, 2),
        'fahrenheit': round(fahrenheit, 2),
        'kelvin': round(kelvin, 2)
    }

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route for temperature conversion (AJAX call)
@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    temp_value = float(data['temperature'])
    original_unit = data['unit']
    
    # Convert temperature
    result = convert_temperature(temp_value, original_unit)
    
    # Return the result as JSON
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
