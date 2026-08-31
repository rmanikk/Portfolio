# Manik Kafle — Developer Portfolio

> A quiet portfolio for loud work — built with Django, PostgreSQL, Tailwind CSS, and vanilla JavaScript.

This repository contains my personal developer portfolio: a responsive, content-driven website where projects, experience, writing, and contact messages are managed through Django's admin panel rather than being hardcoded into templates.

## ✦ What it does

The portfolio is designed around a simple idea: **keep the interface minimal, keep the content manageable, and let the work speak for itself.**

- **Home** — introduction, featured experience, featured projects, and featured blog posts
- **Projects** — project collection with descriptions, technologies, images, GitHub links, and live links
- **Project details** — dedicated pages with rich project descriptions and related projects
- **Experience** — company-based experience timeline with roles, employment type, technologies, duration, and key work
- **Blog** — published articles with categories, cover images, excerpts, and rich content
- **Contact** — validated contact form with messages stored in the database
- **Django Admin** — manage projects, experience, companies, blog posts, and contact messages
- **Light / Dark theme** — persistent theme selection using `localStorage`
- **Responsive UI** — designed to work across desktop, tablet, and mobile layouts
- **Rich text editing** — CKEditor 5 for project and blog content
- **Media management** — project, blog, company, and site imagery served through Django media handling

---

## 🛠 Tech Stack

| Layer | Technology |
| --- | --- |
| Backend | Python, Django 6.1 |
| Database | PostgreSQL |
| Frontend | Django Templates, HTML, CSS, Vanilla JavaScript |
| Styling | Tailwind CSS 4 |
| Rich Text | Django CKEditor 5 |
| Database Driver | Psycopg 3 |
| Environment | `python-dotenv` |
| WSGI | Gunicorn-ready Django WSGI structure |
| Package Management | `pip` + `npm` |

---

## 📁 Project Structure

```text
portfolio/
├── apps/
│   ├── core/
│   │   └── Home page and shared portfolio logic
│   ├── projects/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── experience/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   ├── blog/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   └── contact/
│       ├── models.py
│       ├── forms.py
│       ├── views.py
│       ├── urls.py
│       └── admin.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   ├── home/
│   ├── projects/
│   ├── experience/
│   ├── blog/
│   └── contact/
│
├── static/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── documents/
│
├── media/
├── manage.py
├── package.json
├── package-lock.json
├── requirements.txt
└── .gitignore
```

---

## 🧩 Architecture

The project follows a Django app-based structure so each major section of the portfolio has its own responsibility.

### Core

The `core` app handles the homepage and pulls featured content from the other portfolio apps.

The homepage dynamically displays:

- up to two featured projects
- up to two published featured blog posts
- the featured experience entry

### Projects

Projects are stored in PostgreSQL and rendered dynamically.

Each project can contain:

- title
- automatically generated slug
- short description
- rich description
- image
- GitHub URL
- live/demo URL
- technology list
- featured status
- display order

Project detail pages also include an "Explore More Projects" section.

### Experience

Experience is separated into:

- **Company**
- **Experience**
- **ExperienceBullet**

This allows multiple roles to belong to a company while keeping individual responsibilities/work items organized.

The experience model also calculates a simple duration such as:

```text
5m
1y
1y 4m
```

Only one experience can be marked as featured.

### Blog

Blog posts support:

- categories
- excerpts
- rich text content
- cover images
- publishing state
- featured state
- publication timestamps
- automatic slugs

Only published posts appear on the public blog.

### Contact

The contact page uses a Django `ModelForm`.

Submitted messages are stored as `ContactMessage` records containing:

- name
- email
- subject
- message
- creation timestamp
- read/unread status

This makes incoming messages accessible from Django Admin.

---

## 🎨 Frontend

The frontend uses Django templates rather than a separate SPA framework.

### Styling

Tailwind CSS 4 is compiled from:

```text
static/css/input.css
```

into:

```text
static/css/output.css
```

Additional section-specific styles are maintained separately:

```text
static/css/
├── theme.css
├── experience.css
├── projects.css
├── blog.css
└── contact.css
```

### JavaScript

Interactive behavior is handled by:

```text
static/js/main.js
```

The current interface includes theme switching and interactive UI behavior such as cursor effects and expandable experience content.

### Theme system

The site supports:

- Dark mode
- Light mode
- Persistent theme selection

The selected theme is stored in the browser using `localStorage`.

The site also includes separate dark/light hero background assets:

```text
static/images/hero-bg.png
static/images/hero-bg-light.png
```

---

## ⚙️ Local Development

### 1. Clone the repository

```bash
git clone https://github.com/rmanikk/Portfolio.git
cd Portfolio
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

The current codebase also imports `django_ckeditor_5` and `dateutil`. If they are not present in your installed environment, install them with:

```bash
pip install django-ckeditor-5 python-dateutil
```

### 4. Install frontend dependencies

```bash
npm install
```

### 5. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

Do **not** commit your real `.env` file.

### 6. Create the PostgreSQL database

Create a PostgreSQL database and user matching the values in `.env`.

Then apply Django migrations:

```bash
python manage.py migrate
```

### 7. Create an admin account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your Django admin credentials.

### 8. Build Tailwind CSS

For development with automatic rebuilding:

```bash
npm run dev
```

For a production build:

```bash
npm run build
```

### 9. Start Django

In another terminal:

```bash
python manage.py runserver
```

The site will be available at:

```text
http://127.0.0.1:8000/
```

Django Admin:

```text
http://127.0.0.1:8000/admin/
```

---

## 🗄️ Content Management

Once logged into Django Admin, portfolio content can be managed without editing templates.

### Projects

Add and manage:

- project information
- project image
- technologies
- GitHub link
- live link
- featured status
- display order

### Experience

Manage:

- companies
- roles
- employment types
- dates
- technologies
- featured experience
- key work bullets

### Blog

Create and manage:

- articles
- categories
- cover images
- rich content
- publication status
- featured posts

### Contact Messages

View messages submitted through the public contact form and mark them as read.

---

## 🔗 Routes

| Page | Route |
| --- | --- |
| Home | `/` |
| Projects | `/projects/` |
| Project Detail | `/projects/<slug>/` |
| Blog | `/blog/` |
| Blog Detail | `/blog/<slug>/` |
| Experience | `/experience/` |
| Contact | `/contact/` |
| Admin | `/admin/` |

---

## 🔐 Security & Configuration

The repository is configured to keep sensitive/local files out of version control:

```text
.env
.env.*
venv/
node_modules/
db.sqlite3
media/
staticfiles/
__pycache__/
```

For deployment, remember to:

- set `DEBUG=False`
- configure `ALLOWED_HOSTS`
- use a strong production `SECRET_KEY`
- keep database credentials in environment variables
- configure static/media storage appropriately
- serve the application through a production WSGI/ASGI setup
- review Django's deployment security checklist

---

## 🚀 Production Notes

The project is structured around Django's standard WSGI/ASGI entry points:

```text
config/wsgi.py
config/asgi.py
```

Before deploying, build the frontend assets:

```bash
npm run build
```

Then collect Django static files:

```bash
python manage.py collectstatic
```

The production database should be PostgreSQL rather than the local development database.

---

## 🧠 Design Philosophy

This portfolio intentionally avoids unnecessary complexity.

No frontend framework.  
No oversized component library.  
No hardcoded project cards.

Just Django handling the data, Tailwind handling the styling, JavaScript handling the interactions, and the admin panel handling the content.

> **Less noise. More signal.**

---

## 📌 Future Improvements

Possible future additions include:

- automated email notifications for contact messages
- pagination for projects and blog posts
- search/filtering for blog content
- richer analytics
- SEO/Open Graph metadata
- sitemap and robots configuration
- production media storage
- automated deployment pipeline
- automated tests for portfolio apps

---

## 👤 Author

**Manik Kafle**  
Software Engineer / Full-stack Developer

- LinkedIn: https://www.linkedin.com/in/rm4nik/
- GitHub: https://github.com/rmanikk

---

## 📄 License

This project is primarily a personal portfolio. The code can be referenced for learning and inspiration, but personal content, branding, imagery, resume files, and portfolio materials should not be reused without permission.
