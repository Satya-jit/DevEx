# DevEx Sample Service

A Flask REST API demonstrating modern Developer Experience (DevEx) practices with automated testing, CI/CD, and code quality checks.

[![CI Pipeline](https://github.com/Satya-jit/DevEx/actions/workflows/ci.yml/badge.svg)](https://github.com/Satya-jit/DevEx/actions)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Features

- 🐳 Docker containerization for easy deployment
- 🧪 Comprehensive test coverage with pytest
- 🎨 Automated code formatting and linting
- 🔒 Security scanning (Bandit, Safety, TruffleHog)
- ⚡ GitHub Actions CI/CD pipeline
- 📊 Automated dependency health checks

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local development)

### Running with Docker

```bash
# Start the service
docker-compose up

# Access the API
curl http://localhost:5000/
curl http://localhost:5000/products
```

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run the application
python app.py

# Run tests
pytest tests/ -v --cov=.

# Run linting
flake8 .
pylint app.py tests/
black --check .
```

## API Endpoints

### `GET /`
Health check endpoint.

**Response:**
```json
{
  "service": "devex-sample",
  "status": "ok"
}
```

### `GET /products`
Fetches products from an external API.

**Response:**
```json
{
  "products": [...]
}
```

## Development Workflow

### Using Makefile Commands

```bash
make install        # Install production dependencies
make install-dev    # Install development dependencies
make test           # Run tests with coverage
make lint           # Run all linters
make format         # Format code with black
make security       # Run security scans
make start          # Start with docker-compose
make stop           # Stop docker-compose
make clean          # Clean up artifacts
```

### CI/CD Pipeline

The GitHub Actions pipeline automatically runs on every push:

1. **Lint** - Code quality checks (flake8, pylint, black)
2. **Test** - Unit tests with coverage report
3. **Security** - Vulnerability scanning (bandit, safety)
4. **Secret Scan** - Detect leaked secrets (TruffleHog)
5. **Dependencies** - Check for outdated packages
6. **Documentation** - Generate technical docs

## Project Structure

```
DevEx/
├── app.py                      # Flask application
├── tests/
│   └── test_app.py            # Unit tests
├── scripts/
│   ├── check_dependencies.py  # Dependency health checker
│   └── generate_docs.py       # Documentation generator
├── .github/workflows/
│   └── ci.yml                 # CI/CD pipeline
├── Dockerfile                  # Container image
├── docker-compose.yml          # Docker orchestration
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
└── Makefile                    # Developer commands
```

## Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=. --cov-report=html

# Run specific test
pytest tests/test_app.py::test_home_endpoint -v
```

## Code Quality

The project enforces code quality through:

- **Flake8**: PEP 8 style guide compliance
- **Pylint**: Static code analysis
- **Black**: Automatic code formatting
- **Bandit**: Security issue detection
- **Safety**: Known vulnerability checks

## License

MIT License
