"""*args / **kwargs: 4 HackerRank-style problems (W2 Python interview Qs).

Run all sample + hidden tests (like HackerRank's "Submit"):
    uv run python drill/python-qs/args_kwargs.py
Run one problem on your own input (like "Custom input"):
    uv run python drill/python-qs/args_kwargs.py 3 < my_input.txt

Only write code where it says TODO. Hidden tests show Passed/Failed only.

------------------------------------------------------------------------
Problem 1: Flexible Sum (Easy)
Write total(*nums) that returns the sum of any number of integers (0 if none).
Input:  first line q, then q lines of space-separated integers (a line may be empty).
Output: one sum per line.
Sample input        Sample output
3                   6
1 2 3               0
                    6
10 -4

------------------------------------------------------------------------
Problem 2: Config Builder (Easy)
Write describe(**info) that returns "key=value" pairs joined by ", " in the
order they were given, or "(empty)" if there are none.
Input:  first line q, then q lines of space-separated key=value tokens.
Output: describe(...) for each line.
Sample input                         Sample output
2                                    name=Deepak, role=AI
name=Deepak role=AI                  model=gpt, temperature=0.2, stream=true
model=gpt temperature=0.2 stream=true

------------------------------------------------------------------------
Problem 3: Model Call Router (Medium)
Write call_model(prompt, *stop, temperature=0.0, **extra) that returns
    "prompt=<p> | stop=<a,b or -> | temperature=<float> | extra=<k:v,k:v or ->"
AND write the parsing in solve_3: each line is a prompt word, then tokens.
Tokens without "=" are stop words; "temperature=x" is a float; any other
"k=v" goes into extra (value stays a string). Call it with * and ** unpacking.
Sample input                               Sample output
3                                          prompt=hi | stop=END,STOP | temperature=0.5 | extra=top_p:0.9
hi END STOP temperature=0.5 top_p=0.9      prompt=summarise | stop=- | temperature=0.0 | extra=-
summarise                                  prompt=explain | stop=NL | temperature=0.0 | extra=max_tokens:100
explain max_tokens=100 NL

------------------------------------------------------------------------
Problem 4: Call Logger (Medium)
Write log_calls(func): return a wrapper that takes any *args/**kwargs, prints
    CALL <name>(<args as repr>, <k=repr(v)>)
then returns func's result unchanged. (Every decorator is built like this.)
Sample input              Sample output
3                         CALL add(2, 3)
add 2 3                   5
greet Deepak              CALL greet('Deepak')
greet Sam greeting=Hi     Hello, Deepak!
                          CALL greet('Sam', greeting='Hi')
                          Hi, Sam!

Afterwards, out loud (60 s each): what types are args and kwargs inside the
function? Why does a wrapper need both? Why is f(prompt="x", "END") a SyntaxError?
"""

import io
import sys
from contextlib import redirect_stdout


# ---------- Problem 1 ----------
def total(*nums):
# Problem 1: Flexible Sum (Easy)
# Write total(*nums) that returns the sum of any number of integers (0 if none).
# Input:  first line q, then q lines of space-separated integers (a line may be empty).
# Output: one sum per line.
# Sample input        Sample output
# 3                   6
# 1 2 3               0
#                     6
   if nums is not None:
       return sum(nums)
   return None
    


def solve_1(lines):
    q = int(lines[0])
    for line in lines[1:1 + q]:
        print(total(*map(int, line.split())))


# ---------- Problem 2 ----------
def describe(**info):
   '''
   Problem 2: Config Builder (Easy)
   Write describe(**info) that returns "key=value" pairs joined by ", " in the
   Input:  first line q, then q lines of space-separated key=value tokens.
   order they were given, or "(empty)" if there are none.
   Output: describe(...) for each line.
   Sample input                         Sample output
   2                                    name=Deepak, role=AI
   name=Deepak role=AI                  model=gpt, temperature=0.2, stream=true
   model=gpt temperature=0.2 stream=true
   '''
   if not info:
       return "(empty)"
   return (', ').join([f"{k}={v}" for k, v in info.items()]) or "(empty)"


def solve_2(lines):
    q = int(lines[0])
    for line in lines[1:1 + q]:
        info = dict(tok.split("=", 1) for tok in line.split())
        print(describe(**info))


# ---------- Problem 3 ----------
def call_model(prompt, *stop, temperature=0.0, **extra):
    '''
    Problem 3: Model Call Router (Medium)
Write call_model(prompt, *stop, temperature=0.0, **extra) that returns
    "prompt=<p> | stop=<a,b or -> | temperature=<float> | extra=<k:v,k:v or ->"
AND write the parsing in solve_3: each line is a prompt word, then tokens.
Tokens without "=" are stop words; "temperature=x" is a float; any other
"k=v" goes into extra (value stays a string). Call it with * and ** unpacking.
Sample input                               Sample output
3                                          prompt=hi | stop=END,STOP | temperature=0.5 | extra=top_p:0.9
hi END STOP temperature=0.5 top_p=0.9      prompt=summarise | stop=- | temperature=0.0 | extra=-
summarise                                  prompt=explain | stop=NL | temperature=0.0 | extra=max_tokens:100
explain max_tokens=100 NL
    '''
    stop_txt = ",".join(stop) or "-"
    extra_txt = ",".join(f"{k}:{v}" for k, v in extra.items()) or "-"
    return f"prompt={prompt} | stop={stop_txt} | temperature={temperature} | extra={extra_txt}"

def solve_3(lines):
    q = int(lines[0])
    for line in lines[1:1 + q]:
        prompt, *toks = line.split()
        stops = [t for t in toks if "=" not in t]
        options = dict(t.split("=", 1) for t in toks if "=" in t)
        if "temperature" in options:
            options["temperature"] = float(options["temperature"])
        print(call_model(prompt, *stops, **options))

# ---------- Problem 4 ----------
def log_calls(func):
    '''
    Problem 4: Call Logger (Medium)
Write log_calls(func): return a wrapper that takes any *args/**kwargs, prints
    CALL <name>(<args as repr>, <k=repr(v)>)
then returns func's result unchanged. (Every decorator is built like this.)
Sample input              Sample output
3                         CALL add(2, 3)
add 2 3                   5
greet Deepak              CALL greet('Deepak')
greet Sam greeting=Hi     Hello, Deepak!
                          CALL greet('Sam', greeting='Hi')
                          Hi, Sam!

Afterwards, out loud (60 s each): what types are args and kwargs inside the
function? Why does a wrapper need both? Why is f(prompt="x", "END") a SyntaxError?
    '''
    def wrapper(*args, **kwargs):
        parts = [repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()]
        print(f"CALL {func.__name__}({', '.join(parts)})")
        return func(*args, **kwargs)
    return wrapper


def add(a, b):
    return a + b


def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


def solve_4(lines):
    funcs = {"add": log_calls(add), "greet": log_calls(greet)}
    conv = lambda t: int(t) if t.lstrip("-").isdigit() else t
    q = int(lines[0])
    for line in lines[1:1 + q]:
        name, *toks = line.split()
        args = [conv(t) for t in toks if "=" not in t]
        kwargs = dict(t.split("=", 1) for t in toks if "=" in t)
        print(funcs[name](*args, **kwargs))


# ---------- test runner (don't edit) ----------
SOLVERS = {1: solve_1, 2: solve_2, 3: solve_3, 4: solve_4}
TESTS = {
    1: [("3\n1 2 3\n\n10 -4\n", "6\n0\n6"), ("1\n5\n", "5")],
    2: [("2\nname=Deepak role=AI\nmodel=gpt temperature=0.2 stream=true\n",
         "name=Deepak, role=AI\nmodel=gpt, temperature=0.2, stream=true"),
        ("1\n\n", "(empty)")],
    3: [("3\nhi END STOP temperature=0.5 top_p=0.9\nsummarise\nexplain max_tokens=100 NL\n",
         "prompt=hi | stop=END,STOP | temperature=0.5 | extra=top_p:0.9\n"
         "prompt=summarise | stop=- | temperature=0.0 | extra=-\n"
         "prompt=explain | stop=NL | temperature=0.0 | extra=max_tokens:100"),
        ("1\nq temperature=1 a b\n", "prompt=q | stop=a,b | temperature=1.0 | extra=-")],
    4: [("3\nadd 2 3\ngreet Deepak\ngreet Sam greeting=Hi\n",
         "CALL add(2, 3)\n5\nCALL greet('Deepak')\nHello, Deepak!\nCALL greet('Sam', greeting='Hi')\nHi, Sam!"),
        ("1\nadd 10 -4\n", "CALL add(10, -4)\n6")],
}


def run_tests():
    passed = 0
    for p, cases in TESTS.items():
        for i, (inp, want) in enumerate(cases):
            kind = "Sample" if i == 0 else "Hidden"
            buf = io.StringIO()
            try:
                with redirect_stdout(buf):
                    SOLVERS[p](inp.splitlines())
                got = buf.getvalue().strip()
            except Exception as e:
                got = f"{type(e).__name__}: {e}"
            ok = got == want
            passed += ok
            print(f"Problem {p} {kind}: {'Passed' if ok else 'Failed'}")
            if not ok and kind == "Sample":
                print(f"  expected:\n{want}\n  got:\n{got}")
    print(f"\n{passed}/{sum(len(c) for c in TESTS.values())} test cases passed")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        SOLVERS[int(sys.argv[1])](sys.stdin.read().splitlines())
    else:
        run_tests()
