# Workbench Third-Party Package Validation

The `sas-viya-workbench-compatibility` package validation harness is used to compare versions of dependencies in workbench to ensure they work. For each dependency under observation, a battery of tests will be run against all listed versions of that dependency. Note that these will be run against that dependency in isolation with the rest of the built-in packages of workbench still present on the system. Output is compiled into a comprehensive `compatible_packages.csv` file.

## How to use

In workbench, clone this repo then run:

```
pip install -i requirements.txt
run-tests.py
```

There will be a large amount of output as the tests run. At the end, a list of "final results" chart will be presented with certain codes.

 * INSTALL_FAILED: The package was unable to be installed. Run `pip install` manually to identify the source of the error.
 * TESTS_PASSED: The install was successful, and all tests passed
 * TESTS_FAILED: The install was successful, but some tests failed. You can scroll back in the console to find the details
 * UNINSTALL_FAILED: The uninstall failed for some reason. This is usually because it is the built-in version on workbench, which can not be removed, and is informational in nature.
 * VULNERABILITIES_FOUND: `pip-audit` found known vulnerabilities in the package and version specified. If a newer version is available with no vulnerabilities, it should be used instead.

## How to add new packages

To add a new package to the validation system, create a subdirectory in `tests` named after the exact name of the package in pip. This folder should include a file named `versions.txt` that includes a list of which versions should be tested. Incorrectly named packages or versions will cause INSTALL_FAILED reports in the final results.

Next, create a file following the format `test_<anything>.py`. This is a test file that contains correct python code. All functions beginning with the prefix `test_` are test cases. These should be written following the convention of [pytest](https://docs.pytest.org/en/stable/contents.html) functions, including assertions for correctness.

Example (test_pandas.py):

```
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
```

A test file can contain as many tests as necessary to evaluate the package for completeness and correctness. These should include successful importation in the workbench environment, execution of its functionality in isolation, and execution of its functionality in concert with Viya procs.

## Known Compability Chart

### Python
| Package Name | Version |
|------|----|
| pandas | 2.2.2 | 
| pandas | 2.2.1 | 