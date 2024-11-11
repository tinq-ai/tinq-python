# tinq.Classifiers
Official Tinq.ai python SDK
For help and support please check: https://docs.tinq.ai/sdks/python

All URIs are relative to *https://tinq.ai/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classifiers**](Classifiers.md#classifiers) | **GET** /classifiers | Classifiers
[**classify**](Classifiers.md#classify) | **POST** /classify | Classify
[**sentiment_analysis**](Classifiers.md#sentiment_analysis) | **POST** /sentiment-analysis | Sentiment Analysis


# **classifiers**
> classifiers()

Classifiers

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
    api_instance = tinq.Classifiers(api_client)

    try:
        # Classifiers
        api_instance.classifiers()
    except Exception as e:
        print("Exception when calling Classifiers->classifiers: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **classify**
> classify(accept=accept, content_type=content_type, body=body)

Classify

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
    api_instance = tinq.Classifiers(api_client)
    accept = 'application/json' # str |  (optional)
    content_type = 'application/json' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Classify
        api_instance.classify(accept=accept, content_type=content_type, body=body)
    except Exception as e:
        print("Exception when calling Classifiers->classify: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 
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

# **sentiment_analysis**
> sentiment_analysis(content_type=content_type, accept=accept, body=body)

Sentiment Analysis

Sentiment analysis API

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
    api_instance = tinq.Classifiers(api_client)
    content_type = 'application/json' # str |  (optional)
    accept = 'application/json' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Sentiment Analysis
        api_instance.sentiment_analysis(content_type=content_type, accept=accept, body=body)
    except Exception as e:
        print("Exception when calling Classifiers->sentiment_analysis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] 
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

