
def CreateEquation(Koefficients):
    result = ''
    size = len(Koefficients)
    for i in range(size):
        current = Koefficients[i]
        if(current != 0):
            if i > 0:
                if i == 1:
                    result =  'x' + result    
                else:
                    result =  'x**' + str(i) + result
            if not current in {1, -1} or i == 0:
                result = str(current).replace('-', '') + result
            if i < size - 1:
                if current > 0:
                    result = '+' + result
                else:
                    result = '-' + result   
            elif i == size - 1 and current < 0:   
                result = '-' + result   
    result = result[0] + result[1:].replace('+', ' + ').replace('-', ' + ')
    return result