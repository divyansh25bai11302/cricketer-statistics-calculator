print("Cricket Stats")
print("-------------")

# Take input
runs = input("Total runs: ")
balls = input("Total balls faced: ")
outs = input("Number of times player got out: ")

# Do calculations
try:
    r = float(runs)
    b = int(balls) 
    o = int(outs)
    
    print("\nResults:")
    print("--------")
    
    # Batting average
    if o > 0:
        avg = r / o
        print(f"Batting Average: {avg:.2f}")
    else:
        print("Batting Average: N/A")
    
    # Strike rate
    if b > 0:
        sr = (r / b) * 100
        print(f"Strike Rate: {sr:.2f}")
    else:
        print("Strike Rate: N/A")
        
except:
    print("Enter correct numbers!")