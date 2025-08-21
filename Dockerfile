FROM python:3.12-slim

WORKDIR /app

# Cài dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source
COPY . .

# Expose port
EXPOSE 5001

# Chạy Flask trực tiếp qua module entrypoint
CMD ["python", "-m", "src.infrastructure.web.app"]
