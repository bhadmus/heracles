'''
This code is expected to convert any number into a string.
If it is a floating point value,
it should round the number up to 2 decimal values then convert to a string
'''

# Prompt a user for a value
number = input('Please insert a number \n')


def formatMoney(number):
    '''
    :param number:
    :return: money_value (format result to string)
    '''
    if type(number) in (int, float):
        try:
            money_value = round(number, 2)
            return str(money_value)
        except Exception as e:
            ValueError('Invalid value with error', e)

    else:
        return TypeError(
            f'Invalid type of {type(number)} for {number}. Provide Integer or Float')


test = formatMoney(number)
print(test)