# Portfolio Backend Django

[![CI/CD Pipeline](https://github.com/DryZn/Portfolio_Backend_Django/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/DryZn/Portfolio_Backend_Django/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Django REST API backend for dynamic portfolio content management.

## 🔗 Related Projects

- **Frontend**: [Portfolio](https://github.com/DryZn/portfolio) - Next.js 14 with modern UI
- **Chatbot**: [AI Assistant Portfolio](https://github.com/DryZn/AI_Assistant_Portfolio) - FastAPI RAG with LangChain

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

```bash
# With Docker Compose (PostgreSQL included)
docker-compose up -d

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Build only
docker build -t portfolio-django .
docker run -p 8000:8000 -e SECRET_KEY=your-key portfolio-django
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
