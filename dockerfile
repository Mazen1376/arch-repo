FROM python:3.8-slim
WORKDIR /app
COPY server.py /app
RUN pip install flask prometheus-client
CMD ["python", "server.py"]