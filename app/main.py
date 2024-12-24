from fastapi import FastAPI
from routes import post_routes

app = FastAPI(
  title="Blog API",
  description="This API allows users to manage blog posts, including creating, updating, retrieving, and deleting posts.",
  version="1.0.0",
  docs_url="/docs",
)

app.include_router(post_routes.router)






