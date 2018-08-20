def longest_subpalindrome_slice(text):
    "Return (i,j) such that text[i:j] is the longest palindrome in text."
    if text == '': return (0,0)
    def length(slice): a,b = slice; return b-a
    candidates = [grow(text, start, end)
                  for start in range(len(text))
                  for end in (start, start+1)]
    return max(candidates, key=length)

def grow(text, start, end):
    "Start with a 0- or 1- length palindrome; try to grow a bigger one."
    while(start > 0 and end < len(text)
        and text[start-1].upper() == text[end].upper()):
        start -= 1; end += 1
        return (start, end)

def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == L('Racecar') == L('RacecarX') == (0, 7)



statwithに与える引数xはtupleでも、実行可能
text = 'abcde'
x = ('a', 'b')
set([text[1:]]) if text.startswith(x) else null

def match(pattern, text):
    "Match pattern against start of text; return longest match found or None."
    remainders = pattern(text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text) - len(shortest)]

def lit(s): return lambda t: set([t[len(s):]]) if t.startswith(s) else None
def seq(x, y): return lambda t: set().union(*map(y, x(t)))
def alt(x, y): return lambda t: x(t) | y(t)
def oneof(chars): return lambda t: set([t[1:]]) if (t and t[0] in chars) else None
dot = lambda t: set([t[1:]]) if t else None
eol = lambda t: set(['']) if t == '' else None

def star(x): return lambda t: (set([t]) |
                               set(t2 for t1 in x(t) if t1 != t
                                   for t2 in star(x)(t1)))
def test():
    assert match(star(lit('a')), 'aaaaabbbaa') == 'aaaaa'
    assert match(lit('hello'), 'hello how are you?') == 'hello'
    assert match(lit('x'), 'hello how are you?') == None
    assert match(oneof('xyz'), 'x**2 + y**2 = r**2') == 'x'
    assert match(oneof('xyz'), '   x is here!') == None
    return 'tests pass'

test()

immutableなリスト形式 tuple. frozenlistしか、hash化できない
    

