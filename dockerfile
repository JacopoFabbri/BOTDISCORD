# Usa un'immagine base ufficiale di Python
FROM python:3.9-slim

# Imposta la directory di lavoro all'interno del container
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt .

# Installa le dipendenze Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del codice sorgente nella directory di lavoro
COPY . .

ENV DISCORD_TOKEN=MTI0OTg0NjQ0MTU1MjI0ODkxMg.Gngvgp.sMErwmdmu4SmB5n-7bL0qJLo_89qzwiU1EqtfQ

# Comando per avviare l'applicazione
# Cambia "app.py" con il nome del tuo file di esecuzione principale
CMD ["python", "Bimusso_bot.py"]