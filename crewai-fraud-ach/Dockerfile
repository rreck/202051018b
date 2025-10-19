FROM python:3.11-slim

LABEL maintainer="RRECKTEK LLC"
LABEL description="CrewAI ACH Fraud Detection Agent"
LABEL version="1.0.0"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Create working directories
WORKDIR /work
RUN mkdir -p /work/input /work/output/logs /work/kb/short /work/kb/long /opt/app

# Copy application files
COPY app/ /opt/app/
COPY requirements.txt /opt/app/

# Install Python dependencies
RUN pip install --no-cache-dir -r /opt/app/requirements.txt

# Set Python path
ENV PYTHONPATH=/opt/app

# Environment variables with defaults
ENV INPUT_DIR=/work/input
ENV OUTPUT_DIR=/work/output
ENV KB_DIR=/work/kb
ENV PIDFILE=/var/run/fraud-ach-agent.pid
ENV METRICS_PORT=9090
ENV API_PORT=8080

# Expose ports
EXPOSE 8080 9090

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Default command - run in daemon mode
CMD ["python3", "/opt/app/main.py", "--daemon", "--log-level", "INFO"]
