from flask import Flask, render_template, request
import numpy as np
from scipy import stats

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_points = int(request.form['num_points'])
        x_values = []
        y_values = []

        for i in range(num_points):
            x = float(request.form[f'x_{i}'])
            y = float(request.form[f'y_{i}'])
            x_values.append(x)
            y_values.append(y)

        x_values = np.array(x_values)
        y_values = np.array(y_values)

        slope, intercept, r_value, p_value, std_err = stats.linregress(x_values, y_values)
        
        return render_template('index.html', results=True, slope=slope, intercept=intercept, r_squared=r_value**2)

    return render_template('index.html', results=False)

if __name__ == '__main__':
    app.run(debug=True)
