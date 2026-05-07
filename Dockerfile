echo FROM python:3.9-slim > Dockerfile
echo WORKDIR /app >> Dockerfile
echo COPY app.py train.py config.json requirements.txt ./ >> Dockerfile
echo RUN pip install --no-cache-dir -r requirements.txt >> Dockerfile
echo EXPOSE 8000 >> Dockerfile
echo CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"] >> Dockerfile