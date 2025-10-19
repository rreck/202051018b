#!/usr/bin/env bash
# -----------------------------------------------------------------------------
# Copyright (c) RRECKTEK LLC
# CrewAI ACH Fraud Detection Agent - Container Management Script
# Version: 1.0.0
# -----------------------------------------------------------------------------

set -euo pipefail

CONTAINER_NAME="crewai-fraud-ach-agent"
IMAGE_NAME="rrecktek/crewai-fraud-ach:1.0.0"
WORK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

API_PORT="${API_PORT:-8080}"
METRICS_PORT="${METRICS_PORT:-9090}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

usage() {
    cat <<EOF
CrewAI ACH Fraud Detection Agent - Container Management

Usage: $0 {COMMAND} [OPTIONS]

Commands:
  build                 Build the Docker image
  daemon                Start agent in daemon mode (background)
  watch                 Start agent in watch mode (foreground)
  batch                 Run one-shot batch processing
  generate              Generate synthetic ACH file
  stop                  Stop the running container
  restart               Restart the container
  status                Show container status
  health                Check agent health endpoint
  logs                  View container logs (add -f to follow)
  metrics               View Prometheus metrics
  exec                  Execute command in container
  clean                 Remove container and image
  trigger-batch         Trigger batch processing via API
  job FILE              Submit specific file for processing

Examples:
  $0 build
  $0 daemon
  $0 logs -f
  $0 generate --transactions 200 --fraud-ratio 0.10
  $0 job /work/input/transactions.ach
EOF
    exit 1
}

ensure_dirs() {
    mkdir -p "$WORK_DIR/input"
    mkdir -p "$WORK_DIR/output/logs"
    mkdir -p "$WORK_DIR/kb/short"
    mkdir -p "$WORK_DIR/kb/long"
}

build_image() {
    log_info "Building Docker image: $IMAGE_NAME"
    docker build -t "$IMAGE_NAME" "$WORK_DIR"
    log_info "Build complete"
}

start_daemon() {
    log_info "Starting $CONTAINER_NAME in daemon mode..."
    ensure_dirs

    docker run -d \
        --name "$CONTAINER_NAME" \
        --restart unless-stopped \
        -p "${API_PORT}:8080" \
        -p "${METRICS_PORT}:9090" \
        -v "$WORK_DIR/input:/work/input" \
        -v "$WORK_DIR/output:/work/output" \
        -v "$WORK_DIR/kb:/work/kb" \
        "$IMAGE_NAME" \
        python3 /opt/app/main.py --daemon --log-level INFO

    log_info "Container started. API: http://localhost:${API_PORT} | Metrics: http://localhost:${METRICS_PORT}/metrics"
}

start_watch() {
    log_info "Starting $CONTAINER_NAME in watch mode..."
    ensure_dirs

    docker run --rm -it \
        --name "$CONTAINER_NAME" \
        -p "${API_PORT}:8080" \
        -p "${METRICS_PORT}:9090" \
        -v "$WORK_DIR/input:/work/input" \
        -v "$WORK_DIR/output:/work/output" \
        -v "$WORK_DIR/kb:/work/kb" \
        "$IMAGE_NAME" \
        python3 /opt/app/main.py --watch --sleep 10 --log-level INFO
}

run_batch() {
    log_info "Running batch processing..."
    ensure_dirs

    docker run --rm \
        --name "$CONTAINER_NAME" \
        -v "$WORK_DIR/input:/work/input" \
        -v "$WORK_DIR/output:/work/output" \
        -v "$WORK_DIR/kb:/work/kb" \
        "$IMAGE_NAME" \
        python3 /opt/app/main.py --log-level INFO
}

generate_synthetic() {
    log_info "Generating synthetic ACH file..."
    ensure_dirs

    docker run --rm \
        --name "$CONTAINER_NAME-gen" \
        -v "$WORK_DIR/input:/work/input" \
        -v "$WORK_DIR/output:/work/output" \
        -v "$WORK_DIR/kb:/work/kb" \
        "$IMAGE_NAME" \
        python3 /opt/app/main.py --generate "$@"
}

stop_container() {
    if docker ps -q -f name="$CONTAINER_NAME" | grep -q .; then
        log_info "Stopping $CONTAINER_NAME..."
        docker stop "$CONTAINER_NAME"
        docker rm "$CONTAINER_NAME"
        log_info "Container stopped"
    else
        log_warn "Container not running"
    fi
}

restart_container() {
    stop_container
    start_daemon
}

show_status() {
    if docker ps -q -f name="$CONTAINER_NAME" | grep -q .; then
        log_info "Container is running:"
        docker ps -f name="$CONTAINER_NAME" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
    else
        log_warn "Container is not running"
    fi
}

check_health() {
    if ! docker ps -q -f name="$CONTAINER_NAME" | grep -q .; then
        log_error "Container not running"
        return 1
    fi

    log_info "Checking health endpoint..."
    curl -f "http://localhost:${API_PORT}/health" | jq . || log_error "Health check failed"
}

view_logs() {
    if ! docker ps -q -f name="$CONTAINER_NAME" | grep -q .; then
        log_error "Container not running"
        return 1
    fi

    docker logs "$@" "$CONTAINER_NAME"
}

view_metrics() {
    if ! docker ps -q -f name="$CONTAINER_NAME" | grep -q .; then
        log_error "Container not running"
        return 1
    fi

    log_info "Fetching Prometheus metrics..."
    curl -s "http://localhost:${METRICS_PORT}/metrics" | grep fraud_ach_
}

exec_in_container() {
    if ! docker ps -q -f name="$CONTAINER_NAME" | grep -q .; then
        log_error "Container not running"
        return 1
    fi

    docker exec -it "$CONTAINER_NAME" "$@"
}

clean_all() {
    log_warn "Removing container and image..."
    stop_container 2>/dev/null || true
    docker rmi "$IMAGE_NAME" 2>/dev/null || log_warn "Image not found"
    log_info "Cleanup complete"
}

trigger_batch_api() {
    if ! docker ps -q -f name="$CONTAINER_NAME" | grep -q .; then
        log_error "Container not running"
        return 1
    fi

    log_info "Triggering batch processing via API..."
    curl -X POST "http://localhost:${API_PORT}/batch" \
        -H "Content-Type: application/json" \
        -d '{"force": false}' | jq .
}

submit_job() {
    local file_path="$1"
    if ! docker ps -q -f name="$CONTAINER_NAME" | grep -q .; then
        log_error "Container not running"
        return 1
    fi

    log_info "Submitting job: $file_path"
    curl -X POST "http://localhost:${API_PORT}/job" \
        -H "Content-Type: application/json" \
        -d "{\"file_path\": \"$file_path\", \"force\": false}" | jq .
}

# Main command dispatcher
case "${1:-}" in
    build)
        build_image
        ;;
    daemon)
        start_daemon
        ;;
    watch)
        start_watch
        ;;
    batch)
        run_batch
        ;;
    generate)
        shift
        generate_synthetic "$@"
        ;;
    stop)
        stop_container
        ;;
    restart)
        restart_container
        ;;
    status)
        show_status
        ;;
    health)
        check_health
        ;;
    logs)
        shift
        view_logs "$@"
        ;;
    metrics)
        view_metrics
        ;;
    exec)
        shift
        exec_in_container "$@"
        ;;
    clean)
        clean_all
        ;;
    trigger-batch)
        trigger_batch_api
        ;;
    job)
        shift
        submit_job "$@"
        ;;
    *)
        usage
        ;;
esac
