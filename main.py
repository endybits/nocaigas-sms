import datetime

from fastapi import FastAPI

from api.schemas import AnalizeMessageResponse, AnalizeMessageWithTimestamp, AnalizeMessage


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
    input_message["timestamp"] = current_time
    message = AnalizeMessageWithTimestamp(**input_message)
    print(message)

    response = {
        "risk_score": 0.85,
        "response_message": "No Caigas, mensaje fraudulento",
        "classification": "Fraudulento",
        "reasons": ["URL Sospechosa", "Keyword: ganaste"],
    }
    return AnalizeMessageResponse(**response)