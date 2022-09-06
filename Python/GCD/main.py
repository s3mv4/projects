def gcd(a, b):
    if b == 0:
        return a
    if b > a:
        return gcd(b, a)
    return gcd(b, a % b)

nums = [40, 16]
result = max(nums)
for num in nums:
    result = gcd(result, num)

print(result)
