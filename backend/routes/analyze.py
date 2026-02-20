from fastapi import APIRouter, UploadFile, File, HTTPException
from services.ai_service import analyze_log
import os

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not file.filename.endswith((".log", ".txt")):
        raise HTTPException(status_code=400, detail="Only .log or .txt files allowed")

    content = await file.read()
    log_text = content.decode("utf-8")

    # 파일 저장
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "w") as f:
        f.write(log_text)

    # AI 분석
    analysis = analyze_log(log_text)

    return {
        "filename": file.filename,
        "lines": len(log_text.splitlines()),
        "preview": log_text[:300],
        "analysis": analysis
    }