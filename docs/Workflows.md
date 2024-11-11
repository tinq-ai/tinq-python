# tinq.Workflows
Official Tinq.ai python SDK
For help and support please check: https://docs.tinq.ai/sdks/python

All URIs are relative to *https://tinq.ai/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_workflow**](Workflows.md#create_workflow) | **POST** /workflows | Create workflow
[**execute_workflow**](Workflows.md#execute_workflow) | **POST** /workflows/{workflow_slug}/execute | Execute workflow
[**get_one_workflow**](Workflows.md#get_one_workflow) | **GET** /workflows/{workflow_slug} | Get one workflow
[**get_workflows**](Workflows.md#get_workflows) | **GET** /workflows | Get workflows


# **create_workflow**
> create_workflow(content_type=content_type, accept=accept, body=body)

Create workflow

Create a workflow.

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
    api_instance = tinq.Workflows(api_client)
    content_type = 'application/json' # str |  (optional)
    accept = 'application/json' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Create workflow
        api_instance.create_workflow(content_type=content_type, accept=accept, body=body)
    except Exception as e:
        print("Exception when calling Workflows->create_workflow: %s\n" % e)
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

# **execute_workflow**
> execute_workflow(workflow_slug, content_type=content_type, accept=accept, body=body)

Execute workflow

Execute a workflow

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
    api_instance = tinq.Workflows(api_client)
    workflow_slug = 'workflow_slug_example' # str | 
    content_type = 'application/json' # str |  (optional)
    accept = 'application/json' # str |  (optional)
    body = None # object |  (optional)

    try:
        # Execute workflow
        api_instance.execute_workflow(workflow_slug, content_type=content_type, accept=accept, body=body)
    except Exception as e:
        print("Exception when calling Workflows->execute_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_slug** | **str**|  | 
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

# **get_one_workflow**
> get_one_workflow(workflow_slug, accept=accept, content_type=content_type)

Get one workflow

Get one workflow

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
    api_instance = tinq.Workflows(api_client)
    workflow_slug = 'workflow_slug_example' # str | 
    accept = 'application/json' # str |  (optional)
    content_type = 'application/json' # str |  (optional)

    try:
        # Get one workflow
        api_instance.get_one_workflow(workflow_slug, accept=accept, content_type=content_type)
    except Exception as e:
        print("Exception when calling Workflows->get_one_workflow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_slug** | **str**|  | 
 **accept** | **str**|  | [optional] 
 **content_type** | **str**|  | [optional] 

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

# **get_workflows**
> get_workflows()

Get workflows

List all user's workflows

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
    api_instance = tinq.Workflows(api_client)

    try:
        # Get workflows
        api_instance.get_workflows()
    except Exception as e:
        print("Exception when calling Workflows->get_workflows: %s\n" % e)
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

