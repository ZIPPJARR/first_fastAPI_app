from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags = ["ROOT"])
async def root() -> dict:
    return{"Hello": "world"}



#get --> shoes list with brand name
@app.get("/shoe", tags = ["shoes"])
async def get_shoe() -> dict:
    return{"data": shoes}


# post --> create new brand
@app.post("/shoe", tags = ["shoes"])
async def add_shoe(shoe:dict) -> dict:
    shoes.append(shoe)
    return{"data": "A Brand has been added !"}


# put --> update brand
@app.put("/shoe/{id}", tags = ["shoes"])
async def update_shoe(id: int, body: dict) -> dict:
    for shoe in shoes:
        if int((shoe ["id"])) == id:
            shoe["Brand"] = body["Brand"]
            return {
                "data": f"shoe with id {id} has been entered. "
            
            }
    return{
        "data": f"shoe with this id number {id} was not found !"
    }


#Delete --> deleteting data
@app.delete("/shoe/{id}", tag = ["shoes"])
async def delete_shoe(id: int) -> dict:
    for int in shoes:
        shoes.remove(shoes)
        return {"data": f"shoe has been deleted" } or {"data": f"shoe with id {id} has been deleted. "}
        return{
            "data":f"this shoe with id {id} was not found"
        }



shoes = [
    {
        "id": "1",
    "Brand": "Jordan"
    },
    {
        "id": "2",
        "Brand": "NIKE"
    }

]




