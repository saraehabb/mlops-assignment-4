# MLOps Assignment 4

This project demonstrates a simple Convolutional Neural Network (CNN) integrated with a GitHub Actions CI pipeline.

## Objective
To automate validation of a machine learning model using CI/CD practices.

## Project Structure
- model.py → Defines the CNN model
- train.py → Simulates a training step
- test_model.py → Tests the model (used in CI pipeline)
- requirements.txt → Dependencies

## CI Pipeline Features
- Python environment setup
- Dependency installation
- Model testing
- Artifact upload (README)

## How to Run
```bash
pip install -r requirements.txt
python test_model.py
```

