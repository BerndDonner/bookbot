import time

import pytest
from main import find_last_name

run_cases = [
    pytest.param(100000, "John", "Doe", "Doe99999"),
    pytest.param(150000, "Lane", "Wagner", "Wagner149999"),
]

submit_cases = [
    pytest.param(200000, "Key", "Error", None, marks=pytest.mark.submit),
    pytest.param(250000, "Chad", "Energy", "Energy249999", marks=pytest.mark.submit),
    pytest.param(
        300000,
        "Tiffany",
        "Johnson",
        "Johnson299999",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("complexity", "first_name", "last_name", "expected_output"),
    run_cases + submit_cases,
)
def test_find_last_name(complexity, first_name, last_name, expected_output):
    names_dict = get_name_dict(first_name, last_name, complexity)
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * first_name: {first_name}")
    print(
        f"Expected:  {expected_output} & 50 lookups completed in less than 50 milliseconds"
    )
    if last_name == "Error":
        first_name_key = first_name
    else:
        first_name_key = f"{first_name}{complexity - 1}"
    start = time.time()
    for _ in range(50):
        result = find_last_name(names_dict, first_name_key)
    elapsed = time.time() - start
    timeout = 0.05
    if elapsed < timeout:
        print(f"50 lookups completed in less than {timeout * 1000} milliseconds!")
    else:
        print(f"50 lookups took too long ({elapsed * 1000} milliseconds). Speed it up!")
    print(f"Actual: {result}")
    assert elapsed < timeout
    assert result == expected_output


def get_name_dict(first_name, last_name, num):
    names = {}
    for i in range(num):
        names[f"{first_name}{i}"] = f"{last_name}{i}"
    return names

