def feedbackShift(bits):
    xor_result = (bits[1] + bits[2]) % 2
    output = bits.pop()
    bits.insert(0, xor_result)
    return bits, output


def feedbackShiftList(bits_this):
    bits_output = [bits_this.copy()]
    random_output = []
    bits_next = bits_this.copy()
    while (len(bits_output) < 2**len(bits_this)):
        bits_next, next = feedbackShift(bits_next)
        bits_output.append(bits_next.copy())
        random_output.append(next)
    return bits_output, random_output


bitslist = feedbackShiftList([1, 1, 1])[0]
print(bitslist)
pseudorandom_bits = feedbackShiftList([1, 1, 1])[1]
print(pseudorandom_bits)