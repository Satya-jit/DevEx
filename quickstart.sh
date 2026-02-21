#!/bin/bash

# Quick Start Script for DevEx Sample Service
# This script helps you get started quickly

set -e

echo "=========================================="
echo "  DevEx Sample Service - Quick Start"
echo "=========================================="
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

# Check prerequisites
echo -e "${BLUE}Checking prerequisites...${NC}"

if ! command -v docker &> /dev/null; then
    echo -e "${YELLOW}⚠ Docker not found. Please install Docker first.${NC}"
    echo "   Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo -e "${YELLOW}⚠ Docker Compose not found. Please install Docker Compose first.${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Docker found${NC}"
echo -e "${GREEN}✓ Docker Compose found${NC}"
echo ""

# Check if Python is installed (for local testing)
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python found: ${PYTHON_VERSION}${NC}"
else
    echo -e "${YELLOW}⚠ Python not found (optional for local testing)${NC}"
fi

echo ""
echo -e "${BLUE}Starting the service...${NC}"

# Start Docker Compose
docker-compose up --build -d

echo ""
echo -e "${GREEN}✓ Service started successfully!${NC}"
echo ""
echo "=========================================="
echo "  Your service is now running!"
echo "=========================================="
echo ""
echo "Try these endpoints:"
echo "  • http://localhost:5000/"
echo "  • http://localhost:5000/products"
echo ""
echo "Quick commands:"
echo "  • make help          - Show all commands"
echo "  • make test          - Run tests"
echo "  • make logs          - View logs"
echo "  • make stop          - Stop service"
echo ""
echo -e "${BLUE}Testing the endpoints...${NC}"

# Wait a bit for service to start
sleep 3

# Test the endpoint
if curl -f http://localhost:5000/ &> /dev/null; then
    echo -e "${GREEN}✓ Service is responding!${NC}"
    echo ""
    echo "Response from /"
    curl -s http://localhost:5000/ | python3 -m json.tool || curl -s http://localhost:5000/
else
    echo -e "${YELLOW}⚠ Service might still be starting up...${NC}"
    echo "   Check logs with: make logs"
fi

echo ""
echo -e "${GREEN}Happy coding! 🚀${NC}"
