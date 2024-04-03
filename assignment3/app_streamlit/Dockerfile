FROM python:slim
WORKDIR /app
COPY . .
RUN pip install -r app_streamlit/requirements.txt
RUN python -m spacy download en_core_web_sm
CMD ["python", "-m", "streamlit", "run", "app_streamlit/app_streamlit.py"]