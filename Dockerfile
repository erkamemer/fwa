# Temel imaj olarak Python 3.9 kullanın
FROM python:3.9

# Çalışma dizini oluşturun ve ayarlayın
WORKDIR /app

# Gereksinimleri kopyalayın
COPY requirements.txt .

# Gereksinimleri yükleyin
RUN pip install --no-cache-dir -r requirements.txt

# Uygulama kodunu kopyalayın
COPY . .

# Uygulamayı çalıştırma komutunu ayarlayın
CMD ["python", "app.py"]
