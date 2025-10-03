# Image de base
FROM python:3.10-slim

# Créer un utilisateur non-root pour la sécurité
RUN adduser --system --group appuser

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier l'application
COPY app.py .

# Changer la propriété du dossier et des fichiers à l'utilisateur non-root
RUN chown -R appuser:appuser /app

# Passer à l'utilisateur non-root
USER appuser

# Exposer le port de l'application (pour information)
EXPOSE 5000

# Lancer l'app
CMD ["python", "app.py"]
