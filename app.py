from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form.get('user-name')
        email = request.form.get('user-email')
        password = request.form.get('user-password')

        with open('files/data.txt', 'a') as file:
            file.write(f'Имя: {name}, почта: {email}, пароль: {password}\n')
        return render_template('result.html', name = name, email = email, password = '*' * len(password))
    return  render_template('index.html')

@app.route('/all_result')
def all_result():
    with open('files/data.txt', 'r') as file:
        data = file.readlines()
    return render_template('all_result.html', data=data)
if __name__ == "__main__":
    app.run(debug=True)