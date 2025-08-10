from flask import *
import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv(".gitignore/admin.env")

cursor = <connection-name>.cursor(buffered=True)
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", os.urandom(24))

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

@app.route('/contact', methods=['GET', 'POST', 'HEAD'])
def contact():
    if request.method == "POST":
        subject = request.form.get('subject')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        comment = request.form.get('message')

        msg = f"📩 Нове повідомлення з сайту:\n✍️ Тема: {subject}\n👤 Ім'я: {name}\n📧 Email: {email}\n📞 Телефон: {phone}\n💬 Повідомлення: {comment}"
        send_to_telegram(msg)
        return render_template('contact.html', success=True)

    return render_template('contact.html')
def index():
    return render_template('index.html')


def specialty_IT():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('speciality_IT.html')
def specialty_mentor():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('speciality_mentor.html')

def advice():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('advice.html')

def achievements():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('achievements.html')
def support():
    return render_template('support.html')
#enLISH

def index_en():
    return render_template('index_en.html')


def specialty_IT_en():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('speciality_IT_en.html')
def specialty_mentor_en():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('speciality_mentor_en.html')

def advice_en():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('advice_en.html')

def achievements_en():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('achievements_en.html')

def contact_en():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('contact_en.html')

def support_en():
    return render_template('support_en.html')
#CZECH

def index_cz():
    return render_template('index_cz.html')


def specialty_IT_cz():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('speciality_IT_cz.html')
def specialty_mentor_cz():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('speciality_mentor_cz.html')

def advice_cz():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('advice_cz.html')

def achievements_cz():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('achievements_cz.html')

def contact_cz():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('contact_cz.html')
def support_cz():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('support_cz.html')
# Створюємо об'єкт веб-програми:

# створюємо правило для URL '/':
app.add_url_rule('/', 'index', index)
app.add_url_rule('/speciality_IT.html', 'speciality_IT', specialty_IT)
app.add_url_rule('/speciality_mentor.html', 'speciality_mentor', specialty_mentor)
app.add_url_rule('/advice.html', 'advice', advice)
app.add_url_rule('/contact.html', 'contact', contact)
app.add_url_rule('/support.html', 'support', support)
app.add_url_rule('/achievements.html', 'achievements', achievements)

app.add_url_rule('/index_en.html','index_en', index_en)
app.add_url_rule('/speciality_IT_en.html', 'speciality_IT_en', specialty_IT_en)
app.add_url_rule('/speciality_mentor.html_en', 'speciality_mentor_en', specialty_mentor_en)
app.add_url_rule('/advice_en.html', 'advice_en', advice_en)
app.add_url_rule('/contact_en.html', 'contact_en', contact_en)
app.add_url_rule('/support_en.html', 'support_en', support_en)
app.add_url_rule('/achievements_en.html', 'achievements_en', achievements_en)

app.add_url_rule('/index_cz.html', 'index_cz', index_cz)
app.add_url_rule('/speciality_IT_cz.html', 'speciality_IT_cz', specialty_IT_cz)
app.add_url_rule('/speciality_mentor_cz.html', 'speciality_mentor_cz', specialty_mentor_cz)
app.add_url_rule('/advice_cz.html', 'advice_cz', advice_cz)
app.add_url_rule('/contact_cz.html', 'contact_cz', contact_cz)
app.add_url_rule('/support_cz.html', 'support_cz', support_cz)
app.add_url_rule('/achievements_cz.html', 'achievements_cz', achievements_cz)

if __name__ == "__main__":
    # Запускаємо веб-сервер:
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)



