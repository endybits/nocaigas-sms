import datetime

from fastapi import FastAPI

from api.fraud_detection import detect_fraud
from api.schemas import (
    AnalizeMessageResponse, 
    AnalizeMessageWithTimestamp,
    AnalizeMessage,
    FeedbackMessage,
    FeedbackResponse
)


# Use rout

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/analize", tags=["Analize Message"])
async def analize_message(
    input_message: AnalizeMessage
) -> AnalizeMessageResponse:
    
    current_time = datetime.datetime.now().isoformat().split(".")[0] + "Z"
    
    input_dict = input_message.model_dump()
    input_dict["timestamp"] = current_time
    message = AnalizeMessageWithTimestamp(**input_dict)
    
    # Getting message_id
    message_id = "12345"

    detected_fraud = detect_fraud(
        message.message,
        message.sender,
        message_id
    )

    response = {
        "risk_score": detected_fraud["risk_score"] if "risk_score" in detected_fraud else 0.0,
        "response_message": "No Caigas, mensaje fraudulento", # Hardcoded response message - Use AI to generate a response message
        "classification": detected_fraud["classification"] if "classification" in detected_fraud else "Seguro",
        "reasons": detected_fraud["reasons"] if "reasons" in detected_fraud else [],
        "message_id": message_id
    }
    return AnalizeMessageResponse(**response)





# ----- FEEDBACK MECHANISM -----

@app.post("/feedback", tags=["Feedback Mechanism"])
async def feedback(
    feedback_message: FeedbackMessage
) -> FeedbackResponse:
    response = {
        "status": "success",
        "message": "Feedback recorded. Thank you!"
    }
    return FeedbackResponse(**response)
