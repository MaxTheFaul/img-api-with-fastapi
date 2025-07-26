from fastapi import FastAPI
from fastapi.responses import FileResponse
import glob, os
file_paths = []
os.chdir("./img")
for file in glob.glob("*.jpg"):
    file_paths.append(file)
print(file_paths[1]) 
api = FastAPI()
@api.get("/img/{item_id}")
def get_item(item_id: int):
    item = file_paths[item_id]
    return FileResponse(item)
