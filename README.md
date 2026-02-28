# 🚀 AriexAI — AI Powered BOQ Automation Engine
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?logo=fastapi)
![OpenPyXL](https://img.shields.io/badge/Excel-Automation-yellow)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)
![AEC](https://img.shields.io/badge/Industry-AEC-orange)
> A scalable AI-driven backend engine built to automate Bill of Quantities (BOQ), structural quantity takeoff, and Excel-based estimation workflows for the AEC industry.

AriexAI is designed to reduce manual Excel work, automate structural quantity calculations, and build a scalable backend foundation for future AI-assisted drawing analysis.

---

## 🏗 Problem Statement

Manual BOQ preparation is:
- Time-consuming
- Error-prone
- Repetitive
- Dependent on Excel-heavy workflows

AriexAI aims to automate excavation, PCC, RCC, steel, slab, and footing calculations through a modular API-based backend system.

---

## ⚙️ Tech Stack

- **Python**
- **FastAPI**
- **Pydantic (Data Validation)**
- **Uvicorn**
- **OpenPyXL (Excel Generation)**
- **Modular Service Architecture**

---

## 🧠 Core Features

✔ Footing quantity calculation (Excavation, PCC, RCC, Steel)  
✔ Slab quantity & cost estimation  
✔ Structured service-layer backend  
✔ Input validation using Pydantic models  
✔ Auto-generated Swagger UI documentation  
✔ Excel BOQ export support  
✔ Multi-module scalable architecture  

---

## 🏛 Project Architecture

```
ariexAI/
│
├── main.py
├── services/
│   ├── footing_service.py
│   ├── slab_service.py
│   ├── boq_services.py
│
├── drawings/
├── downloads/
│
├── project_boq.xlsx
├── requirements.txt
├── .gitignore
└── README.md
```

The system follows a clean separation between:

- **API Layer** → FastAPI endpoints defined in `main.py`
- **Engineering Logic Layer** → Quantity calculations handled inside `services`
- **Output Layer** → Excel BOQ generation and file handling

This modular structure allows scalability for future AI features such as PDF drawing analysis and BIM integration.

