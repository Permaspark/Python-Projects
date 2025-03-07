# Taking all inputs in a single line and splitting them into parts
input_values = input("Enter wages, taxable interest, unemployment compensation, status, and taxes withheld (separated by spaces): ")

# Split the input into individual components
input_wage, taxable_interest, unemployment_compensation, marriage_status, taxes_withheld = map(int, input_values.split())

# Calculate AGI
AGI = input_wage + taxable_interest + unemployment_compensation
print(f'AGI: ${AGI:,}')

# Check for high income error
if AGI >= 120000:
    print('Error: Income too high to use this form')

# Determine deduction based on marriage status
if marriage_status == 1:
    status_deduction = 12000
elif marriage_status == 2:
    status_deduction = 24000
else:
    status_deduction = 12000

print(f'Deduction: ${status_deduction:,}')

# Calculate taxable income
taxable_income = AGI - status_deduction
if taxable_income < 0:
    taxable_income = 0
print(f'Taxable Income: ${taxable_income:,}')

# Calculate federal tax based on marriage status and taxable income
if marriage_status == 1 and taxable_income <= 10000:
    federal_tax = taxable_income * 0.10
elif marriage_status == 1 and 10001 <= taxable_income <= 40000:
    federal_tax = 1000 + (taxable_income - 10000) * 0.12
elif marriage_status == 1 and 40001 <= taxable_income <= 85000:
    federal_tax = 4600 + (taxable_income - 40000) * 0.22
elif marriage_status == 1 and taxable_income > 85000:
    federal_tax = 14500 + (taxable_income - 85000) * 0.24
elif marriage_status == 2 and taxable_income <= 20000:
    federal_tax = taxable_income * 0.10
elif marriage_status == 2 and 20001 <= taxable_income <= 80000:
    federal_tax = 2000 + (taxable_income - 20000) * 0.12
elif marriage_status == 2 and taxable_income > 80000:
    federal_tax = 9200 + (taxable_income - 80000) * 0.22
else:
    # Default in case marriage_status or taxable_income fall through all other conditions
    federal_tax = 0
    print("Warning: Tax status or income level unhandled")

# Round federal tax to nearest whole number
federal_tax = round(federal_tax)
print(f'Federal Tax: ${federal_tax:,}')

# Calculate tax due or refund
tax_due = federal_tax - taxes_withheld

if tax_due < 0:
    tax_refund = abs(tax_due)
    print(f'Tax Refund: ${tax_refund:,}')
else:
    print(f'Tax Due: ${tax_due:,}')
