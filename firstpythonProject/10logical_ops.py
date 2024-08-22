has_high_income = False
has_good_credit = True
has_ciminal_record = False
if has_high_income and has_good_credit: # or, not
    print("Eligible for loan")
elif has_good_credit and not has_ciminal_record:
    print("Still Eligible for loan")
else:
    print("Declined for loan")