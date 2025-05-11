# 🔐 Password Generator

A simple and secure Django-based web application that allows users to generate random passwords based on custom criteria such as length and character types.

## 🚀 Features

- Generate passwords of varying lengths
- Include/exclude:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Easy-to-use web interface

## 🛠️ Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (via Django templates)
- **Database:** SQLite (default Django DB)

## 📦 Installation

Follow these steps to run the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jidet1/password-generator.git
   cd password-generator

   
2. **Create and activate a virtual environment**:
    ```python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate


3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

4. **Run migrations**:
    ```bash
    python manage.py migrate

5. **Start the development server**:
    ```bash
    python manage.py runserver

6. **Open your browser and go to http://127.0.0.1:8000**


🧪 Usage
- Choose your password length using the slider or input box.
- Select the character types you want to include.
- Click Generate Password.
- Copy and use the generated password securely!

## 📁 Project Structure
  password-generator/
├── generator/           # Main app
│   ├── templates/
│   ├── views.py
│   └── urls.py
├── password_generator/  # Project config
│   └── settings.py
├── manage.py
└── requirements.txt

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


