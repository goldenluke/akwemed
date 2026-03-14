<div align="center">

# 🧠 AKWEMED  
### Indigenous Clinical AI Assistant for Intercultural Healthcare

An experimental **clinical AI system** designed to support healthcare professionals working in **Indigenous territories**, integrating **natural language processing, retrieval-augmented reasoning, and Indigenous language interpretation**.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-API-green)
![FastAPI](https://img.shields.io/badge/FastAPI-AI%20Service-009688)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![Tailwind](https://img.shields.io/badge/TailwindCSS-UI-38BDF8)
![License](https://img.shields.io/badge/license-MIT-black)

</div>

---

# 🌎 Overview

**AKWEMED** is a prototype **clinical artificial intelligence assistant** designed to support medical decision-making in **intercultural healthcare contexts**, particularly within **Indigenous communities in Brazil**.

The system combines:

- Indigenous language interpretation
- Retrieval-Augmented Clinical Reasoning (RAG)
- Local AI inference
- Mobile-first deployment
- Offline operation capability

The goal is to reduce **communication barriers between healthcare professionals and Indigenous patients**.

---

# 🧭 Motivation

In many Indigenous territories, healthcare professionals face challenges such as:

- linguistic barriers  
- culturally specific symptom descriptions  
- lack of clinical decision support tools adapted to local contexts  
- limited internet connectivity  

AKWEMED explores how **AI systems can assist intercultural clinical communication**.

The system integrates linguistic interpretation of **Xerente (Akwẽ)** expressions with clinical protocol retrieval.

Example input:

```
ĩsĩ kâ peito
```

System interpretation:

```
dor no peito
```

Clinical output:

```
Possible protocol: Acute Coronary Syndrome
```

---

# 🧠 System Architecture

AKWEMED follows a **multi-layer architecture** separating the clinical interface from the AI reasoning engine.

```
React Frontend (Chat Interface)
        ↓
Django REST API
        ↓
FastAPI AI Service
        ↓
Xerente Language Interpreter
        ↓
Clinical RAG Engine
        ↓
Protocol Knowledge Base
```

---

# ⚙️ Core Components

## Frontend

**React + TailwindCSS**

Provides a conversational clinical interface:

- chatbot-style UI  
- clinical response cards  
- mobile-friendly layout  
- real-time API interaction  

---

## Backend API

**Django REST Framework**

Responsible for:

- request validation  
- API routing  
- integration with AI service  
- authentication layer (future)  

---

## AI Service

**FastAPI**

Handles:

- natural language interpretation  
- clinical retrieval  
- inference logic  
- semantic similarity search  

---

## Linguistic Layer

The **Xerente interpreter** normalizes indigenous expressions into medical concepts.

Example:

```
ĩsĩ → dor
kâ → em / no
```

Normalized query:

```
dor no peito
```

---

## Clinical Knowledge Retrieval

The system uses **sentence-transformer embeddings** to perform semantic search over clinical protocols.

Pipeline:

```
query → embedding → similarity search → protocol match
```

---

# 🧩 Repository Structure

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
│   └── rag
│       └── search.py
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
│   │
│   └── index.html
│
├── models
│
├── run_all.py
│
└── README.md
```

---

# 🚀 Installation

Clone the repository:

```
git clone https://github.com/goldenluke/akwemed.git
cd akwemed
```

Create virtual environment:

```
python -m venv venv
source venv/bin/activate
```

Install backend dependencies:

```
pip install -r requirements.txt
```

Install frontend dependencies:

```
cd frontend
npm install
```

---

# 🧪 Running the System

Start the AI service:

```
uvicorn backend.fastapi_ai.main:app --reload --port 9000
```

Start Django API:

```
python manage.py runserver
```

Start frontend:

```
cd frontend
npm run dev
```

Access interface:

```
http://localhost:5173
```

---

# 💬 Example Interaction

User input:

```
ĩsĩ kâ peito
```

System output:

```
Interpretation
dor no peito

Clinical Protocol
Infarto com Supra de ST

Recommendation
Avaliar síndrome coronariana aguda
```

---

# 📱 Offline Mode (Planned)

AKWEMED is designed to support **offline deployment in remote territories**.

Future goals include:

- lightweight local AI models  
- Android deployment  
- edge inference  
- offline protocol database  

---

# 🔬 Research Context

AKWEMED is a **research prototype** exploring:

- intercultural clinical communication  
- indigenous language processing  
- AI-assisted healthcare in remote environments  
- clinical decision support systems  

The project contributes to discussions in:

- **medical informatics**  
- **digital health**  
- **indigenous health policy**  
- **AI for social impact**

---

# 🛣️ Roadmap

Future development directions:

- multi-turn clinical conversations  
- expanded indigenous language coverage  
- clinical reasoning modules  
- voice interface  
- offline mobile deployment  
- epidemiological integration  

---

# 🤝 Contributing

Contributions are welcome.

Possible areas:

- indigenous linguistics  
- medical informatics  
- AI systems engineering  
- health data science  

Pull requests and issue reports are encouraged.

---

# 📜 License

MIT License

```
MIT License

Copyright (c) 2026 Lucas Dourado

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

# 👤 Author

Lucas Amaral Dourado
Medical student and researcher in **AI, complex systems and digital health**.

---
