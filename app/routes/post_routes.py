from fastapi import APIRouter, HTTPException
from models.post import Post, PostUpdate
from typing import List

router = APIRouter()

posts_db = {}


@router.post("/posts", response_model=Post)
async def create_post(post: Post):
  """
  Create a new blog post.
  
  - **title**: Title of the post.
  - **content**: Content of the post.
  - **author**: Author of the post.
  """
  if post.title in posts_db:
    raise HTTPException(status_code=400, detail="Post with this title already exists.")
  
  posts_db[post.title] = post
  return post


@router.get("/posts", response_model=List[Post])
async def get_posts():
  """
  Retrieve a list of all blog posts available in the database.
  """
  return list(posts_db.values())


@router.get("/posts/{title}", response_model=Post)
async def get_post(title: str):
  """
  Retrieve a specific blog post by its title.
  
  - **title**: Title of the post to retrieve.
  
  Raises a `404` if the post is not found.
  """
  if title not in posts_db:
    raise HTTPException(status_code=404, detail="Post not found")
  return posts_db[title]


@router.put("/posts/{title}", response_model=Post)
async def update_post(title: str, post_update: PostUpdate):
  """
  Update an existing post by its title.
  
  - **title**: Title of the post to update.
  - **post_update**: The fields to update (title, content, author).
  
  Raises a `404` if the post is not found.
  """
  
  if title not in posts_db:
    raise HTTPException(status_code=404, detail="Post not found")
  
  current_post = posts_db[title]
  updated_post = current_post.copy(update=post_update.model_dump(exclude_unset=True))
  posts_db[title] = updated_post
  return updated_post


@router.delete("/posts/{title}", response_model=Post)
async def delete_post(title: str):
  """
  Delete a specific post by its title.
  
  - **title**: Title of the post to delete.
  
  Raises a `404` if the post is not found.
  """
  if title not in posts_db:
    raise HTTPException(status_code=404, detail="Post not found")
  
  deleted_post = posts_db.pop(title)
  return deleted_post




