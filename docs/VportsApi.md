# TelstraTPN.VportsApi

All URIs are relative to *https://penapi.pacnetconnect.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_v_port_for_physical_endpoint**](VportsApi.md#create_v_port_for_physical_endpoint) | **POST** /1.0.0/inventory/regularvport | Create VPort for physical endpoint
[**create_vnf_v_port**](VportsApi.md#create_vnf_v_port) | **POST** /1.0.0/inventory/vnf/vport | Create VNF VPort
[**get_information_about_the_specified_v_port**](VportsApi.md#get_information_about_the_specified_v_port) | **GET** /1.0.0/inventory/vport/{vportuuid} | Get information about the specified VPort


# **create_v_port_for_physical_endpoint**
> Model100InventoryRegularvportResponse create_v_port_for_physical_endpoint(body=body)

Create VPort for physical endpoint

Create VPort representing a VLAN on a Physical Ethernet Port

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.VportsApi()
body = TelstraTPN.Model100InventoryRegularvportRequest() # Model100InventoryRegularvportRequest |  (optional)

try: 
    # Create VPort for physical endpoint
    api_response = api_instance.create_v_port_for_physical_endpoint(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->create_v_port_for_physical_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model100InventoryRegularvportRequest**](Model100InventoryRegularvportRequest.md)|  | [optional] 

### Return type

[**Model100InventoryRegularvportResponse**](Model100InventoryRegularvportResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vnf_v_port**
> Model100InventoryVnfVportResponse create_vnf_v_port(body=body)

Create VNF VPort

Create VNF VPort

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.VportsApi()
body = TelstraTPN.Model100InventoryVnfVportRequest() # Model100InventoryVnfVportRequest |  (optional)

try: 
    # Create VNF VPort
    api_response = api_instance.create_vnf_v_port(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->create_vnf_v_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Model100InventoryVnfVportRequest**](Model100InventoryVnfVportRequest.md)|  | [optional] 

### Return type

[**Model100InventoryVnfVportResponse**](Model100InventoryVnfVportResponse.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_information_about_the_specified_v_port**
> EndpointPort get_information_about_the_specified_v_port(vportuuid)

Get information about the specified VPort

Get information about the specified VPort

### Example 
```python
from __future__ import print_function
import time
import TelstraTPN
from TelstraTPN.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: auth
TelstraTPN.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = TelstraTPN.VportsApi()
vportuuid = 'vportuuid_example' # str | Unique identifier representing a specific virtual port

try: 
    # Get information about the specified VPort
    api_response = api_instance.get_information_about_the_specified_v_port(vportuuid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VportsApi->get_information_about_the_specified_v_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vportuuid** | **str**| Unique identifier representing a specific virtual port | 

### Return type

[**EndpointPort**](EndpointPort.md)

### Authorization

[auth](../README.md#auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
