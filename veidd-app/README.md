# VEIDD Web Application

VEIDD (Visual recognition, Evaluation, Intactness, Difficulty, Decisioning) is a web application for AI-based decision support in e-waste processing.

## Project Structure

```
veidd-app/
├── backend/           # Backend API server
│   ├── src/          # Source code
│   ├── tests/        # Test files
│   ├── migrations/   # Database migrations
│   └── config/       # Configuration files
├── frontend/         # Frontend React application
│   ├── src/          # Source code
│   ├── public/       # Static files
│   └── tests/        # Test files
├── docs/             # Documentation
├── scripts/          # Utility scripts
└── deployment/       # Deployment configurations
```

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python (v3.9 or higher)
- PostgreSQL (v14 or higher)
- Docker (optional)

### Development Setup

1. Clone the repository
2. Set up the backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```bash
   cd frontend
   npm install
   ```

4. Start the development servers:
   - Backend: `cd backend && python run.py`
   - Frontend: `cd frontend && npm start`

## Development Workflow

1. Create a new branch for your feature
2. Make your changes
3. Run tests
4. Create a pull request

## Contributing

Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 