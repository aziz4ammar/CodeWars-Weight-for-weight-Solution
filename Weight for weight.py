def order_weight(strng):
    wg = strng.split()
    
    def sum_of_digits(wg):
        return sum(int(digit) for digit in wg)
    
    sorted_weights = sorted(wg, key=lambda w: (sum_of_digits(w), w))
    
    return ' '.join(sorted_weights)