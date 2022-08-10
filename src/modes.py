from pydantic import BaseModel
from typing import List

class Article(BaseModel):
    created_date: str
    author_id: str
    article_title: str
    article_content: str

class Articles(BaseModel):
    articles: List[Article]