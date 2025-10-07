from fastapi import FastAPI

app = FastAPI()

# name = "Hanzla Iqbal"
my_list = []

@app.post("/list")
async def create(item:str):
    list_id = 1
    list_id = len(my_list) + 1
    my_list.append(item)
    return {"message": f"The item: {item} was inserted successfully with ID: {list_id}"}
@app.get("/getList")
async def get_list():
    return(f"{my_list} Retreived Successfully")

@app.put("/list/{list_id}")
async def update(list_id: int , item: str):
    my_list[list_id - 1] = {"id": list_id, "item": item}
    return {"message": "Item updated successfully", "data": my_list}
@app.delete("/list/{list_id}")
async def delete(list_id: int):
    del my_list[list_id - 1]
    return {"message": "Item deleted successfully", "data": my_list}
    