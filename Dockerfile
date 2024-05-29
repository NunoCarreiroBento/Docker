FROM alpine:latest

COPY app.py .

CMD ["python", "app.py"]
