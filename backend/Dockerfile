# 1. Start from an official, small Python image, with a pinned version
FROM python:3.12-slim
# 2. Work inside /app in the image
WORKDIR /app
# 3. Install dependencies first: this layer stays cached while only the code changes
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# 4. Copy the application code
COPY . .
# 5. Do not run as root
RUN useradd --create-home appuser
USER appuser
# 6. Document the port and define the start command
EXPOSE 5000
CMD ["python", "app.py"]
