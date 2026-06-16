# 🍽️ AI Recipe Generator

An AI-powered web application that generates recipe suggestions based on ingredients provided by the user. The application uses Python Flask for the backend and can optionally integrate with OpenAI GPT to generate creative and personalized recipes.

---

## 🚀 Features

- 🥗 Generate recipes from available ingredients
- 🤖 AI-powered recipe suggestions using OpenAI GPT
- 🌐 User-friendly web interface
- ⚡ Built with Flask, HTML, and CSS
- 📱 Simple and responsive design
- 🔄 Easy to customize and extend

---

## 📸 Project Overview

The user enters ingredients into the application, and the system generates suitable recipe suggestions. The application can work using predefined logic or leverage OpenAI's GPT model for more advanced recipe generation.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend Logic |
| Flask | Web Framework |
| OpenAI API | AI Recipe Generation |
| HTML5 | Frontend Structure |
| CSS3 | Styling |

---

## 📂 Project Structure

```text
AI-Recipe-Generator/
│
├── app.py              # Flask backend application
├── index.html          # Frontend webpage
├── style.css           # Styling file
├── requirements.txt    # Project dependencies
└── README.md           # Documentation
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-recipe-generator.git
cd ai-recipe-generator
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Linux/Mac**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 OpenAI API Setup (Optional)

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

---

## ▶️ Running the Application

Start the Flask server:

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User enters available ingredients.
2. Flask receives the input.
3. The application processes the ingredients.
4. OpenAI GPT generates a suitable recipe.
5. The recipe is displayed on the web interface.

---

## 🌟 Future Improvements

- Recipe filtering by cuisine
- Nutritional information
- User authentication
- Recipe saving feature
- Image generation for recipes
- Voice input support

---

## 📷 Screenshots

Add screenshots of your application here.

```markdown
![Home Page](screenshots/home.png)
```

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📜 License

This project is developed for educational and learning purposes.

---

## 👨‍💻 Author

**Soumya**

If you found this project useful, consider giving it a ⭐ on GitHub.
