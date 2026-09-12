from fastapi import FastAPI

app = FastAPI(
    title="FitFlow AI Service",
    description="AI service for workout recommendations and nutrition analysis.",
    version="0.1.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "fitflow-ai-service"}

@app.get("/recommendation/example")
def example_recommendation():
    return {
        "goal": "general fitness",
        "fitness_level": "beginner",
        "duration_minutes": 15,
        "message": "Starter endpoint for future AI-powered workout recommendations.",
    }
