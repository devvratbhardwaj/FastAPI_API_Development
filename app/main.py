from typing import Optional
from fastapi import FastAPI, status
from fastapi.params import Body

## Using the library "pydantic" to define how our schema should look like
## Does automatic validation for the user input
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):      # does the validation part for the user input
    Title: str
    Content: str
    ID: int

# A decorator is a function that take in functions 
# as their argument, and extends the behaviour of 
# that function (the parameter) without explicitly
# modifying it.

# storing locally instead of database for now
my_posts =[{"Title": "Title of post 1", "Content": "Content of post 1", "ID": 1},
           {"Title": "Fav Foods", "Content": "Pizza", "ID": 2}
           ]

def find_post(id):
    for p in my_posts:
        if p["ID"] == int(id):
            return p


#  object (app) calling method (get) which is an HTTP get request 
@app.get("/")
#Decorator(@)FastAPI_Object.HTTP_Method(Path(OR the URL))
def loggedIn():
    return {"UserName":"Welcome"}


## CREATE

@app.post("/posts", status_code = status.HTTP_201_CREATED)
def create_posts(post:Post):
    my_posts.append(post.model_dump())
    return {"data":my_posts}


## READs

@app.get("/posts")
def get_posts():
    #Logic
    return {"data": my_posts} 

## READ using ID

@app.get("/posts/{id}")
def get_post(id: int):      ## Fast API performing the validation
    try:
        specific_post = find_post(id)
        return {"post_detail": specific_post}
    except:
        return {"post_detail":"post with the given ID doesn't exist"}





## UPDATE


## UPDATE using ID
@app.put("/posts/{id}")
def update_post(id:int, post: Post):    ## it is a function annotation after :
    for i, p in enumerate(my_posts):
        if p["ID"] == id:
            my_posts[i] = post.model_dump()
        return {"Message":f"ID {id} had been updated using PUT"}
    return "ID {id} does not exist"
## DELETE
# When 204 is sent, we don't send back any data in form of messages   
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
@app.delete("/posts/{id}")
def delete_posts(id : int):
    for i,p in enumerate(my_posts):
        if p["ID"]==id:
            my_posts.pop(i) 
            return {"Message":f"Post {id} Removed"}
    return {"Message":f"Post with ID {id} does not exist"}
            # break


## The order of functions matters w.r.t. the URL pathways
## If stuck with and error, try changing the order of the \
## CRUD operation/function.

# @app.post("/posts")
# def create_post(new_post: Post):    ## referencing to the Post pydantic model
#     print(new_post.Title)
#     # return {"Title": new_post.Title, "Rated at: ":new_post.Rating}
#     return new_post.model_dump()
#     # return f"The following has been posted:\
#     # Title: {new_post['Title']}\
#     # Content: {new_post['Content']}"