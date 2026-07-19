# OziAgro Rainfall Analytics Engine

A modular rainfall analytics engine powering the OziAgro Research Platform.

---

## Overview

The OziAgro Rainfall Analytics Engine is the first analytical engine developed within the OziAgro Research Platform, an open, modular ecosystem for climate-smart agricultural research and decision support.

The engine processes historical daily rainfall datasets and transforms them into reproducible agroclimatic indicators that can support agricultural research, extension services, and future intelligent decision-support systems.

Rather than providing only qualitative recommendations, the engine preserves the underlying scientific measurements, enabling researchers to report actual climatic values while also benefiting from automatically generated seasonal classifications and risk assessments.

The engine is exposed through a REST API built with FastAPI, making it suitable for integration into future applications including the OziAgro Decision Support System (DSS), mobile applications, dashboards, and AI advisory services.

---

## Objectives

The OziAgro Rainfall Analytics Engine aims to:

- Transform historical daily rainfall observations into scientifically meaningful agroclimatic indicators.
- Automate rainfall data validation and quality checking before analysis.
- Detect rainfall onset and cessation dates using reproducible algorithms.
- Quantify seasonal dry spell characteristics that influence crop production.
- Generate structured rainfall analytics that can support agricultural research, extension services, and decision-support applications.


---

### Current Capabilities
The Rainfall Analytics Engine currently performs:

### Data Validation
- Dataset integrity checks
- Missing value validation
- Required column validation
- Data consistency verification

### Rainfall Analytics
- Annual rainfall totals
- Rainfall onset detection
- Rainfall cessation detection
- Growing season length estimation
- Longest dry spell analysis

### Seasonal Classification
The engine automatically classifies:
- Rainfall onset
- Rainfall cessation
- Growing season length
- Dry spell severity
- Overall seasonal climate risk

### Research Outputs
Unlike many advisory systems, OziAgro returns both:
(1) Raw analytical values for example:
- Annual rainfall (mm)
- Onset day of year
- Cessation day of year
- Season length
- Longest dry spell
(2) Decision-support interpretations for example:
- Early onset
- Long growing season
- Moderate risk
- High dry spell risk

This makes the engine suitable for academic research, climate reports, agricultural extension,downstream AI systems.

### API Features
The engine exposes a RESTful API. Current endpoints include:
| Endpoint              | Description                                   
|-----------------------|----------------------------------------------
| GET /                 | API information                              
| GET /rainfall/sample  | Analyze bundled sample rainfall dataset      
| POST /rainfall/analyze| Upload an Excel rainfall dataset for analysis

Results are returned as structured JSON suitable for integration with external software.

### Example Output
The API returns both measured values and interpreted results.

```text
{
  "Year": 2024,
  "AnnualRainfallMM": 1682.4,
  "OnsetDOY": 118,
  "CessationDOY": 286,
  "SeasonLengthDays": 168,
  "LongestDrySpellDays": 14,

  "OnsetCategory": "Late",
  "CessationCategory": "Normal",
  "SeasonLengthCategory": "Moderate",
  "DrySpellRisk": "Moderate",
  "OverallRisk": "High"
}
```
This design allows researchers to cite the original climatic measurements while still benefiting from automated decision-support outputs.

### Software Architecture

```text
OziAgro Research Platform
│
├── OziAgro Rainfall Analytics Engine (Current)
│   │
│   ├── Data Validation
│   ├── Annual Rainfall Analysis
│   ├── Rainfall Onset Detection
│   ├── Rainfall Cessation Detection
│   ├── Growing Season Analysis
│   ├── Dry Spell Analysis
│   ├── Seasonal Classification
│   ├── Risk Assessment
│   └── REST API
│
├── OziAgro Decision Support System
│   │
│   ├── Recommendation Engine
│   ├── Farmer Advisory
│   ├── Extension Support
│   ├── Research Analytics
│   └── Policy Support
│
├── Crop Yield Engine (Planned)
├── Pest Risk Engine (Planned)
├── Irrigation Engine (Planned)
├── Soil Moisture Engine (Planned)
└── AI Advisory Engine (Planned)
```

## Technology Stack

| Category                | Technology 
|-------------------------|------------
| Programming Language    | Python 3.12
| API Framework           | FastAPI 
| Data Processing         | Pandas, NumPy 
| Testing                 | Pytest 
| Development Environment | Visual Studio Code 
| Version Control         | Git & GitHub 
| Server                  | Uvicorn


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

## Documentation

Project documentation is available in the `docs/` directory.

- API Reference (`docs/API.md`)
- Developer Guide *(coming soon)*
- Deployment Guide *(coming soon)*

## Example Workflow

1. Start the FastAPI server.
2. Open the interactive API documentation.
3. Upload a climate dataset in Excel format.
4. The rainfall  processing Engine validates the dataset.
5. Agroclimatic indicators are calculated.
6. Seasonal recommendations are generated.
7. Results are returned as structured JSON for integration with external applications.

## Development Roadmap

### Completed

- Rainfall validation
- Annual rainfall computation
- Rainfall onset detection
- Rainfall cessation detection
- Growing season estimation
- Dry spell analysis
- Seasonal classification
- Climate risk assessment
- FastAPI REST API
- Automated testing
- Structured error handling

### Next Milestones
- PDF report generation
- CSV and Excel export
- Visualization module
- Research report templates
- AI advisory integration
- Multi-engine orchestration
- OziAgro Decision Support System

### Planned

- Crop Yield Engine
- Pest Risk Engine
- Irrigation Engine
- Soil Moisture Engine
- AI-powered advisory system
- Mobile application
- Web dashboard
- Research analytics portal

## License

Copyright © 2026 Okorie David Amah.

OziAgro Rainfall Analytics Engine is currently distributed under an **All Rights Reserved** license.

The software is provided for academic review and research purposes. Any reproduction, modification, redistribution, or commercial use requires prior written permission from the copyright holder.

## Author

**Amah, Okorie David**

M.Sc. Candidate in Agricultural Extension 

University of Nigeria, Nsukka

Research interests include AI applications in agriculture, decision support systems climate-smart agriculture, agricultural extension, and environmental sustainability.

## Citation

If you use **OziAgro Rainfall Analytics Engine** in academic research, please cite the software as follows:

**APA 7th Edition**


> Amah, O. D. (2026). *OziAgro Rainfall Analytics Engine* (Version 1.0.0) [Computer software]. GitHub. https://github.com/mcdavyz/oziagro-api



**BibTeX**

```bibtex
@software{amah2026oziagro,
  author  = {Amah, Okorie David},
  title   = {OziAgro Rainfall Analytics Engine},
  year    = {2026},
  version = {1.0.0},
  url     = {https://github.com/mcdavyz/oziagro-api},
  publisher = {GitHub}
}
```

## Acknowledgements

OziAgro is being developed as a research-driven initiative to advance climate-smart agriculture through open, modular, and reproducible analytical tools.

The project integrates climate analytics, decision support, and software engineering principles to support sustainable agricultural development.