.PHONY: help start stop restart test lint format clean install-dev check-deps docs security-scan all

# Default target
.DEFAULT_GOAL := help

# Colors for output
BLUE := \033[0;34m
GREEN := \033[0;32m
YELLOW := \033[0;33m
RED := \033[0;31m
NC := \033[0m # No Color

help: ## Show this help message
	@echo "$(BLUE)DevEx Sample Service - Available Commands$(NC)"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2}'
	@echo ""
	@echo "$(YELLOW)Quick Start:$(NC)"
	@echo "  1. make install-dev  # Install dependencies"
	@echo "  2. make start        # Start the service"
	@echo "  3. make test         # Run tests"
	@echo ""

install-dev: ## Install development dependencies
	@echo "$(BLUE)Installing development dependencies...$(NC)"
	pip install -r requirements.txt
	pip install -r requirements-dev.txt
	@echo "$(GREEN)✓ Dependencies installed$(NC)"

start: ## Start the service using Docker Compose
	@echo "$(BLUE)Starting the service...$(NC)"
	docker-compose up --build -d
	@echo "$(GREEN)✓ Service started at http://localhost:5000$(NC)"
	@echo "  • Health check: curl http://localhost:5000/"
	@echo "  • Products API: curl http://localhost:5000/products"

stop: ## Stop the service
	@echo "$(BLUE)Stopping the service...$(NC)"
	docker-compose down
	@echo "$(GREEN)✓ Service stopped$(NC)"

restart: stop start ## Restart the service

logs: ## View service logs
	docker-compose logs -f

test: ## Run unit tests with coverage
	@echo "$(BLUE)Running tests...$(NC)"
	pytest tests/ -v --cov=. --cov-report=term-missing --cov-report=html
	@echo "$(GREEN)✓ Tests completed$(NC)"
	@echo "  Coverage report: htmlcov/index.html"

lint: ## Run code linting (flake8, pylint, black check)
	@echo "$(BLUE)Running linters...$(NC)"
	@echo "→ Running flake8..."
	flake8 app.py tests/ scripts/
	@echo "→ Running pylint..."
	pylint app.py tests/*.py scripts/*.py --exit-zero
	@echo "→ Checking code formatting (black)..."
	black --check app.py tests/ scripts/
	@echo "$(GREEN)✓ Linting completed$(NC)"

format: ## Auto-format code with black
	@echo "$(BLUE)Formatting code...$(NC)"
	black app.py tests/ scripts/
	@echo "$(GREEN)✓ Code formatted$(NC)"

security-scan: ## Run security scans (bandit, safety)
	@echo "$(BLUE)Running security scans...$(NC)"
	@echo "→ Running bandit (code security)..."
	bandit -r app.py -f screen || true
	@echo "→ Running safety (dependency vulnerabilities)..."
	safety check --json || true
	@echo "$(GREEN)✓ Security scan completed$(NC)"

check-deps: ## Check for outdated dependencies and vulnerabilities
	@echo "$(BLUE)Checking dependencies...$(NC)"
	python scripts/check_dependencies.py
	@echo "$(GREEN)✓ Dependency check completed$(NC)"

docs: ## Generate documentation using AI
	@echo "$(BLUE)Generating documentation...$(NC)"
	python scripts/generate_docs.py
	@echo "$(GREEN)✓ Documentation generated$(NC)"

clean: ## Clean up containers, cache, and generated files
	@echo "$(BLUE)Cleaning up...$(NC)"
	docker-compose down -v 2>/dev/null || true
	rm -rf __pycache__ .pytest_cache htmlcov .coverage
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "$(GREEN)✓ Cleanup completed$(NC)"

all: clean install-dev lint test ## Run complete CI pipeline locally
	@echo "$(GREEN)✓ All checks passed!$(NC)"

validate: lint test security-scan check-deps ## Run all validation checks (like CI)
	@echo "$(GREEN)✓ Validation completed - Ready for PR!$(NC)"
