# Django-weather-app

---

## 🌦️ Django Weather App

A basic, responsive weather application built with **Django** and the **Visual Crossing Weather API**. Users can search for any city and view current weather conditions like temperature, humidity, and weather descriptions.

---

### 🚀 Features

- 🌍 Search weather by city name
- 🌡️ Displays current temperature, humidity, and condition
- 📱 Fully responsive for mobile and desktop
- 🎨 Clean, modern UI inspired by top weather apps
- 🔐 Uses API keys securely via Django settings

---

### 🔧 Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3 (No frameworks)
- **API**: [Visual Crossing Weather API](https://www.visualcrossing.com)
- **Database**: SQLite (default with Django)

---

### ⚙️ Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/django-weather-app.git
cd django-weather-app
```

#### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure Environment

Create a `.env` file or add to `settings.py`:

```python
# settings.py
WEATHER_API_KEY = 'your_visual_crossing_api_key'
```

#### 5. Run Migrations

```bash
python manage.py migrate
```

#### 6. Start the Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

### 🔑 Getting a Weather API Key

1. Go to [Visual Crossing](https://www.visualcrossing.com/weather-api)
2. Sign up for a free account
3. Copy your API key from the dashboard
4. Paste it into your `settings.py` or `.env` file

---

### 🛠 Project Structure

```bash
weather_app/
│
├── weather/               # Main app
│   ├── templates/
│   │   └── weather.html   # Frontend HTML
│   ├── views.py           # Core logic
│
├── weather_app/           # Project settings
│   ├── settings.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

### 🙋‍♀️ Future Improvements

- 🌤️ Add 5-day or hourly forecast
- 📍 Detect location automatically
- 🎨 Add dark/light mode toggle
- 🧠 Cache results to reduce API calls

---

### 🤝 Contributing

Pull requests and feedback are welcome! Feel free to open an issue or fork the repo and submit a PR.

---

### 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
