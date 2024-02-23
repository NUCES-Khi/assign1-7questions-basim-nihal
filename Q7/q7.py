import random

def solve(n, max_iterations=1000):

#starting from a random state
    solution = []
    for _ in range(n):
        solution.append(random.randint(0, n - 1))

    for _ in range(max_iterations):
        conflicts = CalculateConflicts(solution)
        if conflicts == 0:
            return solution  # Solution found
        
        neighbor = betterneibhour(solution)
        if neighbor is None:
            continue
        solution = neighbor

    return None  # No solution found

def CalculateConflicts(solution):
    # Shuru mein ham conflicts ko 0 kar ke shuru karte hain.
    conflicts = 0
    for i in range(len(solution)):
        # Dusre queens ke saath compare
        for j in range(i + 1, len(solution)):
            # Agar dono queens ek hi column mein hain ya phir unki diagonal pe hai to ye ek conflict hai.
            if solution[i] == solution[j] or abs(i - j) == abs(solution[i] - solution[j]):
               
                conflicts += 1
    return conflicts


def betterneibhour(solution):
    min_conflicts = CalculateConflicts(solution)
    better_neighbor = None
    for i in range(len(solution)):
        for j in range(len(solution)):
            if solution[i] != j:
                neighbor = solution[:]
                neighbor[i] = j
                conflicts = CalculateConflicts(neighbor)
                if conflicts < min_conflicts:
                    min_conflicts = conflicts
                    better_neighbor = neighbor
    return better_neighbor

def Print(solution):
    if solution:
        print("Solution found:")
        for row in solution:
            print("." * row + "Q" + "." * (len(solution) - row - 1))
    else:
        print("No solution found")


n = int(input("Enter the number of queens: "))
solution = solve(n)
Print(solution)
