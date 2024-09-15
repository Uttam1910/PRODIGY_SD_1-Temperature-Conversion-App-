function convertTemperature() {
    const temp = parseFloat(document.getElementById('temp').value);
    const unit = document.getElementById('unit').value;

    let celsius, fahrenheit, kelvin;

    if (unit === 'celsius') {
        celsius = temp;
        fahrenheit = (celsius * 9/5) + 32;
        kelvin = celsius + 273.15;
    } else if (unit === 'fahrenheit') {
        fahrenheit = temp;
        celsius = (fahrenheit - 32) * 5/9;
        kelvin = celsius + 273.15;
    } else if (unit === 'kelvin') {
        kelvin = temp;
        celsius = kelvin - 273.15;
        fahrenheit = (celsius * 9/5) + 32;
    }

    document.getElementById('result-celsius').innerText = `Celsius: ${celsius.toFixed(2)} °C`;
    document.getElementById('result-fahrenheit').innerText = `Fahrenheit: ${fahrenheit.toFixed(2)} °F`;
    document.getElementById('result-kelvin').innerText = `Kelvin: ${kelvin.toFixed(2)} K`;
}
