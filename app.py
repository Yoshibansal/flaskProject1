from flask import Flask, render_template
import numpy as np  #open terminal and install it by cmd pip3 install numpy

app = Flask(__name__)

def yoshi():
    print("Yoshi Bansal Bennett University Hello!!!")
    x = [x for x in range(10) if x%2==0]
    x = np.array(x)
    return x

temp = yoshi()

@app.route('/')
@app.route('/index')
def hello_world():
    output = temp
    if (output[0] == 0):
        text = f"Everything is Alright. {output[0]} error found"
    else:
        text = "check the syntax!!!"
    return render_template('index.html', output=output, text=text)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/images.html')
def images():
    return render_template('images.html')

if __name__ == '__main__':
    app.run(debug=True)
