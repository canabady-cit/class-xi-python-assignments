# To find simple interest 
# with given Principle (p), No. of Years (n) and Rate of Interest (r)
p = int(input("Enter principle: "))
n = int(input("Enter number of years: "))
r = int(input("Enter the rate of interest: "))

interest = (p * n * r ) / 100

print("\nPrinciple = ", p)
print("Years = ", n)
print("Rate of Interest = ", r)

print("Simple interest = ",interest)
