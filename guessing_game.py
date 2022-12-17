from flask import Flask, render_template, request
from random import randint


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def game_loop():
    if request.method == 'POST':
        mi_num = int(request.form['min'])
        mx_num = int(request.form['max'])
        pc_number = int(request.form['guess'])
        p_answer = request.form['answer']
        if p_answer == 'too big':
            mx_num = pc_number
        elif p_answer == 'too small':
            mi_num = pc_number
        else:
            msg = 'I have won!'
            return msg

        pc_number = randint(mi_num, mx_num)
        return render_template('index.html', pc_number=pc_number, mi_num=mi_num, mx_num=mx_num)
    else:
        mi_num = 0
        mx_num = 1000
        pc_number = randint(mi_num, mx_num)
        return render_template('index.html', pc_number=pc_number, mi_num=mi_num, mx_num=mx_num)


if __name__ == '__main__':
    app.run(debug=True)
