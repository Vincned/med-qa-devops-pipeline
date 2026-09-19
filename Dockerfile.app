# 1. Берем легкий базовый образ Python
FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# 2. Создаем рабочую папку внутри контейнера
WORKDIR /workspace

# 3. Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Копируем исходный код нашего API из папки app
COPY app/ ./app

# 5. Команда запуска сервера FastAPI при старте контейнера
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]