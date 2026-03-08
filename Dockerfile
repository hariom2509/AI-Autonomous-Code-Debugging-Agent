FROM python:3.11-slim

# working directory
WORKDIR /app

# copy requirements
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy project files
COPY . .

# important for python imports
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# start fastapi server
CMD ["uvicorn", "api.debug_api:app", "--host", "0.0.0.0", "--port", "8000"]