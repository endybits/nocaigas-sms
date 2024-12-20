
from pydantic import BaseModel
from pydantic.fields import Field



# ----- ANALIZE MESSAGE -----

# {
#     "sender": "+573001234567",
#     "message": "Felicidades, ganaste un premio. Ingresa a bit.ly/abc123 para reclamarlo.",
#     "timestamp": "2024-12-03T10:00:00Z"
# }
class AnalizeMessage(BaseModel):
    sender: str = Field(..., example="+573001234567")
    message: str = Field(..., example="Felicidades, ganaste un premio. Ingresa a bit.ly/abc123 para reclamarlo.")
    
class AnalizeMessageWithTimestamp(AnalizeMessage):
    timestamp: str = Field(..., example="2024-12-03T10:00:00Z")


# {
#     "risk_score": 0.85,
#     "classification": "Fraudulent",
#     "reasons": ["Suspicious URL", "Keyword: ganaste"]
# }

class AnalizeMessageResponse(BaseModel):
    risk_score: float = Field(..., example=0.85)
    response_message: str = Field(..., example="No Caigas, mensaje fraudulento")
    classification: str = Field(..., example="Fraudulent")
    reasons: list[str] = Field(..., example=["Suspicious URL", "Keyword: ganaste"])
    message_id: str = Field(..., example="12345")



# ----- FEEDBACK MECHANISM -----
# {
#     "message_id": "12345",
#     "correct_classification": "Safe"
# }

class FeedbackMessage(BaseModel):
    message_id: str = Field(..., example="12345")
    correct_classification: str = Field(..., example="Safe")


# {
#     "status": "success",
#     "message": "Feedback recorded. Thank you!"
# }
class FeedbackResponse(BaseModel):
    status: str = Field(..., example="success")
    message: str = Field(..., example="Feedback recorded. Thank you!")