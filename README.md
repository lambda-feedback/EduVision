# EduVision Evaluation Function

An AWS Lambda evaluation function for the [Lambda Feedback](https://github.com/lambda-feedback) platform that grades student responses by querying the EduVision API. Built on the [BaseEvaluationFunctionLayer](https://github.com/lambda-feedback/BaseEvalutionFunctionLayer).

## Table of Contents
- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Usage](#usage)
  - [Getting Started](#getting-started)
  - [API Endpoints](#api-endpoints)
  - [Request Format](#request-format)
- [How it works](#how-it-works)
  - [Docker & AWS Lambda](#docker--aws-lambda)
  - [GitHub Actions](#github-actions)
- [Pre-requisites](#pre-requisites)

## Overview

This function evaluates student responses by making API calls to the EduVision server. It compares the API's response against an expected answer to determine correctness, supporting two grading modes:

- **Resistance** — checks the global resistance of a circuit (float comparison)
- **Resistors** — checks the list of recognised resistors and their resistance values (list comparison)

## Repository Structure

```
app/
    __init__.py
    evaluation.py       # Main evaluation function — called on "eval" command
    preview.py          # Preview function — called on "preview" command
    utility.py          # Shared helper (initialize_test_connection)
    evaluation_tests.py # Unit tests for the evaluation function
    preview_tests.py    # Unit tests for the preview function
    requirements.txt    # Python dependencies
    Dockerfile          # Container image for AWS Lambda deployment
    docs/
        user.md         # End-user documentation (served via "docs" command)
        dev.md          # Developer documentation

.github/
    workflows/
        test-and-deploy.yml  # CI/CD pipeline

config.json  # Evaluation function name ("eduVision")
.gitignore
```

## Usage

### Getting Started

1. Clone this repository.
2. Set the `API_CONNECTION` environment variable to the EduVision API server URL (e.g. in a `.env` file):
   ```
   API_CONNECTION=http://<host>:<port>
   ```
3. Install dependencies:
   ```bash
   pip install -r app/requirements.txt
   ```
4. Run the tests:
   ```bash
   cd app && pytest -v evaluation_tests.py preview_tests.py
   ```
5. Push to `main` to trigger the CI/CD pipeline, which will build, test, and deploy the function to AWS Lambda.

### API Endpoints

The function proxies requests to the EduVision API. The endpoint is controlled by the `api_endpoint` param:

| Endpoint | Description | Expected answer type |
| --- | --- | --- |
| `resistance/` (default) | Global circuit resistance | `float` |
| `resistors/` | List of recognised resistors | `list[dict]` |

The student's 6-character connection ID is appended to the endpoint:
```
{API_CONNECTION}/{api_endpoint}{response}
```

### Request Format

Requests follow the Lambda Feedback schema:

```json
{
  "headers": { "command": "eval" },
  "body": {
    "response": "999999",
    "answer": 1000.0,
    "params": {
      "api_endpoint": "resistance/"
    }
  }
}
```

**Resistance example** — `answer` is a `float`:
```json
{
  "body": {
    "response": "999999",
    "answer": 1000.0,
    "params": { "api_endpoint": "resistance/" }
  }
}
```

**Resistors example** — `answer` is a list of dicts:
```json
{
  "body": {
    "response": "999999",
    "answer": [
      { "resistance": 1000.0 },
      { "resistance": 1000.0 }
    ],
    "params": { "api_endpoint": "resistors/" }
  }
}
```

**Response** — the function returns:
```json
{ "is_correct": true, "error": 0 }
```

`error` codes: `0` = success, `1` = invalid connection ID length, `2`–`5` = answer mismatch variants, `6` = API connection error.

## How it works

### Docker & AWS Lambda

The function runs as a Docker container on AWS Lambda. On every push to `main`, GitHub Actions builds the image, pushes it to a shared ECR repository, then calls the Lambda Feedback backend to provision the necessary infrastructure.

### GitHub Actions

The `.github/workflows/test-and-deploy.yml` pipeline:

1. **Lint** — runs `flake8` for syntax errors.
2. **Test** — runs `pytest` against `evaluation_tests.py` and `preview_tests.py`.
3. **Deploy (staging)** — builds and pushes the Docker image, then registers the function with the staging environment.
4. **Deploy (production)** — same as staging, but targets the production environment.

Tests also run on every `healthcheck` command sent to the deployed function.

## Pre-requisites

- Python 3.8+
- Docker (for local image builds)
- `git` CLI or GitHub Desktop
- Access to the EduVision API server

## Contact

For issues with the Lambda Feedback platform, see the [lambda-feedback organisation](https://github.com/lambda-feedback) on GitHub.