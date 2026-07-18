# OziAgro Decision Support System API

## Overview

The OziAgro Decision Support System exposes climate analytics through a RESTful API built with FastAPI.

The API enables client applications to submit climate datasets for analysis and receive structured agroclimatic indicators and seasonal recommendations.

Base URL 
http://127.0.0.1:8000


Interactive documentation is available through:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

---

## GET /

### Description

Returns a welcome message confirming that the API is running.

### Request

```http
GET /
```

### Success Response

Status Code

```
200 OK
```

Example

```json
{
    "message": "Welcome to OziAgro DSS!"
}
```

---

## GET /analyze/sample

### Description

Runs the complete climate analysis pipeline using the default sample dataset configured in the application.

This endpoint is useful for testing the API without uploading a dataset.

### Request

```http
GET /analyze/sample
```

### Success Response

Status Code

```
200 OK
```

Example

```json
[
  {
    "Onset": "Early",
    "Cessation": "Very Late",
    "SeasonLength": "Long",
    "DrySpellRisk": "Low",
    "OverallRisk": "Moderate",
    "SeasonSummary": "Rainfall onset is early, the growing season is long, and dry spell risk is low. Overall seasonal risk is moderate.",
    "Recommendations": [
      "Plant at the normal planting window.",
      "Long-duration rice varieties are suitable.",
      "Dry spell risk is low."
    ],
    "Reasons": [
      "Rainfall onset is Early.",
      "Long-duration rice varieties can complete their full growth cycle because the rainy season provides sufficient moisture for a longer period.",
      "Rainfall is expected to be sufficiently regular during the growing season, reducing the likelihood of prolonged moisture stress on the rice crop."
    ],
    "year": 1981
  }
]
```
---

## POST /analyze

### Description

Uploads an Excel climate dataset, processes the data, and returns climate indicators together with seasonal recommendations.

### Request

```http
POST /analyze
```

### Request Body

| Field | Type                  | Required | Description            |
|-------|-----------------------|----------|------------------------|
| file  | Excel (.xlsx or .xls) | Yes      | Daily rainfall dataset |

### Success Response

Status Code

```
200 OK
```

Example

```json
{
  "status": "success",
  "records": 45,
  "results": [
    {
      "Onset": "Early",
      "Cessation": "Very Late",
      "SeasonLength": "Long",
      "DrySpellRisk": "Low",
      "OverallRisk": "Moderate",
      "SeasonSummary": "Rainfall onset is early, the growing season is long, and dry spell risk is low. Overall seasonal risk is moderate.",
      "Recommendations": [
        "Plant at the normal planting window.",
        "Long-duration rice varieties are suitable.",
        "Dry spell risk is low."
      ],
      "Reasons": [
        "Rainfall onset is Early.",
        "Long-duration rice varieties can complete their full growth cycle because the rainy season provides sufficient moisture for a longer period.",
        "Rainfall is expected to be sufficiently regular during the growing season, reducing the likelihood of prolonged moisture stress on the rice crop."
      ],
      "year": 1981
    }
  ]
}
```

---

## Error Responses

### Unsupported File Type

Status Code

```
200 OK
```

Example

```json
{
    "error": "Only Excel (.xlsx or .xls) files are supported."
}
```

---

### Missing Upload

Status Code

```
422 Unprocessable Entity
```

Returned automatically by FastAPI when the required file parameter is omitted.

## Climate Processing Pipeline

The uploaded dataset passes through the following processing stages:

1. Dataset validation
2. Annual rainfall calculation
3. Rainfall onset detection
4. Rainfall cessation detection
5. Growing season length estimation
6. Dry spell analysis
7. Seasonal risk classification
8. Climate recommendation generation
9. JSON response construction

## Response Format

Successful requests return JSON with the following structure.

```json
{
    "status": "success",
    "records": 45,
    "results": [
        ...
    ]
}
```
