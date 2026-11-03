'''
Write a Python program that prompts the user to enter the price of petrol per litre in SEK and the number of litres of petrol they want to purchase. The program should then ask for the current USD to SEK exchange rate.

Using this information, the program should calculate the price of petrol per gallon (where 1 gallon is equal to 3.78541 litres). It should also calculate the total cost in SEK for the amount of fuel and convert it into USD based on the exchange rate. Finally, the program should print a statement indicating the total cost in both SEK and USD, as well as the equivalent number of gallons.

For example, if the user enters a price of 21.50 SEK per litre and requests 50 litres of petrol, the program should state the total cost in both SEK and USD and indicate how many gallons that amount of fuel is equivalent to. See an example below

Enter the price of petrol per litre (in SEK):  21.50
Enter the amount of petrol (in litres):  50
Enter the USD to SEK exchange rate:  10.53

--- Fuel Cost Calculation ---
50.00 litres at the price of 21.50 SEK per litre
is equivalent to 102.09 USD and 13.21 gallons.
Total cost in SEK: 1075.00 SEK
'''

# Code Start
price_per_litre = float(input('Enter the price of petrol per litre (in SEK): '))
litres = float(input('Enter the amount of petrol (in litres): '))
usd_to_sek_rate = float(input('Enter the USD to SEK exchange rate: '))

gallons = litres / 3.78541
total_sek = litres * price_per_litre
total_usd = total_sek / usd_to_sek_rate

print()
print('--- Fuel Cost Calculation ---')
print(round(litres, 2), ' litres at the price of ', round(price_per_litre, 2), 'is equivalent to ', round(total_usd, 2), ' USD and ', round(gallons, 2), 'gallons.')
print('Total cost in SEK: ', round(total_sek, 2), 'SEK')