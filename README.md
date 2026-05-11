# Student Portal

A Django-based student management system for managing student records, academic information, and performance tracking.

## Features

- ✅ Student CRUD Operations (Create, Read, Update, Delete)
- ✅ Student Information Management
  - Personal details (name, email, phone, DOB, address)
  - Academic information (roll number, department, semester, CGPA, grade)
- ✅ Admin Panel for advanced management
- ✅ Responsive Bootstrap UI
- ✅ Pagination for student list
- ✅ Login-based authentication for sensitive operations

## Project Structure

```
StudentPortal/
├── StudentPortal/          # Main project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── students/               # Students app
│   ├── models.py           # Student model definition
│   ├── views.py            # Views for CRUD operations
│   ├── urls.py             # URL routing for students
│   ├── admin.py            # Admin panel configuration
│   ├── forms.py            # Form definitions (optional)
│   └── migrations/         # Database migrations
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   └── students/           # Student-specific templates
│       ├── home.html
│       ├── student_list.html
│       ├── student_detail.html
│       ├── student_form.html
│       └── student_confirm_delete.html
├── static/                 # Static files (CSS, JS, images)
│   ├── css/
│   └── js/
├── media/                  # User uploaded files
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
└── requirements.txt        # Python dependencies
```

## Installation & Setup

### 1. Clone or navigate to the project
```bash
cd StudentPortal
```

### 2. Create a virtual environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser (for admin panel)
```bash
python manage.py createsuperuser
```

### 6. Collect static files (for production)
```bash
python manage.py collectstatic
```

### 7. Run the development server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### URLs

- **Home Page**: `http://localhost:8000/`
- **Student List**: `http://localhost:8000/students/`
- **Student Detail**: `http://localhost:8000/students/<id>/`
- **Add Student**: `http://localhost:8000/students/create/`
- **Edit Student**: `http://localhost:8000/students/<id>/update/`
- **Delete Student**: `http://localhost:8000/students/<id>/delete/`
- **Admin Panel**: `http://localhost:8000/admin/`

### Admin Panel

Access the admin panel with your superuser credentials to:
- Manage students
- Filter by department, semester, or grade
- Search by roll number or email
- Bulk operations

## Database Models

### Student Model

```python
- user (OneToOne): Link to Django User model
- roll_number (CharField): Unique student ID
- department (CharField): Department name
- semester (IntegerField): Current semester
- cgpa (FloatField): Cumulative GPA
- grade (CharField): Academic grade (A-F)
- phone (CharField): Contact number
- address (TextField): Student address
- date_of_birth (DateField): DOB
- enrollment_date (DateTimeField): Auto-set on creation
- is_active (BooleanField): Student status
```

## Development

### Adding New Features

1. Create models in `students/models.py`
2. Create views in `students/views.py`
3. Update URLs in `students/urls.py`
4. Create templates in `templates/students/`
5. Register models in `students/admin.py`

### Running Tests
```bash
python manage.py test
```

### Django Shell
```bash
python manage.py shell
```

## Customization

### Change Database
Edit `StudentPortal/settings.py` DATABASES section to use PostgreSQL, MySQL, etc.

### Add Authentication
Implement Django's authentication system for login/logout functionality.

### Email Configuration
Set up email backend in settings.py for notifications.

## Troubleshooting

### Migration Issues
```bash
python manage.py makemigrations --empty students --name fix_field
python manage.py migrate
```

### Database Locked
```bash
rm db.sqlite3
python manage.py migrate
```

### Static Files Not Loading
```bash
python manage.py collectstatic --clear --noinput
```

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in settings.py
2. Update `ALLOWED_HOSTS` with your domain
3. Change `SECRET_KEY` to a strong random value
4. Use a production-grade database (PostgreSQL, MySQL)
5. Configure email backend for notifications
6. Set up HTTPS
7. Use a production WSGI server (Gunicorn, uWSGI)

## License

MIT License

## Support

For issues or questions, please create an issue in the repository.
