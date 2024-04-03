FROM python:slim
WORKDIR /app
COPY . .
RUN pip install -r app_fastapi/requirements.txt
RUN python -m spacy download en_core_web_sm
RUN apt-get update && apt-get install -y curl
CMD ["uvicorn", "app_fastapi.fastapi_app:app", "--reload"]