from fastapi import APIRouter

router = APIRouter()


@router.get("/plugin/hello")
def hello_plugin():
    return {"message": "Hello from plugin!"}
