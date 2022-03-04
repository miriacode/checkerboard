from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_default_checkerboard():
    return render_template('index.html',columns=8, rows=8, color_one="black", color_two="red")

@app.route('/<int:rows>')
def show_8_4_chekerboard(rows):
    return render_template('index.html',rows=rows, columns=8, color_one="black", color_two="red")

@app.route('/<int:rows>/<int:columns>')
def show_columns_rows_chekerboard(rows, columns):
    return render_template('index.html',rows=rows, columns=columns, color_one="black",color_two="red")

@app.route('/<int:rows>/<int:columns>/<string:color_one>')
def show_columns_rows_color_one_chekerboard(rows, columns,color_one):
    return render_template('index.html',rows=rows, columns=columns, color_one=color_one)

@app.route('/<int:rows>/<int:columns>/<string:color_one>/<string:color_two>')
def show_columns_rows_color_one_color_two_chekerboard(rows, columns, color_one, color_two):
    return render_template('index.html',rows=rows, columns=columns,color_one=color_one,color_two=color_two)

if __name__ == '__main__':
    app.run(debug=True)