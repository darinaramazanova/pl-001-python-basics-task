def merge_sorted_lists(first: list[int], second: list[int]) -> list[int]:
    a=[]
    for i in range(len(first)):
        a.append(first[i])
    for j in range(len(second)):
        a.append(second[j])
    return sorted(a) 
assert merge_sorted_lists([], []) == []
assert merge_sorted_lists([1, 2], []) == [1, 2]
assert merge_sorted_lists([], [1, 2]) == [1, 2]
assert merge_sorted_lists([1, 2, 3], [4, 5]) == [1, 2, 3, 4, 5]
assert merge_sorted_lists([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]
assert merge_sorted_lists([1, 1], [1]) == [1, 1, 1]

print("All tests passed")