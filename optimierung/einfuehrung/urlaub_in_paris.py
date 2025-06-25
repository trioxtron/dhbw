from gurobipy import Model, GRB

T = ["2-cent", "5-cent", "5-cent", "20-cent", "50-cent", "2-euro"]

cont = {
        "2-cent": 20,
        "5-cent": 3,
        "20-cent": 10,
        "50-cent": 1,
        "2-euro": 5
}

val = {
        "2-cent": 2,
        "5-cent": 5,
        "20-cent": 20,
        "50-cent": 50,
        "2-euro": 200
}

price = 777

m = Model("urlaub_in_paris")

x = m.addVars(T, lb = 0, vtype=GRB.INTEGER)

m.addConstrs(
        x[t] <= cont[t] for t in T
)

m.addConstr(sum(x[t] * val[t] for t in T) == price)

m.setObjective(
        sum(x[t] for t in T),
        sense = GRB.MAXIMIZE
)

m.optimize()

print("Optimal solution:")
for t in T:
    print(f"{t}: {x[t].X}")
