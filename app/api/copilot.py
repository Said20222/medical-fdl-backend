from fastapi import APIRouter, HTTPException
from app.schemas.copilot import CopilotRequest, CopilotResponse
from app.services.copilot_service import CopilotService

router = APIRouter(prefix="/api", tags=["copilot"])


@router.post("/copilot/answer", response_model=CopilotResponse)
def copilot_answer(payload: CopilotRequest):
    try:
        service = CopilotService()

        raw_response, retrieved = service.generate_answer(
            question=payload.question,
            explanation_payload=payload.explanation_payload.model_dump(),
        )

        parsed = CopilotResponse.model_validate_json(raw_response)
        return parsed

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))