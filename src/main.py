from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from faker import Faker
import string 

app = FastAPI()
fake = Faker()

articles = [
    {
        "created_date": "2019-04-09T12:00:00Z",
        "author_id": "4421-45V2-1909-2404-0143-J9936",
        "article_title": "the lord of the nameless",
        "article_content": "But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or pursues or desires to obtain pain of itself, because it is pain, but because occasionally"
    },
     {
        "created_date": "2022-03-01T01:00:00Z",
        "author_id": "090W-73W4-4407-3902-352P-193W9",
        "article_title": "avian shadow",
        "article_content": "The European languages are members of the same family. Their separate existence is a myth. For science, music, sport, etc, Europe uses the same vocabulary. The languages only differ in their grammar, their pronunciation and their most common words. Everyone realizes why a new common language would be desirable: one could refuse to pay expensive translators. To achieve this, it would be necessary to have uniform grammar, pronunciation and more common words. If several languages coalesce, the grammar of the resulting language is more simple and regular than that of the individual languages. The new common language will be more"
    },
     {
        "created_date": "1993-11-23T09:00:00Z",
        "author_id": "42C5-2277-2521-6V53-3K37-57706",
        "article_title": "the eye of isle",
        "article_content": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth."
    },
     {
        "created_date": "1888-03-019T14:00:00Z",
        "author_id": "9112-7055-80HX-3539-4093-J3376",
        "article_title": "bound for duty",
        "article_content": "The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps. Bawds jog, flick quartz, vex nymphs. Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. Brick quiz whangs jumpy veldt fox. Bright vixens jump; dozy fowl quack. Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Sex-charged fop blew my junk TV quiz. How quickly daft jumping zebras vex. Two driven jocks help fax my big quiz. Quick, Baz, get my woven flax jodhpurs!"
    },
    {
        "created_date": "2001-02-01T02:00:00Z",
        "author_id": "6735-4818-43R0-7408-0K74-16478",
        "article_title": "the steel throne",
        "article_content": "Bryan had made peace with himself and felt comfortable with the choices he made. This had made all the difference in the world."
    }
]

class Article(BaseModel):
    created_date: str
    author_id: str
    article_title: str
    article_content: str

class Articles(BaseModel):
    articles: List[Article]

@app.post("/items/{author_id}")
async def add_item(articles: list[Article]): 
    response = []
    
    for article in articles:
        title = string.capwords(article.article_title)
        text = article.article_content.split()

        if len(text) > 50:
            text = text[:50]
            text = ' '.join(text) + "..."
        else:
            text = ' '.join(text)
    
        response.append(
        {
            "created_date": article.created_date,
            "author_name": fake.name(),
            "article_title": title,
            "article_summary": text
        })
    
    return response