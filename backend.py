import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/rates")
def fet_fx__rates():
    try:
        url = "https://er-api.com"
        response = requests.get(url)
        data = response.json()

        rates = data.get("rates", {})

        return {
            "status": "success",
            "base" : "GBP",
            "rates": {
                "USD": round(rates.get("USD", 0), 4),
                "EUR": round(rates.get("EUR", 0), 4),

            }

        }
    except Exception as e:
        return {"status": "error" , "message": str(e)}