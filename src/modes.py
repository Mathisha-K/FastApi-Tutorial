from pydantic import BaseModel
class Article(BaseModel):
    created_date: str
    author_id: str
    article_title: str
    article_content: str