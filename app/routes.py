from flask import request, render_template, url_for, redirect, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, logout_user
from app import app, db
from app.models import User

'''
@app.route('/users/', methods=['POST', 'GET', 'DELETE'])
def users(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_user = User(email=data['email'], password=['password'], fullname=data['fullname'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"Пользователь {new_user.fullname} был успешно создан."}
        else:
            return {"error": "Возникла ошибка, неверно указан пользователь"}

    elif request.method == 'GET':
        users_all = User.query.all()
        results = [
            {
                "email": user.email,
                "password": user.password,
                "fullname": user.fullname
            } for user in users_all]

        return {"Все пользователи": results}

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return {"message": f"Пользователь {user.fullname} успешно удален"}
'''

#GET - возвращает форму авторизации
#POST - данные которые пришли от пользователя

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    email = request.form.get('email')
    password = request.form.get('password')

    if email and password:
        user = User.query.filter_by(email=email).first()
        #проверка авторизации
        if check_password_hash(user.password, password):
            login_user(user)

            #перенаправление пользователя на страничку которую он хотел попасть
            next_page = request.args.get('next')
            redirect(next_page)
        #если пароли не совпадают
        else:
            flash('Пароль или логин введены некоректно')
    else:
        flash('Введите логин пароль')
        return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    email = request.form.get('email')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not(email or password or password2):
            flash('Пожалуйста заполните все поля')
        elif password != password2:
            flash('Пароли не совпадают')
        else:
            hash_pwd = generate_password_hash(password)
            new_user = User(email=email, password=hash_pwd)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login_page'))



    return render_template('register.html')



@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
