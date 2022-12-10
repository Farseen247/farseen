#We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones.
# If n is odd, all piles have an odd number of stones.
# Each pile must more stones than the previous pile but as few as possible.

n=int(input("Enter number of piles : "))
def test(n):
    return [n + 2 * i for i in range(n)]
print("Number of piles:",n)
print("Number of stones in each pile:")
print(test(n))