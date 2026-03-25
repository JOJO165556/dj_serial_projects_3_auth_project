# auth_project

API REST d'authentification construite avec **Django 6** et **Django REST Framework**.

## Stack

- Django 6 + DRF
- JWT via `djangorestframework-simplejwt`
- SQLite (dev)
- `django-unfold` pour l'interface admin

## Installation

```bash
git clone <repo>
cd auth_project
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Créer un fichier `.env` à la racine :

```env
SECRET_KEY=your-secret-key
DEBUG=True
```

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Endpoints

| Méthode | URL | Description | Auth |
|---------|-----|-------------|------|
| `POST` | `/api/register` | Créer un compte | Non |
| `POST` | `/api/token` | Obtenir access + refresh token | Non |
| `POST` | `/api/token/refresh/` | Rafraîchir le token | Non |
| `GET` | `/api/me/` | Profil de l'utilisateur connecté | Oui |
| `POST` | `/api/logout/` | Révoquer le refresh token | Oui |

> Les routes protégées nécessitent un header `Authorization: Bearer <access_token>`.

## Structure

```
auth_project/
├── core/          # Settings, URLs racine
├── apps/
│   └── users/     # Modèle utilisateur, permissions
└── api/
    ├── views/     # Vues (auth, users)
    ├── serializers/
    └── routers.py
```
