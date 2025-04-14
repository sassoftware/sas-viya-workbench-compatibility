# SAS Viya Workbench Third-Party Package Validation

The `sas-viya-workbench-compatibility` package validation harness compares versions of dependencies to ensure they work in SAS Viya Workbench.

Users specify dependencies for which they wish to determine compatibility with SAS Viya Workbench.
The program runs a battery of tests against all listed versions of that dependency and furnishes a report on overall compatibility, compiled into an easy-to-read `compatible_packages.md` file.

The program runs against each dependency in isolation, with the rest of the built-in packages of Workbench still present on the system.

## Installation and Use

> [!WARNING]
> The default disk quota of 5 GB is not enough to run this application.
If you receive out-of-memory errors, delete the python files in `/workspaces/myfolder/.user-python-packages` to return to Workbench's original state.

In Workbench, clone this repo then run:

```
cd sas-viya-workbench-compatibility
pip install -i requirements.txt
run-tests.py
```

As the tests run, they generate a large amount of output.
Users can view results by looking at the resulting `goodlist.md`.
The chart will indicate which packages were able to be installed, which packages had passing or failing states, and which packages posed any security issues.
Users curious about the specific reasons why a test passed or failed can scroll through the output to see the specific error or failure.

## Adding New Packages

To add a new package to the validation system, create a subdirectory in `tests` named after the exact name of the package in pip.
This folder should include a file named `versions.txt` that includes a list of which versions should be tested.
Incorrectly named packages or versions will cause `INSTALL_FAILED` reports in the final results.

Next, create a file following the format `test_<anything>.py`.
This is a test file that contains correct python code.
All functions beginning with the prefix `test_` are test cases.
These should follow the convention of [pytest](https://docs.pytest.org/en/stable/contents.html) functions, including assertions for correctness.

Example (test_baseline.py):

```
def test_baseline():
    assert 2+2==4
```

A test file can contain as many tests as necessary to evaluate the package for completeness and correctness.
These should include successful importation in the Workbench environment, execution of its functionality in isolation, and execution of its functionality in concert with Viya procs.

## Contributing

Maintainers are accepting patches and contributions to this project.
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details about submitting contributions to this project.

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

## Known Compability Chart

| Package | Version | Installs | Validated¹ | Vulnerability Scan² |
| ------- | ------- | -------- | ---------- | ------------------- |
| Patterns | 0.3 | ✅ | ✅ | ✅ |
| **Pillow** | **11.2.0** | ✅ | ✅ | ✅ |
| amazon-textract-caller | 0.2.4 | ✅ | ✅ | ✅ |
| azure-ai-formrecognizer | 3.3.3 | ✅ | ✅ | ✅ |
| azure-cognitiveservices-vision-computervision | 0.9.1 | ✅ | ✅ | ✅ |
| azure-core | 1.32.0 | ✅ | ✅ | ✅ |
| boto3 | 1.37.24 | ✅ | ✅ | ✅ |
| corenlp | 0.0.14 | ✅ | ✅ | ✅ |
| dhash | 1.4 | ✅ | ✅ | ✅ |
| fastapi | 0.115.12 | ✅ | ✅ | ✅ |
| gradio | 5.23.2 | ✅ | ✅ | ✅ |
| gseapy | 1.1.8 | ✅ | ✅ | ✅ |
| hdbscan | 0.8.40 | ✅ | ✅ | ✅ |
| hnswlib | 0.8.0 | ❌ |  |  |
| imagehash | 4.3.2 | ✅ | ✅ | ✅ |
| img2pdf | 0.6.0 | ✅ | ✅ | ✅ |
| mmcv | 2.2.0 | ✅ | ✅ | ✅ |
| mmdet | 3.3.0 | ✅ | ✅ | ✅ |
| mysqlclient | 2.2.7 | ❌ |  |  |
| openTSNE | 1.0.2 | ✅ | ✅ | ✅ |
| openai | 1.70.0 | ✅ | ✅ | ✅ |
| opencv-python | 4.11.0.86 | ✅ | ✅ | ✅ |
| openpyxl | 3.1.5 | ✅ | ✅ | ✅ |
| pandas | 1.0.0 | ❌ |  |  |
| pandas | 2.0.0 | ✅ | ✅ | ✅ |
| pandas | 2.2.2 | ✅ | ✅ | ✅ |
| **pandas** | **2.2.3** | ✅ | ✅ | ✅ |
| pdf2image | 1.17.0 | ✅ | ✅ | ✅ |
| polyglot | 16.7.4 | ✅ | ✅ | ✅ |
| reportlab | 4.3.1 | ✅ | ✅ | ✅ |
| **requests** | **2.32.3** | ✅ | ✅ | ❌ |
| sanbomics | 0.1.0 | ✅ | ✅ | ✅ |
| **scikit-learn** | **1.3.0** | ✅ | ✅ | ❌ |
| scikit-learn | 1.4.0 | ✅ | ✅ | ❌ |
| scikit-learn | 1.5.0 | ✅ | ✅ | ✅ |
| scikit-learn | 1.5.2 | ✅ | ✅ | ✅ |
| **seaborn** | **0.13.2** | ✅ | ✅ | ✅ |
| shap | 0.47.1 | ✅ | ✅ | ✅ |
| shiny | 1.3.0 | ✅ | ✅ | ✅ |
| smote-variants | 1.0.1 | ✅ | ✅ | ✅ |
| spacy | 3.8.4 | ✅ | ✅ | ✅ |
| sqlalchemy | 2.0.40 | ✅ | ✅ | ✅ |
| streamlit | 1.44.0 | ✅ | ✅ | ✅ |
| sympy | 1.13.3 | ✅ | ✅ | ✅ |
| textblob | 0.19.0 | ✅ | ✅ | ✅ |
| toml | 0.10.2 | ✅ | ✅ | ✅ |
| torch | 2.6.0 | ✅ | ✅ | ✅ |
| tqdm | 4.67.1 | ✅ | ✅ | ✅ |
| transformers | 4.50.3 | ✅ | ✅ | ✅ |

¹: A component is "validated" if all of the tests in its respective test case folder run without any errors or failed assertions. It is possible that there are use cases not covered by the test cases, so compatibility is suggested, not guaranteed. If you encounter incompatibility when using a library, please report it so we can update our test cases!

²:  Vulnerability results pass if there are no high or critical CVEs for the component as of 2025-04-14 15:16:45 per the results of the scanning tool "pip-audit".