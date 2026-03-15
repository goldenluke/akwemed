<div align="center">

# AKWEMED
### AI for Intercultural Healthcare and Complex Systems Monitoring

An experimental clinical artificial intelligence system designed to support healthcare professionals working in Indigenous territories.

AKWEMED integrates **natural language processing**, **retrieval-augmented clinical reasoning**, and **complex systems analysis** to assist communication and clinical decision support in intercultural healthcare environments.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Django](https://img.shields.io/badge/Django-REST-green)
![FastAPI](https://img.shields.io/badge/FastAPI-AI%20Engine-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Tailwind](https://img.shields.io/badge/TailwindCSS-UI-38BDF8)
![License](https://img.shields.io/badge/license-MIT-black)

</div>

---

# Overview

**AKWEMED** is an experimental research project exploring how artificial intelligence can support **clinical communication and decision support in Indigenous healthcare contexts**.

Healthcare professionals working in Indigenous territories often encounter:

- linguistic barriers  
- culturally specific symptom descriptions  
- limited digital infrastructure  
- lack of clinical decision-support systems adapted to local realities  

AKWEMED investigates how modern AI techniques can help address these challenges.

The system combines:

- Indigenous language interpretation  
- retrieval-augmented clinical reasoning (RAG)  
- semantic embeddings  
- local AI inference  
- complex systems monitoring  

The project is currently focused on the **Xerente (Akwẽ) language**.

---

# Example Interaction

Patient input (Xerente language)

```
ĩsĩ kâ peito
```

System interpretation

```
dor no peito
```

Possible clinical reasoning

```
Possible protocol → Acute Coronary Syndrome
```

The system interprets linguistic expressions and connects them to clinical knowledge bases.

---

# System Architecture

AKWEMED follows a modular architecture separating the interface, clinical reasoning engine and structural monitoring system.

```
React Frontend (Clinical Chat Interface)
        ↓
Django REST API
        ↓
FastAPI AI Inference Engine
        ↓
Xerente Language Interpreter
        ↓
Clinical RAG Engine (semantic embeddings)
        ↓
MetastableX Structural Analysis Engine
        ↓
Clinical Protocol Knowledge Base
```

This architecture allows the system to evolve as a **research platform for clinical AI and complex systems monitoring**.

---

# MetastableX – Complex Systems Engine

One of the experimental components integrated into AKWEMED is **MetastableX**, a framework inspired by **statistical physics and complex systems theory**.

Many biological, physiological and epidemiological systems operate in **meta-stable regimes**, where apparent stability can abruptly shift into instability.

MetastableX investigates these dynamics using structural indicators derived from nonlinear time-series analysis.

Key indicators include:

- autocorrelation (AC1)  
- volatility  
- Fisher information  
- Lempel–Ziv complexity  
- fractal memory (DFA)  
- multiscale entropy  

These indicators allow the system to detect signals associated with:

- loss of system resilience  
- metastable states  
- critical transitions  
- structural instability  

In the context of AKWEMED, this engine explores how **complex systems analysis can complement clinical reasoning**, potentially enabling new approaches to monitoring health dynamics and epidemiological signals.

---

# Technology Stack

AKWEMED combines modern web technologies and machine learning tools.

Core technologies:

- Python  
- Django REST Framework  
- FastAPI  
- Sentence Transformers  
- MiniLM (local embedding model)  

Frontend:

- React  
- TailwindCSS  

Scientific components:

- MetastableX (complex systems analysis)
- QWAN experimental structural monitoring modules

---

# Repository Structure

```
akwemed
│
├── backend
│   ├── django_api
│   └── fastapi_ai
│
├── core
│   ├── clinical
│   │   └── assistant.py
│   │
│   ├── linguistics
│   │   └── xerente.py
│   │
│   ├── rag
│   │   └── search.py
│   │
│   └── metastable
│       └── engine.py
│
├── metastablex
│
├── data
│   ├── protocolos.json
│   └── xerente_glossary.json
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── pages
│   │   └── services
│
├── run_all.py
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/goldenluke/akwemed.git
cd akwemed
```

Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

Install backend dependencies

```
pip install -r requirements.txt
```

Install frontend dependencies

```
cd frontend
npm install
```

---

# Running the System

Start the AI service

```
uvicorn backend.fastapi_ai.main:app --reload --port 9000
```

Start the Django API

```
python manage.py runserver
```

Start the frontend

```
cd frontend
npm run dev
```

Open the interface

```
http://localhost:5173
```

---

# Research Context

AKWEMED is an experimental research platform exploring intersections between:

- AI for healthcare  
- Indigenous language processing  
- medical informatics  
- complex systems science  
- digital epidemiology  

The integration of linguistic interpretation and structural analysis creates a novel environment for investigating **AI-assisted clinical communication in intercultural settings**.

---

# Future Directions

Planned research directions include:

- offline operation in remote villages  
- Android deployment  
- expansion to additional Indigenous languages  
- integration with official clinical protocols  
- structural monitoring of epidemiological systems  
- extended complex systems modeling using MetastableX  

---

# Acknowledgments

This project was inspired by my mother, who worked for nearly a decade in Indigenous healthcare and speaks the Xerente language.

Her experience and dedication to Indigenous communities were fundamental motivations for this research.

---

# License

MIT License

Copyright (c) 2026 Lucas Amaral Dourado

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

---

# Author

Lucas Amaral Dourado  
Researcher in AI, complex systems and digital health.
