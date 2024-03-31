FROM python:slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN curl http://127.0.0.1:8000?pretty=true
CMD ["python", "run_flask.py", "app_streamlit.py"]