# Portfolio Backend Django

[![CI/CD Pipeline](https://github.com/DryZn/Portfolio_Backend_Django/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/DryZn/Portfolio_Backend_Django/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Django REST API backend for dynamic portfolio content management.

## 🔗 Related Projects

This Django backend is part of a complete portfolio ecosystem:

| Repository | Technology | Purpose | URL |
|------------|------------|---------|-----|
| [portfolio](https://github.com/DryZn/portfolio) | Next.js 14 | Frontend UI | https://portfolio-anthony-lesenfans.vercel.app |
| [AI_Assistant_Portfolio](https://github.com/DryZn/AI_Assistant_Portfolio) | FastAPI + LangChain | RAG Chatbot | https://ai-assistant-portfolio-eka7.onrender.com |
| **Portfolio_Backend_Django** | Django + DRF | CMS & API | (This repo) |

**Each service is independent and can be deployed separately.**

## 🚀 Technologies

- **Framework**: Django 5.0
- **API**: Django REST Framework
- **Database**: PostgreSQL / SQLite
- **Documentation**: drf-spectacular (Swagger)
- **DevOps**: Docker + GitHub Actions
- **Testing**: Pytest

## ✨ Features

### Django Admin Interface
- 📊 Dashboard to manage all content
- 📝 Full CRUD for projects, skills, experiences
- ✍️ Blog system with categories and tags
- 📧 Contact message management
- 🖼️ Image and media uploads

### REST API
- `GET /api/projects/` - Project list
- `GET /api/skills/` - Technical skills
- `GET /api/experience/` - Professional experiences
- `GET /api/blog/posts/` - Blog posts
- `POST /api/contact/` - Contact form
- `GET /api/docs/` - Swagger documentation

## 📦 Installation

### Prerequisites
- Python 3.11+
- PostgreSQL (optional, SQLite by default)

### Local Installation

```bash
# Clone repo
git clone https://github.com/DryZn/Portfolio_Backend_Django.git
cd Portfolio_Backend_Django

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
copy .env.example .env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

Access:
- API: http://localhost:8000/api/
- Admin: http://localhost:8000/admin/
- Docs: http://localhost:8000/api/docs/

## 🐳 Docker

### This Service Only (Django + PostgreSQL)

```bash
# Start Django with PostgreSQL
docker-compose up -d

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# View logs
docker-compose logs -f web

# Stop
docker-compose down
```

### Standalone Docker Build

```bash
docker build -t portfolio-django .
docker run -p 8000:8000 -e SECRET_KEY=your-key -e DEBUG=True portfolio-django
```

## ⚙️ Configuration

Environment variables in `.env`:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgresql://user:pass@localhost:5432/portfolio_db
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

## 🌐 Full-Stack Development

To run the complete portfolio ecosystem locally:

```bash
# Terminal 1 - Frontend (Next.js)
cd portfolio
npm install
npm run dev
# → http://localhost:3000

# Terminal 2 - Chatbot API (FastAPI)
cd AI_Assistant_Portfolio
pip install -r requirements.txt
uvicorn src.main:app --reload --port 8000
# → http://localhost:8000

# Terminal 3 - Backend API (Django)
cd Portfolio_Backend_Django
pip install -r requirements.txt
python manage.py runserver 8001
# → http://localhost:8001
```

**Architecture:**
```
┌─────────────────┐
│  Next.js :3000  │  Frontend (Public)
└────────┬────────┘
         │
    ┌────┴────┐
    ↓         ↓
┌─────────┐ ┌──────────┐
│FastAPI  │ │ Django   │
│:8000    │ │ :8001    │
│Chatbot  │ │ CMS/API  │
└─────────┘ └──────────┘
```

**Note:** Each service is in a separate repository and can be deployed independently.

## 📁 Structure

```
Portfolio_Backend_Django/
├── config/              # Django configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── projects/        # Project management
│   ├── skills/          # Skills
│   ├── experience/      # Professional experience
│   ├── blog/            # Technical blog
│   └── contact/         # Contact messages
├── tests/               # Pytest tests
├── media/               # Uploaded files
├── staticfiles/         # Static files
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🧪 Tests

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/ -v

# With coverage
pytest tests/ --cov=apps

# Linting
black .
flake8 .

# Security
bandit -r apps/ config/
```

## 🚀 Deployment

### Render

1. Create account on [Render](https://render.com)
2. New Web Service
3. Connect GitHub repo
4. Configuration:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn config.wsgi:application`
5. Environment variables:
   - `SECRET_KEY`
   - `DATABASE_URL` (Render PostgreSQL)
   - `ALLOWED_HOSTS`

### Railway

1. Create account on [Railway](https://railway.app)
2. New Project → Deploy from GitHub
3. Add PostgreSQL
4. Automatic environment variables

## 📊 Data Models

### Project
- Title, description, technologies
- GitHub and demo URLs
- Image, status, order
- View counter

### Skill
- Name, category, level
- Years of experience
- Icon

### Experience
- Company, position, location
- Start/end dates
- Description, achievements
- Technologies used

### Blog Post
- Title, content, excerpt
- Category, tags
- Cover image
- Status (draft/published)

### Contact Message
- Name, email, subject, message
- Read/replied status

## 🔐 Security

- CORS configured for frontend
- CSRF protection enabled
- REST Framework permissions
- Admin protected by authentication
- Sensitive variables in .env

## 📝 Usage

### Add a project via admin

1. Go to `/admin/`
2. Projects → Add
3. Fill form
4. Save
5. Visible on API `/api/projects/`

### Write a blog post

1. Admin → Blog → Posts
2. New post
3. Choose category and tags
4. Status "Published"
5. Accessible via `/api/blog/posts/`

## 🤝 Contributing

Contributions are welcome! Open an issue or PR.

## 📄 License

MIT License - see [LICENSE](LICENSE)

## 📧 Contact

Anthony Lesenfans - lesenfans.anthony@gmail.com
