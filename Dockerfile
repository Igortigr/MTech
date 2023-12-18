FROM python:3.10

WORKDIR /docker_app

COPY . .

RUN pip install --upgrade pip && \
    pip install -r /docker_app/requirements.txt



CMD ["streamlit",  "run", "app.py"]