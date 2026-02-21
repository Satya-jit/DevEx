#!/usr/bin/env python3
"""
AI-Powered Documentation Generator
Generates technical documentation (SDD) from codebase using AI.
Falls back to mock mode if API key is not available.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path
from typing import Optional


class Colors:
    """ANSI color codes."""
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


def read_codebase() -> dict:
    """Read relevant code files from the repository."""
    codebase = {}

    files_to_read = [
        'app.py',
        'tests/test_app.py',
        'requirements.txt',
        'Dockerfile',
        'docker-compose.yml'
    ]

    for file_path in files_to_read:
        try:
            with open(file_path, 'r') as f:
                codebase[file_path] = f.read()
        except FileNotFoundError:
            print(f"{Colors.YELLOW}⚠ File not found: {file_path}{Colors.END}")
        except Exception as e:
            print(f"{Colors.RED}✗ Error reading {file_path}: {e}{Colors.END}")

    return codebase


def generate_with_openai(codebase: dict, api_key: str) -> Optional[str]:
    """Generate documentation using OpenAI API."""
    try:
        import openai

        openai.api_key = api_key

        # Prepare prompt
        code_context = "\n\n".join([
            f"=== {filename} ===\n{content}"
            for filename, content in codebase.items()
        ])

        prompt = f"""You are a technical documentation expert. Based on the following codebase,
generate a comprehensive Software Design Document (SDD) in Markdown format.

Include the following sections:
1. Overview
2. Architecture
3. API Endpoints
4. Data Flow
5. Technology Stack
6. Deployment
7. Testing Strategy
8. Security Considerations

Codebase:
{code_context}

Generate a professional SDD.md document:"""

        print(f"{Colors.BLUE}→ Calling OpenAI API...{Colors.END}")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a technical documentation expert."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )

        return response.choices[0].message.content

    except ImportError:
        print(f"{Colors.YELLOW}⚠ OpenAI library not installed{Colors.END}")
        return None
    except Exception as e:
        print(f"{Colors.RED}✗ OpenAI API error: {e}{Colors.END}")
        return None


def generate_mock_documentation(codebase: dict) -> str:
    """Generate mock documentation when API is not available."""
    print(f"{Colors.YELLOW}→ Running in MOCK mode (no API key)...{Colors.END}")

    endpoints = []
    if 'app.py' in codebase:
        # Simple parsing to find endpoints
        for line in codebase['app.py'].split('\n'):
            if '@app.get' in line or '@app.post' in line:
                endpoints.append(line.strip())

    tech_stack = []
    if 'requirements.txt' in codebase:
        tech_stack = [line.strip() for line in codebase['requirements.txt'].split('\n') if line.strip()]

    doc = f"""# Software Design Document (SDD)

**Project:** DevEx Sample Service
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Version:** 1.0
**Status:** Auto-generated (Mock Mode)

---

## 1. Overview

The DevEx Sample Service is a RESTful API built with Flask that provides a simple service status endpoint and a products API integration. This service demonstrates modern DevEx practices including containerization, automated testing, and CI/CD pipelines.

### Purpose
- Provide service health monitoring
- Integrate with external product APIs
- Demonstrate DevEx best practices

### Key Features
- Health check endpoint
- External API integration
- Docker containerization
- Comprehensive testing
- CI/CD automation

---

## 2. Architecture

### System Architecture
```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  Flask Application  │
│  (Docker Container) │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  External APIs      │
│  (dummyjson.com)    │
└─────────────────────┘
```

### Components
1. **Flask Web Server**: Handles HTTP requests
2. **Docker Container**: Provides isolated runtime environment
3. **External API Client**: Integrates with third-party services

---

## 3. API Endpoints

### Detected Endpoints:
"""

    # Add endpoints
    if endpoints:
        endpoint_list = '\n'.join(f'- `{endpoint}`' for endpoint in endpoints)
    else:
        endpoint_list = '- / (Home endpoint)\n- /products (Products endpoint)'

    doc += endpoint_list + """

### Endpoint Details

#### GET /
**Description:** Health check endpoint
**Response:**
```json
{{
  "service": "devex-sample",
  "status": "ok"
}}
```

#### GET /products
**Description:** Fetch products from external API
**External API:** https://dummyjson.com/products
**Timeout:** 10 seconds
**Response:** Proxied JSON from external API

---

## 4. Data Flow

1. **Client Request** → HTTP request to Flask server
2. **Route Handler** → Process request and validate
3. **External API Call** (if needed) → Fetch data from dummyjson.com
4. **Response Processing** → Format and return JSON
5. **Client Response** → Return data to client

---

## 5. Technology Stack

### Core Technologies
"""

    # Add tech stack
    if tech_stack:
        tech_list = '\n'.join(f'- {tech}' for tech in tech_stack[:10])
    else:
        tech_list = '- Flask 3.0.0\n- Requests 2.31.0'

    doc += tech_list + """

### Development Tools
- pytest (Unit Testing)
- flake8, pylint, black (Code Quality)
- Docker & Docker Compose (Containerization)
- GitHub Actions (CI/CD)

### Infrastructure
- Docker for containerization
- Python 3.11 runtime
- Port 5000 for HTTP traffic

---

## 6. Deployment

### Docker Deployment
```bash
# Build and run
docker-compose up --build

# Access service
curl http://localhost:5000/
```

### Environment Variables
- `FLASK_ENV`: Set to 'development' or 'production'
- `OPENAI_API_KEY`: (Optional) For AI documentation generation

### Health Checks
- HTTP health check on `/` endpoint
- Interval: 30s
- Timeout: 3s
- Retries: 3

---

## 7. Testing Strategy

### Unit Tests
- Test coverage for all endpoints
- Mock external API calls
- Validate response formats
- Error handling scenarios

### Test Execution
```bash
make test
```

### Coverage Goals
- Minimum 80% code coverage
- All critical paths tested
- Edge cases covered

---

## 8. Security Considerations

### Implemented Security Measures
1. **Dependency Scanning**: Automated vulnerability checks
2. **Secret Scanning**: TruffleHog integration
3. **Code Security**: Bandit static analysis
4. **Timeout Protection**: 10s timeout on external API calls
5. **Error Handling**: Proper exception management

### Best Practices
- No hardcoded secrets
- Environment variable for sensitive data
- Regular dependency updates
- Automated security scans in CI

---

## 9. DevEx Features

### Developer Workflow
1. **Setup**: `make install-dev`
2. **Start**: `make start`
3. **Test**: `make test`
4. **Lint**: `make lint`
5. **Clean**: `make clean`

### CI/CD Pipeline
- Automated testing on PR
- Code quality checks
- Security scanning
- Docker image building
- Documentation generation

### Time to Productivity
- **Target**: < 5 minutes from clone to running service
- **One-command operations** for all common tasks
- **Automated environment setup**

---

## 10. Future Enhancements

- Add authentication/authorization
- Implement rate limiting
- Add monitoring and logging
- Database integration
- More comprehensive error handling
- API versioning

---

*This document was auto-generated by the DevEx automation pipeline.*
"""

    return doc


def save_documentation(content: str, filename: str = "docs/SDD.md"):
    """Save generated documentation to file."""
    try:
        # Ensure docs directory exists
        Path("docs").mkdir(exist_ok=True)

        with open(filename, 'w') as f:
            f.write(content)

        print(f"{Colors.GREEN}✓ Documentation saved to: {filename}{Colors.END}")
        return True

    except Exception as e:
        print(f"{Colors.RED}✗ Error saving documentation: {e}{Colors.END}")
        return False


def main():
    """Main execution function."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}AI Documentation Generator{Colors.END}\n")

    # Read codebase
    print(f"{Colors.BLUE}→ Reading codebase...{Colors.END}")
    codebase = read_codebase()
    print(f"{Colors.GREEN}✓ Read {len(codebase)} files{Colors.END}\n")

    # Check for API key
    api_key = os.getenv('OPENAI_API_KEY')

    if api_key:
        print(f"{Colors.GREEN}✓ API key found, using OpenAI{Colors.END}")
        documentation = generate_with_openai(codebase, api_key)

        if not documentation:
            print(f"{Colors.YELLOW}⚠ Falling back to mock mode{Colors.END}")
            documentation = generate_mock_documentation(codebase)
    else:
        print(f"{Colors.YELLOW}⚠ No API key found (OPENAI_API_KEY){Colors.END}")
        documentation = generate_mock_documentation(codebase)

    # Save documentation
    print()
    if save_documentation(documentation):
        print(f"\n{Colors.GREEN}✓ Documentation generation completed!{Colors.END}")

        # Also generate a test plan
        print(f"\n{Colors.BLUE}→ Generating test plan...{Colors.END}")
        test_plan = generate_test_plan(codebase)
        save_documentation(test_plan, "docs/TestPlan.md")

        sys.exit(0)
    else:
        sys.exit(1)


def generate_test_plan(codebase: dict) -> str:
    """Generate a test plan document."""
    return f"""# Test Plan

**Project:** DevEx Sample Service
**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Version:** 1.0

---

## 1. Test Objectives

- Verify all API endpoints function correctly
- Ensure error handling works as expected
- Validate integration with external APIs
- Confirm Docker deployment works
- Check CI/CD pipeline functionality

---

## 2. Test Scope

### In Scope
- Unit tests for all endpoints
- Integration tests for external API calls
- Docker container testing
- CI/CD pipeline validation
- Code quality checks

### Out of Scope
- Performance/load testing
- Security penetration testing
- User acceptance testing

---

## 3. Test Cases

### TC-001: Home Endpoint
- **Description**: Test GET / endpoint
- **Expected**: Returns service status JSON
- **Status**: ✓ Implemented

### TC-002: Products Endpoint
- **Description**: Test GET /products endpoint
- **Expected**: Returns products from external API
- **Status**: ✓ Implemented

### TC-003: Error Handling
- **Description**: Test API timeout and error scenarios
- **Expected**: Proper error responses
- **Status**: ✓ Implemented

### TC-004: Docker Container
- **Description**: Build and run Docker container
- **Expected**: Service runs on port 5000
- **Status**: ✓ Implemented

---

## 4. Test Execution

### Running Tests
```bash
make test
```

### Coverage Report
```bash
pytest --cov --cov-report=html
```

---

## 5. Success Criteria

- All unit tests pass
- Code coverage > 80%
- No linting errors
- No security vulnerabilities
- Docker container builds successfully
- CI pipeline passes all checks

---

*Auto-generated test plan*
"""


if __name__ == "__main__":
    main()
