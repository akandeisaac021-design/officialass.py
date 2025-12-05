speed =int(input("Enter speed: "))
acceleration =int(input("Enter airplane acceleretion: "))
speedsqr =speed**2
doubled_acceleration =acceleration*2
runway_length =speedsqr/doubled_acceleration
print(runway_length)
