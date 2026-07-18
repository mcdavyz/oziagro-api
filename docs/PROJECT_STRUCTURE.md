# Project Structure

## Overview

OziAgro follows a modular architecture that separates climate analytics, recommendation generation, API services, configuration, and testing into independent components.

This design improves maintainability, testing, and future extensibility as additional analytical engines are incorporated into the platform.

---

## Directory Structure

```text
oziagro-api/
│
├── app/
│   ├── api/
│   │   ├── server.py
│   │   └── routes.py
│   │
│   ├── climate/
│   │   ├── reader.py
│   │   ├── processor.py
│   │   ├── rainfall.py
│   │   ├── onset.py
│   │   ├── cessation.py
│   │   ├── season.py
│   │   └── dry_spell.py
│   │
│   ├── recommendation/
│   │   ├── advisor.py
│   │   ├── rules.py
│   │   └── report.py
│   │
│   ├── validators/
│   │
│   ├── exceptions/
│   │
│   ├── logger/
│   │
│   └── config/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── tests/
│
├── docs/
│
├── requirements.txt
└── README.md