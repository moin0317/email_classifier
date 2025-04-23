from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models import load_model, predict_category
from utils import mask_pii

router = APIRouter()
model = load_model()


class EmailRequest(BaseModel):
    input_email_body: str


@router.post("/classify_email")
def classify_email(request: EmailRequest):
    email_body = request.input_email_body
    masked_email, entities = mask_pii(email_body)
    try:
        category = predict_category(masked_email, model)
        return {
            "input_email_body": email_body,
            "list_of_masked_entities": entities,
            "masked_email": masked_email,
            "category_of_the_email": category,
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
