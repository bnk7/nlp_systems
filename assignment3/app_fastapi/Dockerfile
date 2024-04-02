FROM python:slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN apt-get update && apt-get install -y curl
CMD ["uvicorn", "app_fastapi:app", "--reload", "host=0.0.0.0.8000"]