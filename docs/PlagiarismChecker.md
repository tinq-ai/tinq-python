# tinq.PlagiarismChecker
Official Tinq.ai python SDK
For help and support please check: https://docs.tinq.ai/sdks/python

All URIs are relative to *https://tinq.ai/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_plagiarism**](PlagiarismChecker.md#check_plagiarism) | **POST** /check-plagiarism | Check Plagiarism


# **check_plagiarism**
> check_plagiarism(content_type=content_type, body=body)

Check Plagiarism

Plagiarism checker

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
    api_instance = tinq.PlagiarismChecker(api_client)
    content_type = 'application/json' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Check Plagiarism
        api_instance.check_plagiarism(content_type=content_type, body=body)
    except Exception as e:
        print("Exception when calling PlagiarismChecker->check_plagiarism: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

