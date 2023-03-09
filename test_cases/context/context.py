from typing import List
def foo() -> List[int]:
    lst = [1]
    lst.append("2")
    return [int(x) for x in lst]

print(foo())