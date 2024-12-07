import datetime

from fastapi import FastAPI

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
    print(message)

    response = {
        "risk_score": 0.85,
        "response_message": "No Caigas, mensaje fraudulento",
        "classification": "Fraudulento",
        "reasons": ["URL Sospechosa", "Keyword: ganaste"],
        "message_id": "12345"
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
