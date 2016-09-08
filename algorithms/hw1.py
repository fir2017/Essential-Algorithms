number = raw_input('Enter your numbers:')
list_ = number.split()

numbersInt = map(int, list_)

print 'Max', max(numbersInt)
print 'Min', min(numbersInt)
print 'Average', float(sum(numbersInt))/len(numbersInt) if len(numbersInt) > 0 else float('nan')
