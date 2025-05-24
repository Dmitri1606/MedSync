from flask import Flask, render_template
import sqlite3
import os
from flask import Flask, render_template

app = Flask(__name__)

# Проверка существования папки templates
print("Путь к templates:", os.path.join(os.path.dirname(__file__), 'templates'))
print("Содержимое папки:", os.listdir(os.path.dirname(__file__)))

@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

# Создаём базу данных
def create_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Таблица врачей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            login TEXT UNIQUE,
            password TEXT
        )
    ''')

    # Таблица пациентов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            diagnosis TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_db()  # Вызываем при запуске

# Страница входа
@app.route('/')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)