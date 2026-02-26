# Gilded Rose starting position in Python

For exercise instructions see [top level README](../README.md)


## Gilded Rose Refactoring Kata – Python Implementation

This branch contains my short solution to the Gilded Rose Refactoring Kata implemented in Python.

## Overview

The task was approached as a legacy code refactoring exercise.
The goal was to safely introduce a new item ("Conjured Magic Hat") while improving readability and maintainability of the original implementation.

## Solution and the steps

1. Fixed the first failing test (intented).
2. Added unit tests to capture and verify expected behavior.
3. Implemented the new requirement for "Conjured Magic Hat" to the legacy code base.
4. Added the unit tests to support the new item.
4. Refactored the structure to:
   - Reduce nested conditionals
   - Fix the rules and logic to be more clearer (functions)
   - Support to add more items with new rules a bit easier
   - Still to work as expected even if refactored
   - Be more readable
5. Checked that previous unit tests still are OK
6. Added more unit tests to test the logic a bit better

## How to get started

```
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
``` 

## Run the unit tests from the Command-Line

```
python -m unittest
```

## About Approval / TextTest Regression Tests

The original kata repository includes TextTest-based approval (Golden Master) regression tests.

I did not do regression tests in my solution, only unit tests were used. However, below you can find how to proceed with the regression tests.

## Run the TextTest fixture from the Command-Line

For e.g. 10 days:

```
python texttest_fixture.py 10
```

You should make sure the command shown above works when you execute it in a terminal before trying to use TextTest (see below).


## Run the TextTest approval test that comes with this project

There are instructions in the [TextTest Readme](../texttests/README.md) for setting up TextTest. You will need to specify the Python executable and interpreter in [config.gr](../texttests/config.gr). Uncomment these lines:

    executable:${TEXTTEST_HOME}/python/texttest_fixture.py
    interpreter:python

## Run the ApprovalTests.Python test

This test uses the framework [ApprovalTests.Python](https://github.com/approvals/ApprovalTests.Python). You will need to install  Run it like this:

```
python tests/test_gilded_rose_approvals.py
```

You will need to approve the output file which appears under "approved_files" by renaming it from xxx.received.txt to xxx.approved.txt.
