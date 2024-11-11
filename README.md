# tinq

- API version: v2
- Package version: 0.2.0

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/tinq-ai/tinq-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/tinq-ai/tinq-python.git`)

Then import the package:
```python
import tinq
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tinq
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import tinq
from tinq.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tinq.ai/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = tinq.Configuration(
    host = "https://tinq.ai/api/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = tinq.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with tinq.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tinq.Assistant(api_client)
    accept_charset = 'UTF-8' # str |  (optional)
    content_type = 'application/json' # str |  (optional)
    accept = 'application/json' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Generate
        api_instance.generate(accept_charset=accept_charset, content_type=content_type, accept=accept, body=body)
    except ApiException as e:
        print("Exception when calling Assistant->generate: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://tinq.ai/api/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*Assistant* | [**generate**](docs/Assistant.md#generate) | **POST** /assistant | Generate
*Classifiers* | [**classifiers**](docs/Classifiers.md#classifiers) | **GET** /classifiers | Classifiers
*Classifiers* | [**classify**](docs/Classifiers.md#classify) | **POST** /classify | Classify
*Classifiers* | [**sentiment_analysis**](docs/Classifiers.md#sentiment_analysis) | **POST** /sentiment-analysis | Sentiment Analysis
*PlagiarismChecker* | [**check_plagiarism**](docs/PlagiarismChecker.md#check_plagiarism) | **POST** /check-plagiarism | Check Plagiarism
*Projects* | [**create_project**](docs/Projects.md#create_project) | **POST** /projects | Create Project
*Projects* | [**get_all_projects**](docs/Projects.md#get_all_projects) | **GET** /projects/ | Get All Projects
*Projects* | [**get_project**](docs/Projects.md#get_project) | **GET** /projects/{project} | Get Project
*Projects* | [**update_project**](docs/Projects.md#update_project) | **PUT** /projects/{project} | Update Project
*Scraper* | [**extract_article**](docs/Scraper.md#extract_article) | **POST** /scraper/extract-article | Extract article
*Scraper* | [**google_search**](docs/Scraper.md#google_search) | **POST** /scraper/google | Google Search
*Scraper* | [**scrape**](docs/Scraper.md#scrape) | **POST** /scraper/scrape | Scrape
*Tools* | [**extract_text_from_file**](docs/Tools.md#extract_text_from_file) | **POST** /extract-text | Extract text from file
*Tools* | [**extract_url**](docs/Tools.md#extract_url) | **POST** /extract-article | Extract URL
*Workflows* | [**create_workflow**](docs/Workflows.md#create_workflow) | **POST** /workflows | Create workflow
*Workflows* | [**execute_workflow**](docs/Workflows.md#execute_workflow) | **POST** /workflows/{workflow_slug}/execute | Execute workflow
*Workflows* | [**get_one_workflow**](docs/Workflows.md#get_one_workflow) | **GET** /workflows/{workflow_slug} | Get one workflow
*Workflows* | [**get_workflows**](docs/Workflows.md#get_workflows) | **GET** /workflows | Get workflows


## Documentation For Models



<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication


## Author

boulama@tinq.ai


