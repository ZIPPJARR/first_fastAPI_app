
from fastapi import FastAPI

app = FastAPI()

@app.get("/", tags = ["ROOT"])
async def root() -> dict:
    return{"Hello": "world"}

shoes = []
count = 1




#get --> shoes list with brand name
@app.get("/shoe/{id}", tags = ["shoes"])
async def get_shoe(id:int, body: dict) -> dict:
    for shoe in dict:
        pass
       

   
# post --> create new brand
@app.post("/shoe", tags = ["shoes"])
async def add_shoe(shoe_dict:dict) -> dict:
    global count 
    shoe_dict["id"] = count
    count += 1
    shoes.append(shoe_dict)        
    return{"data": "A Brand has been added !"}
        
# put --> update brand
@app.put("/shoe/{id}", tags = ["shoes"])
async def update_shoe(id: int, body: dict) -> dict:
    for shoe in shoes:
        if int((shoe ["id"])) == id:
            shoe["brand"] = body["brand"]
            return {
                "data": f"shoe with id {id} has been entered. "
            
            }
    return{
        "data": f"shoe with this id number {id} was not found !"
    }
#get total list
@app.get("/shoe", tags = ["shoes"])
async def get_shoe() -> dict:
    return{"data":shoes} 

#Delete --> deleteting data
@app.delete("/shoe/{id}", tags = ["shoes"])
async def delete_shoe(id: int) -> dict:
    for shoe in shoes:
        
        shoes.remove(shoe)
        return {"data": f"shoe has been deleted" } or {"data": f"shoe with id {id} has been deleted. "}
       










