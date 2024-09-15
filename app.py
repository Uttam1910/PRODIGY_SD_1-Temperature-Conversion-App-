from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for temperature conversion logic
@app.route('/convert', methods=['POST'])
def convert_temperature():
    try:
        # Check if the request is JSON or form-encoded
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form

        temp = float(data.get('temperature'))
        unit = data.get('unit').lower()

        # Conversion logic
        conversions = {
            'celsius': {
                'fahrenheit': (temp * 9/5) + 32,
                'kelvin': temp + 273.15
            },
            'fahrenheit': {
                'celsius': (temp - 32) * 5/9,
                'kelvin': ((temp - 32) * 5/9) + 273.15
            },
            'kelvin': {
                'celsius': temp - 273.15,
                'fahrenheit': ((temp - 273.15) * 9/5) + 32
            }
        }

        if unit not in conversions:
            return jsonify({'error': 'Invalid unit provided. Use celsius, fahrenheit, or kelvin.'}), 400

        # Calculate other temperature units
        celsius = temp if unit == 'celsius' else conversions[unit]['celsius']
        fahrenheit = temp if unit == 'fahrenheit' else conversions[unit]['fahrenheit']
        kelvin = temp if unit == 'kelvin' else conversions[unit]['kelvin']

        # Return the results
        return jsonify({
            'celsius': round(celsius, 2),
            'fahrenheit': round(fahrenheit, 2),
            'kelvin': round(kelvin, 2)
        })
    
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid input. Please provide a valid number for temperature.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
