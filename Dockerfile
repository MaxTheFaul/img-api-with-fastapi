FROM python:alpine

WORKDIR /app/api/img

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "80"]

