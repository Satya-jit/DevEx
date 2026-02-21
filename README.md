# DevEx Sample Service 🚀

A showcase of modern **Developer Experience (DevEx)** practices around a simple Flask REST API. This project demonstrates how to build a frictionless developer workflow with automation, CI/CD, and AI-powered tooling.

[![CI Pipeline](https://github.com/Satya-jit/DevEx/actions/workflows/ci.yml/badge.svg)](https://github.com/Satya-jit/DevEx/actions)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

---

## ✨ Features

- 🐳 **One-command setup** with Docker
- 🧪 **Comprehensive testing** with pytest
- 🎨 **Code quality** automation (flake8, pylint, black)
- 🔒 **Security scanning** (bandit, safety, secret detection)
- 🤖 **AI-powered documentation** generation
- ⚡ **Fast CI/CD pipeline** with GitHub Actions
- 📊 **Dependency health monitoring**
- 📝 **Clean, maintainable codebase**

---

## 🎯 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+
- Make (optional, but recommended)

### Get Running in Under 5 Minutes

```bash
# 1. Clone the repository
git clone https://github.com/Satya-jit/DevEx.git
cd DevEx

# 2. Install development dependencies (optional, for local testing)
make install-dev

# 3. Start the service
make start

# 4. Test it out!
curl http://localhost:5000/
curl http://localhost:5000/products
```

That's it! 🎉 Your service is running at `http://localhost:5000`

---

## 🛠️ Developer Commands

We've made everything simple with a **Makefile** that provides a golden path:

```bash
make help              # Show all available commands
make start             # Start the service with Docker
make stop              # Stop the service
make restart           # Restart the service
make logs              # View service logs
make test              # Run unit tests with coverage
make lint              # Run all linters
make format            # Auto-format code
make security-scan     # Run security checks
make check-deps        # Check dependency health
make docs              # Generate AI-powered documentation
make clean             # Clean up everything
make validate          # Run all checks (like CI)
```

### Example Workflow

```bash
# Start development
make start

# Make changes to app.py
# ...

# Run tests
make test

# Check code quality
make lint

# Format code
make format

# Run full validation (like CI will)
make validate

# Generate documentation
make docs
```

---

## 📁 Project Structure

```
devex-sample/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD pipeline
├── docs/
│   ├── SDD.md                  # Software Design Document (AI-generated)
│   └── TestPlan.md             # Test Plan (AI-generated)
├── scripts/
│   ├── check_dependencies.py   # Dependency health checker
│   └── generate_docs.py        # AI documentation generator
├── tests/
│   └── test_app.py             # Unit tests
├── .flake8                     # Flake8 configuration
├── .gitignore                  # Git ignore rules
├── app.py                      # Main Flask application
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Container definition
├── Makefile                    # Developer commands
├── pyproject.toml              # Python project configuration
├── requirements.txt            # Production dependencies
├── requirements-dev.txt        # Development dependencies
└── README.md                   # This file
```

---

## 🔄 CI/CD Pipeline

Our GitHub Actions pipeline runs on every Pull Request:

### Pipeline Stages

1. **🎨 Code Linting**
   - flake8 for PEP 8 compliance
   - pylint for code quality
   - black for formatting checks

2. **🧪 Unit Tests**
   - pytest with coverage reporting
   - Minimum 80% coverage target
   - Parallel test execution

3. **🔒 Security Scanning**
   - Bandit for code security issues
   - Safety for dependency vulnerabilities
   - TruffleHog for secret detection

4. **📦 Dependency Checks**
   - Outdated package detection
   - Vulnerability scanning
   - Dependency conflict resolution

5. **🤖 AI Documentation**
   - Auto-generate SDD on PR
   - Update test plans
   - Mock mode fallback

6. **🐳 Docker Build** (on main branch)
   - Build and test Docker image
   - Health check validation

### CI Configuration

The CI pipeline is designed to:
- ✅ **Fail fast** with clear error messages
- 📊 **Provide rich feedback** with artifacts
- ⚡ **Run in parallel** for speed
- 🔐 **Handle secrets safely**

---

## 🤖 AI Integration

### AI-Powered Documentation

Generate technical documentation automatically:

```bash
# With OpenAI API key
export OPENAI_API_KEY=sk-...
make docs

# Without API key (mock mode)
make docs
```

The AI generator:
- Analyzes your codebase
- Generates Software Design Documents (SDD)
- Creates Test Plans
- Updates automatically in CI
- Falls back to mock mode gracefully

### Supported AI Features
- ✅ SDD generation from code
- ✅ Test plan generation
- ✅ Mock mode for no-API scenarios
- 🚧 PR summary generation (coming soon)

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests with coverage
make test

# Run specific test file
pytest tests/test_app.py -v

# Run with coverage report
pytest --cov --cov-report=html
```

### Test Coverage

We aim for **>80% coverage** across all modules:
- ✅ All endpoints tested
- ✅ Error scenarios covered
- ✅ External API calls mocked
- ✅ Edge cases validated

View coverage report: `open htmlcov/index.html`

---

## 🔒 Security

### Security Measures

1. **Automated Scanning**
   - Bandit: Static code analysis
   - Safety: Dependency vulnerabilities
   - TruffleHog: Secret detection

2. **Best Practices**
   - No hardcoded secrets
   - Environment variables for config
   - Timeout protection on external calls
   - Regular dependency updates

3. **CI Integration**
   - All PRs scanned automatically
   - Fails on high-severity issues
   - Security reports as artifacts

### Running Security Scans

```bash
make security-scan
```

---

## 📦 Dependency Management

### Checking Dependency Health

```bash
make check-deps
```

This command:
- 📋 Lists outdated packages
- 🔍 Scans for vulnerabilities
- ⚠️ Warns on dependency conflicts
- 📊 Generates a detailed report

### Updating Dependencies

```bash
# Check what's outdated
pip list --outdated

# Update specific package
pip install --upgrade <package>

# Update requirements
pip freeze > requirements.txt
```

---

## 🎨 Code Quality

### Linting & Formatting

We use a multi-layered approach:

1. **flake8** - PEP 8 compliance
2. **pylint** - Advanced code analysis
3. **black** - Opinionated formatting

```bash
# Run all linters
make lint

# Auto-format code
make format
```

### Configuration

- `.flake8` - Flake8 rules
- `pyproject.toml` - Pylint, Black, Pytest config

---

## 🐳 Docker

### Container Details

- **Base Image**: python:3.11-slim
- **Port**: 5000
- **Health Check**: Automated
- **Volume Mounts**: Hot reload for development

### Docker Commands

```bash
# Build and start
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop and clean
docker-compose down -v
```

---

## 🏗️ Design Decisions

### Why These Tools?

| Tool | Purpose | Reasoning |
|------|---------|-----------|
| **Flask** | Web framework | Lightweight, easy to test |
| **Docker** | Containerization | Consistent environments |
| **pytest** | Testing | Powerful and popular |
| **black** | Formatting | Removes style debates |
| **flake8** | Linting | Industry standard |
| **bandit** | Security | Python-specific |
| **safety** | Vulnerabilities | PyPI focused |
| **Make** | Task runner | Universal, simple |
| **GitHub Actions** | CI/CD | Native, powerful |

### DevEx Principles Applied

1. **⚡ Reduce Friction**
   - One-command operations
   - Sensible defaults
   - Fast feedback loops

2. **🔄 Automation First**
   - Automate repetitive tasks
   - Consistent environments
   - CI validates everything

3. **📚 Documentation**
   - AI-assisted updates
   - Always up-to-date
   - Self-documenting code

4. **🛡️ Safety Nets**
   - Tests catch regressions
   - Linters catch bugs early
   - Security scans prevent vulnerabilities

5. **🎯 Developer Productivity**
   - Clear error messages
   - Fast local iteration
   - Minimal setup time

---

## 🚀 Deployment

### Local Deployment

```bash
make start
```

### Production Considerations

For production deployment, consider:

1. **Environment Variables**
   ```bash
   export FLASK_ENV=production
   export OPENAI_API_KEY=sk-...
   ```

2. **Scaling**
   - Use gunicorn or uwsgi
   - Add load balancer
   - Implement health checks

3. **Monitoring**
   - Add logging
   - Implement metrics
   - Set up alerts

4. **Security**
   - Enable HTTPS
   - Rate limiting
   - Authentication

---

## 📈 Metrics & Monitoring

### Health Check

```bash
curl http://localhost:5000/
```

Expected response:
```json
{
  "service": "devex-sample",
  "status": "ok"
}
```

---

## 🤝 Contributing

### Development Workflow

1. **Fork & Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/devex-sample.git
   cd devex-sample
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

3. **Make Changes**
   ```bash
   # Edit files
   make format  # Format code
   make lint    # Check quality
   make test    # Run tests
   ```

4. **Commit & Push**
   ```bash
   git add .
   git commit -m "feat: add amazing feature"
   git push origin feature/amazing-feature
   ```

5. **Open Pull Request**
   - CI will run automatically
   - Fix any issues
   - Wait for review

### Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New features
- `fix:` Bug fixes
- `docs:` Documentation
- `style:` Formatting
- `refactor:` Code restructuring
- `test:` Adding tests
- `chore:` Maintenance

---

## 🐛 Troubleshooting

### Common Issues

**Issue: Port 5000 already in use**
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9

# Or use different port
docker-compose up --build -e PORT=5001
```

**Issue: Docker build fails**
```bash
# Clean Docker cache
docker system prune -af
docker-compose build --no-cache
```

**Issue: Tests fail**
```bash
# Ensure dependencies are installed
make install-dev

# Run tests with verbose output
pytest -vv
```

---

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions](https://docs.github.com/actions)

---

## 📝 License

This project is for educational purposes as part of a DevEx Engineer assessment.

---

## 🎓 What This Project Demonstrates

✅ **DevEx Mindset**
- Developer-first thinking
- Friction reduction
- Golden path design

✅ **Automation Thinking**
- CI/CD pipelines
- Automated quality checks
- Self-service tools

✅ **CI Design Quality**
- Fast feedback
- Clear error messages
- Parallel execution

✅ **Practical AI Usage**
- Documentation generation
- Mock mode fallback
- Developer productivity

✅ **Friction Reduction**
- One-command operations
- Sensible defaults
- Clear documentation

---

## 📞 Questions?

For questions or feedback about this project, please open an issue on GitHub.

---

**Built with ❤️ for DevEx Engineers**
