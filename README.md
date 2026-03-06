# Portfolio Backend Django

[![CI/CD Pipeline](https://github.com/DryZn/Portfolio_Backend_Django/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/DryZn/Portfolio_Backend_Django/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

Backend Django REST API pour la gestion dynamique du contenu du portfolio.

## 🔗 Projets liés

- **Frontend**: [Portfolio](https://github.com/DryZn/portfolio) - Next.js 14 avec UI moderne
- **Chatbot**: [AI Assistant Portfolio](https://github.com/DryZn/AI_Assistant_Portfolio) - FastAPI RAG avec LangChain

## 🚀 Technologies

- **Framework**: Django 5.0
- **API**: Django REST Framework
- **Base de données**: PostgreSQL / SQLite
- **Documentation**: drf-spectacular (Swagger)
- **DevOps**: Docker + GitHub Actions
- **Testing**: Pytest

## ✨ Fonctionnalités

### Interface Admin Django
- 📊 Dashboard pour gérer tout le contenu
- 📝 CRUD complet pour projets, compétences, expériences
- ✍️ Système de blog avec catégories et tags
- 📧 Gestion des messages de contact
- 🖼️ Upload d'images et médias

### API REST
- `GET /api/projects/` - Liste des projets
- `GET /api/skills/` - Compétences techniques
- `GET /api/experience/` - Expériences professionnelles
- `GET /api/blog/posts/` - Articles de blog
- `POST /api/contact/` - Formulaire de contact
- `GET /api/docs/` - Documentation Swagger

## 📦 Installation

### Prérequis
- Python 3.11+
- PostgreSQL (optionnel, SQLite par défaut)

### Installation locale

```bash
# Cloner le repo
git clone https://github.com/DryZn/Portfolio_Backend_Django.git
cd Portfolio_Backend_Django

# Créer environnement virtuel
python -m venv venv

# Activer (Windows)
venv\Scripts\activate

# Activer (Linux/Mac)
source venv/bin/activate

# Installer dépendances
pip install -r requirements.txt

# Configurer variables d'environnement
copy .env.example .env

# Migrations
python manage.py migrate

# Créer superuser
python manage.py createsuperuser

# Lancer serveur
python manage.py runserver
```

Accéder à :
- API: http://localhost:8000/api/
- Admin: http://localhost:8000/admin/
- Docs: http://localhost:8000/api/docs/

## 🐳 Docker

```bash
# Avec Docker Compose (PostgreSQL inclus)
docker-compose up -d

# Créer superuser
docker-compose exec web python manage.py createsuperuser

# Build seul
docker build -t portfolio-django .
docker run -p 8000:8000 -e SECRET_KEY=your-key portfolio-django
```

## ⚙️ Configuration

Variables d'environnement dans `.env` :

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
├── config/              # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── projects/        # Gestion des projets
│   ├── skills/          # Compétences
│   ├── experience/      # Expériences pro
│   ├── blog/            # Blog technique
│   └── contact/         # Messages de contact
├── tests/               # Tests pytest
├── media/               # Fichiers uploadés
├── staticfiles/         # Fichiers statiques
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🧪 Tests

```bash
# Installer dépendances dev
pip install -r requirements-dev.txt

# Lancer tests
pytest tests/ -v

# Avec coverage
pytest tests/ --cov=apps

# Linting
black .
flake8 .

# Sécurité
bandit -r apps/ config/
```

## 🚀 Déploiement

### Render

1. Créer compte sur [Render](https://render.com)
2. Nouveau Web Service
3. Connecter repo GitHub
4. Configuration :
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn config.wsgi:application`
5. Variables d'environnement :
   - `SECRET_KEY`
   - `DATABASE_URL` (PostgreSQL Render)
   - `ALLOWED_HOSTS`

### Railway

1. Créer compte sur [Railway](https://railway.app)
2. New Project → Deploy from GitHub
3. Ajouter PostgreSQL
4. Variables d'environnement automatiques

## 📊 Modèles de données

### Project
- Titre, description, technologies
- URLs GitHub et démo
- Image, statut, ordre
- Compteur de vues

### Skill
- Nom, catégorie, niveau
- Années d'expérience
- Icône

### Experience
- Entreprise, poste, localisation
- Dates début/fin
- Description, réalisations
- Technologies utilisées

### Blog Post
- Titre, contenu, extrait
- Catégorie, tags
- Image de couverture
- Statut (brouillon/publié)

### Contact Message
- Nom, email, sujet, message
- Statut lu/répondu

## 🔐 Sécurité

- CORS configuré pour frontend
- CSRF protection activée
- Permissions REST Framework
- Admin protégé par authentification
- Variables sensibles dans .env

## 📝 Utilisation

### Ajouter un projet via admin

1. Aller sur `/admin/`
2. Projets → Ajouter
3. Remplir formulaire
4. Sauvegarder
5. Visible sur API `/api/projects/`

### Écrire un article de blog

1. Admin → Blog → Articles
2. Nouveau post
3. Choisir catégorie et tags
4. Statut "Publié"
5. Accessible via `/api/blog/posts/`

## 🤝 Contribution

Les contributions sont bienvenues ! Ouvrez une issue ou PR.

## 📄 Licence

MIT License - voir [LICENSE](LICENSE)

## 📧 Contact

Anthony Lesenfans - lesenfans.anthony@gmail.com
