# Workbench Third-Party Package Validation

The `sas-viya-workbench-compatibility` package validation harness is used to compare versions of dependencies in workbench to ensure they work. For each dependency under observation, a battery of tests will be run against all listed versions of that dependency. Note that these will be run against that dependency in isolation with the rest of the built-in packages of workbench still present on the system. Output is compiled into an easy-to-read `compatible_packages.md` file.

## Installation and Use

NOTE: The default disk quota of 5 GB is not enough to run this application. If you receive out-of-memory errors, delete the python files in `/workspaces/myfolder/.user-python-packages` to get back to the workbench original state.

In workbench, clone this repo then run:

```
cd sas-viya-workbench-compatibility
pip install -i requirements.txt
run-tests.py
```

There will be a large amount of output as the tests run, and the results can be viewed by looking at the resulting `goodlist.md`.  The chart will indicate which packages were able to be installed, which packages had passing or failing states, and which packages had any security issues. If you are curious about the specific reasons why a test passed or failed, you can scroll through the output to see the specific error or failure.

## How to add new packages

To add a new package to the validation system, create a subdirectory in `tests` named after the exact name of the package in pip. This folder should include a file named `versions.txt` that includes a list of which versions should be tested. Incorrectly named packages or versions will cause INSTALL_FAILED reports in the final results.

Next, create a file following the format `test_<anything>.py`. This is a test file that contains correct python code. All functions beginning with the prefix `test_` are test cases. These should be written following the convention of [pytest](https://docs.pytest.org/en/stable/contents.html) functions, including assertions for correctness.

Example (test_baseline.py):

```
def test_baseline():
    assert 2+2==4
```

A test file can contain as many tests as necessary to evaluate the package for completeness and correctness. These should include successful importation in the workbench environment, execution of its functionality in isolation, and execution of its functionality in concert with Viya procs.


## Contributing

Maintainers are accepting patches and contributions to this project.
Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details about submitting contributions to this project.

## License

This project is licensed under the [Apache 2.0 License](LICENSE).

## Known Compability Chart

| Python| Dependency | Version | Installs | Validated | Vulnerability Scan |
| -------- | ------- | ------- | ------- | ------- |
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
