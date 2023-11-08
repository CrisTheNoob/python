print('Welcome to the tip calculator')
client =  float(input('What is your total bill? $'))
tip = int(input('How much tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the billl?'))

percent = client / 100
tip_bill = percent * tip
total_bill = tip_bill / people

print(f'the total bill is ${total_bill}')