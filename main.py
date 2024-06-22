from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body

## Using the library "pydantic" to define how our schema should look like
## Does automatic validation for the user input
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):      # does the validation part for the user input
    Title: str
    Content: str
    Rating: Optional[int] = None

# A decorator is a function that take in functions 
# as their argument, and extends the behaviour of 
# that function (the parameter) without explicitly
# modifying it.

#  object (app) calling method (get) which is an HTTP get request 
@app.get("/")
#Decorator(@)FastAPI_Object.HTTP_Method(Path(OR the URL))
def loggedIn():
    return {"UserName":"Welcome"}

@app.get("/posts")
def get_posts():
    #Logic
    return {"data":"post data"} 

@app.post("/posts")
def create_post(new_post: Post):    ## referencing to the Post pydantic model
    print(new_post.Title)
    # return {"Title": new_post.Title, "Rated at: ":new_post.Rating}
    return new_post.model_dump()
    # return f"The following has been posted:\
    # Title: {new_post['Title']}\
    # Content: {new_post['Content']}"