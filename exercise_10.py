flight = int(input('enter your flight number'))
airline = str(input('enter the name of your airline in Russian'))
airline_eng = str(input('enter the name of your airline in English'))
departure = str(input('enter the departure city in Russian'))
departure_eng = str(input('enter the departure city in English'))
print(f'Заканчивается посадка на рейс {flight}  {airline} до {departure}')
print(f'This is the final boarding call for {airline_eng} flight {flight} to {departure_eng }' )