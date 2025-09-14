import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "morfeo.settings")
django.setup()

User = get_user_model()

USERNAME = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
EMAIL = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com")
PASSWORD = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin123")  # ¡solo para pruebas!

if not User.objects.filter(username=USERNAME).exists():
    User.objects.create_superuser(USERNAME, EMAIL, PASSWORD)
    print(f"Superusuario '{USERNAME}' creado.")
else:
    print(f"Superusuario '{USERNAME}' ya existe.")
