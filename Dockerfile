
# Python 3.9 imajını kullan
FROM python:3.9

# Çalışma dizinini ayarla
WORKDIR /app

# Python dosyasını kopyala
COPY main.py .

# Uygulamayı çalıştır
CMD ["python", "main.py"]

