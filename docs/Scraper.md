# tinq.Scraper
Official Tinq.ai python SDK
For help and support please check: https://docs.tinq.ai/sdks/python

All URIs are relative to *https://tinq.ai/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_article**](Scraper.md#extract_article) | **POST** /scraper/extract-article | Extract article
[**google_search**](Scraper.md#google_search) | **POST** /scraper/google | Google Search
[**scrape**](Scraper.md#scrape) | **POST** /scraper/scrape | Scrape


# **extract_article**
> extract_article(accept=accept, body=body)

Extract article

### Example

* Bearer Authentication (bearerAuth):

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
    api_instance = tinq.Scraper(api_client)
    accept = 'application/json' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Extract article
        api_instance.extract_article(accept=accept, body=body)
    except Exception as e:
        print("Exception when calling Scraper->extract_article: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **google_search**
> google_search(accept=accept, body=body)

Google Search

### Example

* Bearer Authentication (bearerAuth):

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
    api_instance = tinq.Scraper(api_client)
    accept = 'application/json' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Google Search
        api_instance.google_search(accept=accept, body=body)
    except Exception as e:
        print("Exception when calling Scraper->google_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scrape**
> scrape(accept=accept, body=body)

Scrape

### Example

* Bearer Authentication (bearerAuth):

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
    api_instance = tinq.Scraper(api_client)
    accept = 'application/json' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Scrape
        api_instance.scrape(accept=accept, body=body)
    except Exception as e:
        print("Exception when calling Scraper->scrape: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | [optional] 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

