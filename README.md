# 🚀 Nexus Ultra — Code Snippet Manager, https://nexus-ultra.onrender.com

**Nexus Ultra** is a full-stack web application designed to help developers store, organize, and search code snippets efficiently. Built with Django, PostgreSQL, and Tailwind CSS, it provides a clean, responsive UI and secure user authentication — perfect for anyone who wants to manage their code libraries in one place.

---

## 🌟 Features

- 🔐 **User Authentication** — Secure login/registration using Django's built-in auth system
- 🧠 **Personal Snippet Libraries** — Each user gets a private snippet collection
- 🔎 **Search Functionality** — Quickly find snippets by title, language, or tags
- 🎨 **Responsive UI** — Clean, modern frontend built with Tailwind CSS
- 💾 **PostgreSQL Integration** — Persistent storage with robust querying
- 🚀 **Deployed on Render** — Production-ready with environment variable configuration

---

## 🛠️ Tech Stack

**Frontend:**  
- HTML5  
- Tailwind CSS  
- JavaScript  

**Backend:**  
- Python  
- Django  
- PostgreSQL  

**Deployment:**  
- Render

---


## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Bryxel/nexus-ultra.git
cd nexus-ultra

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (create a .env file if needed)
# Example:
# SECRET_KEY=your-secret-key
# DEBUG=True

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
