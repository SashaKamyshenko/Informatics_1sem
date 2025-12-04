heights = list(map(int, input().split()))
len = len(heights)
stack = []
result = []

for i in range(len):
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()
    if not stack:
        result.append(-1)
    else:

        result.append(stack[-1])

    while stack and heights[stack[-1]] == heights[i]:
        stack.pop()
    stack.append(i)

print(" ".join(map(str, result)))
