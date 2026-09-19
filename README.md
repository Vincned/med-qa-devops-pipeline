# Automated FastAPI Integration Testing Pipeline

[![CI Pipeline](https://github.com/Vincend/med-qa-devops-pipeline/actions/workflows/ci-pipeline.yml/badge.svg)](https://github.com/Vincend/med-qa-devops-pipeline/actions)

Production-ready automated testing infrastructure for a **FastAPI** application using **Docker Compose**, **Pytest**, and **GitHub Actions**.

---

## System Architecture

This project implements an isolated testing environment using a containerized microservice architecture:

| Component | Service Name | Role & Functionality |
| :--- | :--- | :--- |
| **Backend API** | `app` | FastAPI application running on port `8000`. Exposes business logic and the `/health` readiness endpoint. |
| **Test Suite** | `test-runner` | Isolated Pytest environment that runs integration tests against the `app` service. |
| **Orchestrator** | `Docker Compose` | Manages internal DNS networking and enforces service readiness via `healthcheck`. |
app: FastAPI web application providing health checks (/health) and business logic endpoints.

test-runner: Dedicated container executing automated API integration tests via Pytest.

Healthcheck Orchestration: The test-runner waits for the app container to reach a service_healthy state before starting tests, preventing race conditions.

Tech Stack
Language: Python 3.11 🐍

Framework: FastAPI + Uvicorn ⚡

Testing: Pytest, Requests, Allure Framework 🧪

Containerization: Docker, Docker Compose 🐳

CI/CD: GitHub Actions ⚙️

- Quick Start (Local Execution)
All dependencies and runtime environments are fully containerized. To build the environment and run the test suite locally, execute a single command:

- Bash
docker compose up --build --exit-code-from test-runner
Once execution completes, raw test results will be automatically saved to the local ./allure-results directory via volume mapping.

- CI/CD Pipeline (GitHub Actions)
On every push or pull_request to the main branch:

Spawns an isolated ubuntu-latest virtual machine in the cloud.

Builds Docker images using efficient layer caching.

Runs integration tests via Docker Compose.

Uploads Allure test report artifacts to the Actions tab.