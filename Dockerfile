# Use official Python image
FROM python:3.11.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install mysql-client
RUN apt update && apt install -y default-mysql-client

# Copy wait-for-it.sh into the container and make it executable
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the port that Django runs on
EXPOSE 8000


# Default command (can be overridden in docker-compose)
CMD ["/wait-for-it.sh", "mysql:3306", "--", "python", "manage.py", "migrate", "&&", "python", "manage.py", "grpcrunaioserver", "--dev", "0.0.0.0:8000"]
