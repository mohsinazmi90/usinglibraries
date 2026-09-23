"""
FILE: test_student_demo.py
RUN COMMAND: pytest test_student_demo.py -v
"""

import pytest

# ==============================================================================
# SECTION 1: THE APPLICATION CODE (What we want to test)
# ==============================================================================
# In a real job, this would be application logic or API calls.

def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

def divide(a: float, b: float) -> float:
    """Divides two numbers and raises an error if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


# ==============================================================================
# SECTION 2: BASIC TESTS (Native Python Assertions)
# ==============================================================================
# PyTest uses standard Python 'assert' statements—no heavy class structure needed.

def test_basic_addition():
    """Teaches basic verification using assert."""
    result = add(5, 5)
    assert result == 10, "5 + 5 should equal 10"


def test_divide_by_zero_exception():
    """Teaches how an SDET verifies that bad inputs fail safely."""
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    
    # Asserting the error message matches expectation
    assert "Cannot divide by zero!" in str(exc_info.value)


# ==============================================================================
# SECTION 3: FIXTURES (Setup & Teardown)
# ==============================================================================
# Fixtures teach students how SDETs set up test environment/data before running tests.

@pytest.fixture
def student_database_record():
    """Simulates creating a test record in a database before a test runs."""
    # STEP 1: Setup test data
    record = {"student_id": 101, "name": "Alex", "course": "Python SDET", "grade": "A"}
    
    yield record  # Provide data to the test function
    
    # STEP 2: Teardown (runs automatically after the test finishes)
    record.clear()


def test_student_data_validation(student_database_record):
    """PyTest automatically injects the fixture 'student_database_record' as an argument."""
    assert student_database_record["course"] == "Python SDET"
    assert student_database_record["grade"] in ["A", "B", "C"]


# ==============================================================================
# SECTION 4: PARAMETRIZATION (Data-Driven Testing)
# ==============================================================================
# Teaches running 1 test function against multiple datasets to avoid duplicate code.

@pytest.mark.parametrize("input_a, input_b, expected_sum", [
    (1, 2, 3),        # Test Case 1: Positive numbers
    (-5, 5, 0),       # Test Case 2: Negative and positive
    (0, 0, 0),        # Test Case 3: Zeros
    (100, 200, 300)   # Test Case 4: Larger numbers
])
def test_addition_data_driven(input_a, input_b, expected_sum):
    """Runs 4 separate test passes dynamically using the parameterized values."""
    assert add(input_a, input_b) == expected_sum