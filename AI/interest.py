# interest.py
def calculate_compound_interest():
    try:
        p = float(input("Enter principal: "))
        r = float(input("Enter rate (%): "))
        t = int(input("Enter time (years): "))
        total = p * (1 + r/100) ** t
        print(f"Amount after {t} years: ₹{round(total, 2)}")
    except:
        print("Invalid input.")
