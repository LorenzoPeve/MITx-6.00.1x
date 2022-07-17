
def fancy_divide(numbers,index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        print("-1")
    else:
        print("1")
    finally:
        print("0")


# fancy_divide([0, 2, 4], 1) # 1,0
# fancy_divide([0, 2, 4], 4) #, -1,0
# fancy_divide([0, 2, 4], 0) # 0, 'error'


def fancy_divide(numbers, index):
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError:
        fancy_divide(numbers, len(numbers) - 1)
    except ZeroDivisionError:
        print("-2")
    else:
        print("1")
    finally:
        print("0")

# fancy_divide([0, 2, 4], 1) # 1,0
# fancy_divide([0, 2, 4], 4) #, 1, 0, 0 
# fancy_divide([0, 2, 4], 0) # -2, 0 

def fancy_divide2(numbers, index):
    print(f"On entry index is {index}", flush=True)
    try:
        denom = numbers[index]
        print("Try", index, denom)
    except IndexError:
        fancy_divide2(numbers, index-1)
    else:
        print("Else", "1")
    finally:
        print("Finally", "0", f"index = {index}")

# fancy_divide2([0, 2, 4], 6)


def raise_2nd_exception():
    try:
        pass

    except IndexError:
        print('in except')
        raise ValueError("Exception in except IE")
    else:
        print('in else')
        raise KeyError("Exception in else")
    finally:
        print("***### Finally ###***")
        print("then it will reraise unhandled or 2nd exception unless there is")
        print("an exception in the finally clause\n")

    
# raise_2nd_exception()
print('Outside')


def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        except IndexError:
            pass
        # finally:
        #     denom = list_of_numbers[index]
        #     for i in range(len(list_of_numbers)):
        #         list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)


# fancy_divide([0, 2, 4], 0)


def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"

    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
        
    return numbers

# normalize([0, 0, 0])

def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')