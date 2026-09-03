from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from matplotlib.pylab import solve
from pydantic import BaseModel
from formula import solve

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
class FormulaRequest(BaseModel):
    formula: list[list[int]]
    
@app.post("/solve")
def solve_endpoint(request: FormulaRequest):
    result = solve(request.formula)
    if result == "UNSATISFIABLE":
        return {"SATISFIABLE": False, "assignment": None}
    return {"satisfiable": True, "assignment": result}