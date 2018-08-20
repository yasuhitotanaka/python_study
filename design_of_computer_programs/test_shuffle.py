def timecall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1 - t0, result


def timecalls(n, fn, *args):
    "Call function n times with args; return the min, avg and max time."
    if isinstance(n, int):
        times = [timecall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timecall(fn, *args)[0])
    return min(times), average(times), min(times)


def average(numbers):
    "Return the avearge (arithmetric mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))


def all_ints():
    # "Generate integers in the order 0,+1,-1,+2,-2,+3,-3", ..
    yield 0
    # ints(1) is a function to inifinitly generate positive numbers
    for i in ints(1):
        yield +i
        yield -i

def all_ints2():
    # "Generate integers in the order 0,+1,-1,+2,-2,+3,-3", ..
    yield 0
    i = 1
    # ints(1) is a function to inifinitly generate positive numbers
    while True:
        yield +i
        yield -i
        i += 1

import string, re, itertools

def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    # Your code here
    for f in fill_in(formula):
        if valid(f):
            return f


def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    for digits in itertools.permutations('1234567890',len(letters)):
        table = string.maketrans(letters,''.join(digits))
        yield formula.translate(table)

def valid(f):
    "Formula f is valid if f it has no numbers with leading zero, and evals zero. "
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False



def fill_in2(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    f, letters = compile_formula(formula)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0),len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters,''.join(digits))
                return formula.translate(table)
        except ArithmeticError:
            pass


def compile_formula(formula, verbose=False):
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s' % (params, body)
    if verbose: print(f)
    return eval(f), letters

#  string '012' => int 10. why? '01' = 8, 1970 C lang history.
#  that's taking up about 47 seconds out of our 75 seconds or about 63% of our time.

def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                 for (i,d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word
