formula = [
    [1, -2],
    [2, 3],
    [-1, 3]
]
def is_satisfied(formula, assignment):
    for clause in formula:
        clause_true = False
        for literal in clause:
            var = abs(literal)
            if var in assignment:
                
                value = assignment[var]
                
                if literal < 0 :
                    value = not value
                if value:
                    clause_true = True
                    break
        if not clause_true:
            return False
    return True

def unit_propagate(formula, assignment):
    assignment= assignment.copy()
    changed = True
    while changed:
        changed = False
        for clause in formula:
            unassigned = [lit for lit in clause if abs(lit) not in assignment]
            values = [assignment [abs(lit)] == (lit > 0) for lit in clause if abs (lit) in assignment]
            if any(values):
                continue
            if len(unassigned) == 1:
                lit = unassigned[0]
                assignment[abs(lit)] = (lit > 0)
                changed = True
            elif len(unassigned) == 0:
                return None
    return assignment

def dpll(formula, assignment ={}):
    assignment = unit_propagate(formula, assignment)
    if assignment is None:
        return None

    if is_satisfied(formula, assignment):
        return assignment
    
    unassigned_vars = set(abs(lit) for clause in formula for lit in clause) - set(assignment.keys())
    if not unassigned_vars:
        return None
    
    var = next(iter(unassigned_vars))
    
    for value in [True, False]:
        new_assignment = assignment.copy()
        new_assignment[var] = value
        
        result = dpll(formula,new_assignment)
        if result is not  None:
            return result
        
    return None
def solve(formula):
    result = dpll(formula, {})
    if result is None:
        return "UNSATISFIABLE"
    return result
   
    
def read_dimacs(filepath):
    formula = []
    with open(filepath, 'r') as f:  
        for line in f:
            line = line.strip()
            if line.startswith('c') or line.startswith('p') or line =='':
                continue
            literals = [int(x) for x in line.split()]
            clause = literals [:-1]
            formula.append(clause)
    return formula


if __name__ == "__main__":
    formula = read_dimacs("test2.cnf")
    result = solve(formula)
    print(result)  
        