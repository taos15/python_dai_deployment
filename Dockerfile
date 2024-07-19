FROM python:3.11.8-slim-bullseye as base

WORKDIR /app

COPY requirements.txt app.py ./

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

# # Health check
# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health 

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

