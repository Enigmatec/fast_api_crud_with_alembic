from fastapi import FastAPI
from app.controllers.user_controller import UserController
from app.controllers.login_controller import LoginController
from app.controllers.profile_controller import ProfileController
from app.models.user_model import User
from app.models.post_model import Post
import logging
from app.controllers.user_post_controller import UserPostController

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Write logs to file
        logging.StreamHandler()  # Keep logs visible in terminal
    ]
)

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(UserController.router)
app.include_router(LoginController.router)
app.include_router(ProfileController.router)
app.include_router(UserPostController.router)



@app.get("/",tags=["index"])
async def root():
    return {"message" : "Welcome to FastAPI Project"}
    