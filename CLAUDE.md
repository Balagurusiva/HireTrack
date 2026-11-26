# HireTrack

A job application tracker: Kanban board of applications, resume–JD matcher, reminders, and a dashboard.

## Stack

- **Backend** (`/backend`): Django 5, Django REST Framework, MySQL 8, SimpleJWT (auth), Celery + Redis (background jobs, reminders)
- **Frontend** (`/frontend`): Next.js (App Router), TypeScript, Tailwind CSS, Redux Toolkit

## How to work with me

- I'm learning Django. Before writing code that uses a new Django/DRF concept (models, migrations, serializers, viewsets, permissions, signals, Celery tasks, etc.), give a short plain-language explanation of what it is and why we need it.
- Work in small steps: one focused change at a time, and explain what changed.
- Commit after each completed feature (with its tests passing).

## Rules

- **Secrets** live in `.env` files only (DB credentials, `SECRET_KEY`, JWT settings, Redis URL). Never commit `.env`; keep a `.env.example` with placeholder values up to date.
- **Custom User model**: email-based login (no username). Defined before the first migration and referenced via `settings.AUTH_USER_MODEL` / `get_user_model()`, never `django.contrib.auth.models.User` directly.
- **Data isolation**: every queryset must be scoped to `request.user` (e.g. override `get_queryset()` to filter by `user=self.request.user`, and set `user` in `perform_create`). Never return or modify another user's data.
- **Tests**: write pytest tests (pytest-django) for every API endpoint, covering the happy path, auth required, and that users can't access each other's data.
