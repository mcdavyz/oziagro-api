# OziAgro

A modular research platform for climate-smart agriculture.

---

## Overview

OziAgro is an open, modular research platform that transforms climate, environmental, and agricultural data into practical decision-support tools for sustainable agriculture.

The platform is designed to support farmers, agricultural extension agents, researchers, and policymakers through evidence-based analytics and intelligent decision support.

The first product developed within the platform is the **OziAgro Decision Support System (DSS)**, which provides climate risk analysis and seasonal recommendations for rainfed agriculture using historical climate data.

Rather than being limited to a single application, OziAgro is designed as an extensible research platform where additional analytical engines can be integrated over time, including crop yield prediction, pest forecasting, irrigation scheduling, soil moisture assessment, and AI-assisted agricultural advisory services.

---

## Vision

To build an open, research-driven platform that enables data-informed agricultural decision-making for climate-smart agriculture across Africa and beyond.

---

## Objectives

The OziAgro Research Platform aims to:

- Transform climate and agricultural datasets into actionable knowledge.
- Support evidence-based decision making for sustainable agriculture.
- Provide practical decision-support tools for farmers and extension services.
- Enable reproducible agricultural research through modular analytical engines.
- Serve as a foundation for future AI-powered agricultural applications.

---
## Current Features

### Climate Processing Engine

The Climate Processing Engine is the core analytical component of OziAgro. It processes historical daily rainfall data and derives agroclimatic indicators for seasonal decision support.

Current capabilities include:

- Climate data validation
- Annual rainfall analysis
- Rainfall onset detection
- Rainfall cessation detection
- Growing season length estimation
- Dry spell analysis
- Seasonal climate risk classification
- Climate-based advisory generation

### Decision Support API

The OziAgro Decision Support System exposes its analytical capabilities through a RESTful API built with FastAPI.

Available endpoints include:

- Analyze a sample climate dataset
- Upload and analyze Excel climate datasets
- Return structured JSON results for downstream applications

### Software Quality

The current release includes:

- Modular architecture
- Automated unit testing
- API integration testing
- Structured error handling
- Input validation
- Logging support

## Technology Stack

| Category                | Technology 
|-------------------------|------------
| Programming Language    | Python 
| API Framework           | FastAPI 
| Data Processing         | Pandas, NumPy 
| Testing                 | Pytest 
| Development Environment | Visual Studio Code 
| Version Control         | Git & GitHub 

## Platform Architecture

```text
OziAgro Research Platform
│
├── Climate Engine (Current)
│   ├── Climate Data Validation
│   ├── Annual Rainfall Analysis
│   ├── Rainfall Onset Detection
│   ├── Rainfall Cessation Detection
│   ├── Growing Season Length
│   ├── Dry Spell Analysis
│   ├── Seasonal Risk Classification
│   └── Climate Advisory Generation
│
├── OziAgro Decision Support System
│   ├── Farmer Interface
│   ├── Extension Agent Interface
│   ├── Research Interface
│   └── Policy Interface
│
├── Crop Yield Engine (Planned)
├── Pest Risk Engine (Planned)
├── Irrigation Engine (Planned)
├── Soil Moisture Engine (Planned)
└── AI Advisory Engine (Planned)
```

## Project Structure

```text
oziagro-api/
│
├── app/
│   ├── api/
│   ├── climate/
│   ├── advisory/
│   ├── config/
│   ├── logger/
│   ├── exceptions/
│   └── validators/
│
├── tests/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/mcdavyz/oziagro-api.git

cd oziagro-api
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux/macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the API

Start the FastAPI development server.

```bash
uvicorn app.api.server:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```
## Interactive API Documentation

Once the server is running, FastAPI automatically provides interactive documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

## Running the Test Suite

Run the complete automated test suite using:

```bash
pytest
```

Run a specific test module:

```bash
pytest tests/test_api.py
```

or

```bash
pytest tests/test_advisor.py
```

## Example Workflow

1. Start the FastAPI server.
2. Open the interactive API documentation.
3. Upload a climate dataset in Excel format.
4. The Climate Processing Engine validates the dataset.
5. Agroclimatic indicators are calculated.
6. Seasonal recommendations are generated.
7. Results are returned as structured JSON for integration with external applications.

