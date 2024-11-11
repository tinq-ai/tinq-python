# tinq.Tools
Official Tinq.ai python SDK
For help and support please check: https://docs.tinq.ai/sdks/python

All URIs are relative to *https://tinq.ai/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_text_from_file**](Tools.md#extract_text_from_file) | **POST** /extract-text | Extract text from file
[**extract_url**](Tools.md#extract_url) | **POST** /extract-article | Extract URL


# **extract_text_from_file**
> extract_text_from_file(content_type=content_type, accept=accept, input_file=input_file)

Extract text from file

This API endpoint allows users to upload a document file in one of the supported formats. The file can be sent either as `input_file`. The endpoint accepts various document types such as Word, PowerPoint, and PDF, and enforces a file size limit of 10 MB, and returns the text extracted from the document with no formatting.

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
    api_instance = tinq.Tools(api_client)
    content_type = 'application/json' # str |  (optional)
    accept = 'application/json' # str |  (optional)
    input_file = None # bytearray |  (optional)

    try:
        # Extract text from file
        api_instance.extract_text_from_file(content_type=content_type, accept=accept, input_file=input_file)
    except Exception as e:
        print("Exception when calling Tools->extract_text_from_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 
 **input_file** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_url**
> extract_url(content_type=content_type, accept=accept, extract_url=extract_url)

Extract URL

Article Extractor endpoint.  Please use the newer scraper/extract-article for more flexibility.

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
    api_instance = tinq.Tools(api_client)
    content_type = 'application/json' # str |  (optional)
    accept = 'application/json' # str |  (optional)
    extract_url = 'extract_url_example' # str |  (optional)

    try:
        # Extract URL
        api_instance.extract_url(content_type=content_type, accept=accept, extract_url=extract_url)
    except Exception as e:
        print("Exception when calling Tools->extract_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] 
 **accept** | **str**|  | [optional] 
 **extract_url** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

