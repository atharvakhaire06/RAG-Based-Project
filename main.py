# from google import genai

# client = genai.Client()

# response = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents="Explain how AI works in a few words",
# )

# print(response.text)
import os
import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api
import uuid
import datetime

inngest_client  = inngest.Inngest(
    app_id = "rag_app",
    logger = logging.getLogger("uvicorn"),
    is_production= False,
    serializer=inngest.PydanticSerializer()
)


@inngest_client.create_function(
    fn_id = "Ingest PDF",
    trigger=inngest.TriggerEvent(event = "rag/ingest_pdf")
)
async def inngest_pdf(ctx:inngest.Context):
    return {"hello" : "world"}

app = FastAPI()    

inngest.fast_api.serve(app,inngest_client,[inngest_pdf])
