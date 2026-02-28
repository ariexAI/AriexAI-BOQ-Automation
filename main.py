from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel, Field
from fastapi.responses import FileResponse
import shutil
import os

# SERVICES
from services.footing_service import calculate_footing
from services.slab_service import calculate_slab
from services.boq_services import generate_project_boq
from services.excel_service import generate_boq_excel
from services.pdf_service import detect_footing_sizes



app = FastAPI()


# -----------------------
# FOOTING INPUT MODEL
# -----------------------

class FootingInput(BaseModel):

    number_of_footings: int = Field(gt=0)

    length: float = Field(gt=0)
    breadth: float = Field(gt=0)
    footing_depth: float = Field(gt=0)
    excavation_depth: float = Field(gt=0)
    pcc_thickness: float = Field(gt=0)

    steel_diameter: float = Field(gt=0)
    steel_spacing: float = Field(gt=0)

    excavation_rate: float = Field(ge=0)
    pcc_rate: float = Field(ge=0)
    rcc_rate: float = Field(ge=0)
    steel_rate: float = Field(ge=0)


# -----------------------
# SLAB INPUT MODEL
# -----------------------

class SlabInput(BaseModel):

    length: float = Field(gt=0)
    breadth: float = Field(gt=0)
    thickness: float = Field(gt=0)

    steel_diameter: float = Field(gt=0)
    steel_spacing: float = Field(gt=0)

    rcc_rate: float = Field(ge=0)
    steel_rate: float = Field(ge=0)


# -----------------------
# PROJECT INPUT MODEL
# -----------------------

class ProjectInput(BaseModel):

    footing: FootingInput
    slab: SlabInput


# -----------------------
# HOME
# -----------------------

@app.get("/")
def home():

    return {"message": "Welcome to AriexAI BOQ Engine"}


# -----------------------
# FOOTING BOQ
# -----------------------

@app.post("/calculate_full_footing")
def calculate_full_footing_endpoint(data: FootingInput):

    result = calculate_footing(data)

    return {

        "project_summary": {

            "number_of_footings": data.number_of_footings,

            "total_cost": round(result["total_cost"], 2)

        }
    }


# -----------------------
# SLAB BOQ
# -----------------------

@app.post("/calculate_slab")
def slab_endpoint(data: SlabInput):

    result = calculate_slab(data)

    return {

        "volume_m3": round(result["volume"], 2),

        "steel_kg": round(result["steel_weight"], 2),

        "concrete_cost": round(result["concrete_amount"], 2),

        "steel_cost": round(result["steel_amount"], 2),

        "total_cost": round(result["total_cost"], 2)

    }


# -----------------------
# PROJECT BOQ
# -----------------------

@app.post("/calculate_project_boq")
def calculate_project_boq_endpoint(data: ProjectInput):

    return generate_project_boq(data)


# -----------------------
# DOWNLOAD BOQ EXCEL
# -----------------------

@app.post("/download_boq_excel")
def download_boq_excel(data: ProjectInput):

    result = generate_project_boq(data)

    boq_data = result["boq"]

    grand_total = result["grand_total"]

    file_path = generate_boq_excel(

        boq_data,
        grand_total

    )

    return FileResponse(

        path=file_path,

        filename="project_boq.xlsx",

        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

    )


# -----------------------
# UPLOAD DRAWING
# -----------------------

@app.post("/upload_drawing")
def upload_drawing(file: UploadFile = File(...)):

    upload_folder = "drawings"

    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    return {

        "message": "Drawing uploaded successfully",

        "file_name": file.filename,

        "location": file_path

    }


# -----------------------
# DETECT FOOTING SIZES
# -----------------------

@app.get("/detect_footing_sizes")
def detect_footing_sizes_api():

    drawing_folder = "drawings"

    files = os.listdir(drawing_folder)

    if not files:
        return {"message": "No drawings found"}

    latest_file = os.path.join(drawing_folder, files[-1])

    result = detect_footing_sizes(latest_file)

    return {
        "file": latest_file,
        "detected_sizes": result
    }