from enum import Enum 
from fastapi import FastAPI ,HTTPException ,Request ,Form
from pydantic import BaseModel 
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles 
from starlette.middleware.sessions import SessionMiddleware 
from pwdlib  import PasswordHash 
from fastapi.responses import RedirectResponse 

app = FastAPI() 

templates = Jinja2Templates(directory='templates')
app.mount("/static",StaticFiles(directory="static"),name="static")

app.add_middleware(
    SessionMiddleware,
    secret_key='change-this-secret-key'
)

password_hash = PasswordHash.recommended() 

users = {}

items_db = [] 

@app.get("/")
async def home(request: Request):
    username = request.session.get('username') 
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request,
                 "username":username}
    )

@app.get("/register")
async def register_page(request:Request):
    return templates.TemplateResponse(
        request= request,
        name="register.html"
    )

@app.post("/register")
async def register(
    request:Request,
    username:str = Form(...),
    password:str = Form(...)
):
    if username  in users:
        return templates.TemplateResponse(
            request=request,
            name='register.html',
            context={
                "error":"Username  already exists"
            }
        )
    
    hashed_password = password_hash.hash(password) 
    users[username] =  hashed_password 
    
    return RedirectResponse(
        url="/login",
        status_code=303
    )

@app.get("/login")
async  def  login_page(request:Request):
    return templates.TemplateResponse (
        request=request,
        name="login.html"
    )
        
@app.post("/login")
async def login(
    request:Request,
    username:str = Form(...),
    password:str= Form(...)
):
    if username not in users:
        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={
                "error": "Invalid username or password"
            }
        ) 
    if not password_hash.verify(
        password,
        users[username]
    ):

        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={
                "error": "Invalid username or password"
            }
        )

    request.session["username"] = username

    return RedirectResponse(
        url="/",
        status_code=303
    )

@app.get("/create") 
async def create_page(request:Request):
    return templates.TemplateResponse(
        request= request,
        name='create.html',
        context = {'request': request}
    )


@app.post("/items/") 
async def create_item(
    name:str = Form(...),
    category: str = Form(...),
    location: str = Form(...),
    date: str = Form(...),
    description: str = Form(...),
    status: str = Form(...)
):
    item = {
        "name": name,
        "category": category,
        "location": location,
        "date": date,
        "description": description,
        "status": status
    }

    items_db.append(item)

    return item


@app.get("/search")
async def search_page(
    request: Request,
    category: str | None = None,
    location: str | None = None,
    status: str | None = None
):
    results = items_db

    if category:
        results = [item for item in results
                   if item["category"] == category]

    if location:
        results = [item for item in results
                   if item["location"] == location]

    if status:
        results = [item for item in results
                   if item["status"] == status]
    
    return templates.TemplateResponse(
        request= request,
        name = "search.html",
        context={"request":request,"result": results}
    )