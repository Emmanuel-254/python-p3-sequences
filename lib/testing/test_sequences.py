import io
import sys
from sequences import print_fibonacci  # Import the function if it's in another file

def test_print_fibonacci_zero():
    captured_out = io.StringIO()
    sys.stdout = captured_out
    print_fibonacci(0)
    sys.stdout = sys.__stdout__
    assert(captured_out.getvalue() == '[]\n')

def test_print_fibonacci_one():
    captured_out = io.StringIO()
    sys.stdout = captured_out
    print_fibonacci(1)
    sys.stdout = sys.__stdout__
    assert(captured_out.getvalue() == '[0]\n')

def test_print_fibonacci_two():
    captured_out = io.StringIO()
    sys.stdout = captured_out
    print_fibonacci(2)
    sys.stdout = sys.__stdout__
    assert(captured_out.getvalue() == '[0, 1]\n')

def test_print_fibonacci_ten():
    captured_out = io.StringIO()
    sys.stdout = captured_out
    print_fibonacci(10)
    sys.stdout = sys.__stdout__
    assert(captured_out.getvalue() == '[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n')
