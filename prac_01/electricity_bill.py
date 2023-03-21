"""
price per kWh in cents,
daily use in kWh, and
number of days in the billing period.
"""

# 1
print("Electricity bill estimator")
price_per_kwh = float(input("Enter cents per kwh: ") )
daily_use_in_kwh = float(input("Enter daily use in kwh: ") )
num_of_days = int(input("Enter number of billing days: "))
estimated_bill = (price_per_kwh / 100) * daily_use_in_kwh * num_of_days
print(f"Estimated bill: ${estimated_bill: .2f}")


# test:
# Electricity bill estimator
# Enter cents per kwh: 35
# Enter daily use in kwh: 4.5
# Enter number of billing days: 90
# Estimated bill: $ 141.75


# 2
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_type = int(input("Which traiff? 11 or 31: "))
daily_use_in_kwh = float(input("Enter daily use in kwh: ") )
num_of_days = int(input("Enter number of billing days: "))
# calculate electricity bill according to different tariff_type
if tariff_type == 11:
    estimated_bill = TARIFF_11* daily_use_in_kwh * num_of_days
else:
    estimated_bill = TARIFF_31* daily_use_in_kwh * num_of_days
print(f"Estimated bill: ${estimated_bill:.2f}")


# test:
# Electricity bill estimator 2.0
# Which traiff? 11 or 31: 11
# Enter daily use in kwh: 13.4
# Enter number of billing days: 90
# Estimated bill: $295.01

# Electricity bill estimator 2.0
# Which traiff? 11 or 31: 31
# Enter daily use in kwh: 13.4
# Enter number of billing days: 90
# Estimated bill: $165.14