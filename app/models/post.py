from pydantic import BaseModel
from typing import Optional

class Post(BaseModel):
  title: str
  content: str
  author: str

  class Config:
    json_schema_extra = {
      "example": {
        "title": "First Post",
        "content": "This is a first post content.",
        "author": "Hello World",
      }
    }


class PostUpdate(BaseModel):
  title: Optional[str] = None
  content: Optional[str] = None
  author: Optional[str] = None

  class Config:
    json_schema_extra = {
      "example": {
        "content": "This is a firstupdated post content.",
        "author": "Hello Developers",
      }
    }