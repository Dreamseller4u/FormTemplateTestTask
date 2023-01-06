from flask import Flask, render_template, request, redirect
from service import get_match, find_match, find_match_s

app = Flask(__name__)


@app.route("/")
def index():
    return redirect('/get_form/')


@app.route('/get_form/', methods=('GET', 'POST'))
def get_form():
    '''
        Вывод совпадающих шаблонов
        только по заначением полей
    '''
    if request.method == 'POST':
        req_forms = request.form.items()
        matches = [get_match(i) for _, i in req_forms]
        match_form = find_match(matches)
        return render_template('forms.html', match_form=match_form)

    return render_template('forms.html')


@app.route('/get_form_second/', methods=('GET', 'POST'))
def get_form_second():
    '''
        Вывод совпадающих шаблонов
        по заначением и именам полей
    '''
    if request.method == 'POST':
        data = [
            {
                request.form['f_name1']: get_match(request.form['f_value1']),         #Взял данные из форм таким образом, если использовать
                request.form['f_name2']: get_match(request.form['f_value2'])          # запрос как в задании " f_name1=value1&f_name2=value2"
            }                                                                         # написал бы через request.get_arg и впринцепи логига была бы такая же
        ]
        match_form = find_match_s(data)
        return render_template('second_forms.html', match_form=match_form)

    return render_template('second_forms.html')


if __name__ == "__main__":
    app.run()
