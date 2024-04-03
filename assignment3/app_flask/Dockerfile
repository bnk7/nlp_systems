FROM python:slim
WORKDIR /app
COPY . .
RUN pip install -r app_flask/requirements.txt
RUN python -m spacy download en_core_web_sm
CMD ["python", "app_flask/run_flask.py"]