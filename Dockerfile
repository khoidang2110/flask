# Dockerfile
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Cài đặt dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ source code
COPY . .

# Expose port (phải giống với port bạn dùng trong app.run)
EXPOSE 6001

# Command chạy app
CMD ["python", "app.py"]
