import threading
from random import choice
from math import inf

def fun3(U, E):
    # U is a list and E is a list of sublists of U.
    C = []
    if len(U) != 0:
        Enew = E.copy()
        covered = []
        while len(covered) != len(U):
            if len(Enew) == 0:
                raise Exception("U cannot be covered by E.")
            Eselected = choice(Enew)
            C.append(Eselected)
            Enew.remove(Eselected)
            for u in Eselected:
                if not u in covered:
                    covered.append(u)
    return C

def fun4(U, E, C):
    covered = []
    for Ei in C:
        for u in Ei:
            if not u in covered:
                covered.append(u)
    score = len(C)
    for u in U:
        if not u in covered:
            score = score + (len(E) + 1)
    best_C = C.copy()
    best_score = score
    for Ei in E:
        new_C = C.copy()
        if Ei in C:
            new_C.remove(Ei)
        else:
            new_C.append(Ei)
        covered = []
        for Ej in new_C:
            for u in Ej:
                if not u in covered:
                    covered.append(u)
        score = len(new_C)
        for u in U:
            if not u in covered:
                score = score + (len(E) + 1)
        if score < best_score:
            best_C = new_C.copy()
            best_score = score
    return best_C

def fun5(U, E):
    # Threaded function to speed up computations
    def threaded_fun3(i, U, E, result):
        result[i] = fun3(U, E)
    
    def threaded_fun4(i, U, E, C_pool, result):
        result[i] = fun4(U, E, C_pool[i])
    
    # Step 1: Parallelizing fun3 calls
    C_pool = [None] * 2
    threads = []
    result = {}
    for i in range(2):
        t = threading.Thread(target=threaded_fun3, args=(i, U, E, result))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    C_pool = [result[i] for i in range(2)]

    # Step 2: Parallelizing fun4 calls
    threads = []
    result = {}
    for i in range(2):
        t = threading.Thread(target=threaded_fun4, args=(i, U, E, C_pool, result))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    # Step 3: Evaluating the best solution
    best_score = inf
    for i in range(2):
        covered = []
        for Ei in C_pool[i]:
            for u in Ei:
                if not u in covered:
                    covered.append(u)
        score = len(C_pool[i])
        for u in U:
            if not u in covered:
                score = score + (len(E) + 1)
        if score < best_score:
            best_C = C_pool[i].copy()
            best_score = score

    return best_C

# Example of input
U1 = [i+1 for i in range(4)]
E1 = [[1, 2], [3, 4], [2]]

# Run the threaded version of fun5
print(fun5(U1, E1))