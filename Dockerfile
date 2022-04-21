FROM python:3.8.12
WORKDIR /app
COPY . .
CMD ["python3", "./game.py"]