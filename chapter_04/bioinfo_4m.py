import sys

def get_positive_distances(input_str):
    raw_list = list(map(int, input_str.strip().split()))
    # 양수만 필터링
    L = sorted([x for x in raw_list if x > 0])
    return L

def check_and_remove(L, dists_to_check):
    temp_removed = []
    possible = True
    
    for d in dists_to_check:
        if d in L:
            L.remove(d)
            temp_removed.append(d)
        else:
            possible = False
            break
    
    if not possible:
        for d in temp_removed:
            L.append(d)
        L.sort()
        return False
    
    return True

def restore_distances(L, dists_to_restore):
    for d in dists_to_restore:
        L.append(d)
    L.sort()

def place_point(L, A, width):
    if not L:
        return sorted(A)
    
    d_max = L[-1]
    
    # --- Option 1: 점을 width - d_max 위치에 배치 (작은 좌표 우선) ---
    candidate_small = width - d_max
    dists_small = [abs(candidate_small - a) for a in A]
    
    if check_and_remove(L, dists_small):
        A.append(candidate_small)
        result = place_point(L, A, width)
        if result is not None:
            return result
        # 실패 시 백트래킹
        A.pop()
        restore_distances(L, dists_small)

    # --- Option 2: 점을 d_max 위치에 배치 (큰 좌표 나중) ---
    candidate_large = d_max
    dists_large = [abs(candidate_large - a) for a in A]
    
    if check_and_remove(L, dists_large):
        A.append(candidate_large)
        result = place_point(L, A, width)
        if result is not None:
            return result
        # 실패 시 백트래킹
        A.pop()
        restore_distances(L, dists_large)
        
    return None

def turnpike_problem(input_str):
    L = get_positive_distances(input_str)
    width = L.pop() 
    A = [0, width]
    
    result = place_point(L, A, width)
    return result

# --- 실행부 ---
if __name__ == "__main__":
    try:
        with open("input/rosalind_ba4m.txt", "r") as f:
            input = f.read().strip()
    except:
        # Rosalind Sample Dataset
        input = "-10 -8 -7 -6 -5 -4 -3 -3 -2 -2 0 0 0 0 0 2 2 3 3 4 5 6 7 8 10"
    
    result = turnpike_problem(input)
    print(result)