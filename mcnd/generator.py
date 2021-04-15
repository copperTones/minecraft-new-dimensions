import random

def set_seed(x):
    global seed
    seed = x
    random.seed(x)

set_seed(random.getrandbits(64))


def generate(gen, **kwargs):
    return globals()[gen](**kwargs) # call function named gen

def r_generate(obj):
    if type(obj) is dict:
        if 'gen' in obj:
            return generate(**obj)
        return {k: r_generate(v) for k, v in obj.items()}
    elif type(obj) is list:
        return [r_generate(x) for x in obj]
    else:
        return obj

## numeric
def int_uniform(min, max):
    return random.randint(min, max)

def float_uniform(min, max):
    return random.uniform(min, max)

def float_normal(mean, stdev):
    return random.gauss(mean, stdev)

## non-numeric
def enum(value):
    return random.choice(value)

def array(value, length=0):
    if type(length) is dict:
        length = generate(length)
    return [r_generate(value) for i in range(length)]

def optional(value, probability=.1):
    if random.random() < probability:
        return value

def rgb():
    return random.getrandbits(24)

def code(code, value):
    var = locals()
    var.update(globals())
    return eval(code, var)

def namespace(value):
    return 'random '+value

def dynamic_namespace(value):
    return namespace(value)

if __name__ == '__main__':
    from json import loads
    print(generate(**loads(input())))
