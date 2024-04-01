FROM python:slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN apt-get update && apt-get install -y curl
CMD ["uvicorn", "app_fastapi:app"]
CMD ["curl", "http://127.0.0.1:8000?pretty=true"]