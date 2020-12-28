x = int(input ("Enter a number for divisor\n"))
numbers = list (range (1, x+1))
divisors_list = []
for number in numbers:
    if x % number == 0 :
        divisors_list.append(number)
print ("{} is divisor by {}".format(x,divisors_list))

