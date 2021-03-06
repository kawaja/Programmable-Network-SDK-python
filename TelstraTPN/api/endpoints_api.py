# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.  # noqa: E501

    OpenAPI spec version: 2.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from TelstraTPN.api_client import ApiClient


class EndpointsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def eis100_endpoints_assign_topology_tag_by_endpointuuid_post(self, endpointuuid, **kwargs):  # noqa: E501
        """Assign a Topology Tag to an Endpoint  # noqa: E501

        Assign a Topology Tag to an Endpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.eis100_endpoints_assign_topology_tag_by_endpointuuid_post(endpointuuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str endpointuuid: Unique identifier representing a specific endpoint (required)
        :param Eis100EndpointsAssignTopologyTagRequest body: 
        :return: list[SuccessFragment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.eis100_endpoints_assign_topology_tag_by_endpointuuid_post_with_http_info(endpointuuid, **kwargs)  # noqa: E501
        else:
            (data) = self.eis100_endpoints_assign_topology_tag_by_endpointuuid_post_with_http_info(endpointuuid, **kwargs)  # noqa: E501
            return data

    def eis100_endpoints_assign_topology_tag_by_endpointuuid_post_with_http_info(self, endpointuuid, **kwargs):  # noqa: E501
        """Assign a Topology Tag to an Endpoint  # noqa: E501

        Assign a Topology Tag to an Endpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.eis100_endpoints_assign_topology_tag_by_endpointuuid_post_with_http_info(endpointuuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str endpointuuid: Unique identifier representing a specific endpoint (required)
        :param Eis100EndpointsAssignTopologyTagRequest body: 
        :return: list[SuccessFragment]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpointuuid', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method eis100_endpoints_assign_topology_tag_by_endpointuuid_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpointuuid' is set
        if ('endpointuuid' not in params or
                params['endpointuuid'] is None):
            raise ValueError("Missing the required parameter `endpointuuid` when calling `eis100_endpoints_assign_topology_tag_by_endpointuuid_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpointuuid' in params:
            path_params['endpointuuid'] = params['endpointuuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/eis/1.0.0/endpoints/{endpointuuid}/assign_topology_tag', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SuccessFragment]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inventory_endpoint_by_endpointuuid_get(self, endpointuuid, **kwargs):  # noqa: E501
        """Get information about the specified endpoint  # noqa: E501

        Get information about the specified endpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_endpoint_by_endpointuuid_get(endpointuuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str endpointuuid: Unique identifier representing a specific endpoint (required)
        :return: InventoryEndpointResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.inventory_endpoint_by_endpointuuid_get_with_http_info(endpointuuid, **kwargs)  # noqa: E501
        else:
            (data) = self.inventory_endpoint_by_endpointuuid_get_with_http_info(endpointuuid, **kwargs)  # noqa: E501
            return data

    def inventory_endpoint_by_endpointuuid_get_with_http_info(self, endpointuuid, **kwargs):  # noqa: E501
        """Get information about the specified endpoint  # noqa: E501

        Get information about the specified endpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_endpoint_by_endpointuuid_get_with_http_info(endpointuuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str endpointuuid: Unique identifier representing a specific endpoint (required)
        :return: InventoryEndpointResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['endpointuuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inventory_endpoint_by_endpointuuid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'endpointuuid' is set
        if ('endpointuuid' not in params or
                params['endpointuuid'] is None):
            raise ValueError("Missing the required parameter `endpointuuid` when calling `inventory_endpoint_by_endpointuuid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'endpointuuid' in params:
            path_params['endpointuuid'] = params['endpointuuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0.0/inventory/endpoint/{endpointuuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InventoryEndpointResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inventory_endpoints_customeruuid_by_customeruuid_get(self, customeruuid, **kwargs):  # noqa: E501
        """Get list of endpoints for a customer  # noqa: E501

        Get list of endpoints for a customer  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_endpoints_customeruuid_by_customeruuid_get(customeruuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customeruuid: Unique identifier representing a specific customer (required)
        :return: InventoryEndpointsCustomeruuidResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.inventory_endpoints_customeruuid_by_customeruuid_get_with_http_info(customeruuid, **kwargs)  # noqa: E501
        else:
            (data) = self.inventory_endpoints_customeruuid_by_customeruuid_get_with_http_info(customeruuid, **kwargs)  # noqa: E501
            return data

    def inventory_endpoints_customeruuid_by_customeruuid_get_with_http_info(self, customeruuid, **kwargs):  # noqa: E501
        """Get list of endpoints for a customer  # noqa: E501

        Get list of endpoints for a customer  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_endpoints_customeruuid_by_customeruuid_get_with_http_info(customeruuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str customeruuid: Unique identifier representing a specific customer (required)
        :return: InventoryEndpointsCustomeruuidResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customeruuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inventory_endpoints_customeruuid_by_customeruuid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customeruuid' is set
        if ('customeruuid' not in params or
                params['customeruuid'] is None):
            raise ValueError("Missing the required parameter `customeruuid` when calling `inventory_endpoints_customeruuid_by_customeruuid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customeruuid' in params:
            path_params['customeruuid'] = params['customeruuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0.0/inventory/endpoints/customeruuid/{customeruuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InventoryEndpointsCustomeruuidResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inventory_regularendpoint_post(self, **kwargs):  # noqa: E501
        """Create Physical (Port) Endpoint  # noqa: E501

        Create Physical (Port) Endpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_regularendpoint_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param InventoryRegularendpointRequest body: 
        :return: list[InventoryRegularendpointResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.inventory_regularendpoint_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.inventory_regularendpoint_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def inventory_regularendpoint_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Physical (Port) Endpoint  # noqa: E501

        Create Physical (Port) Endpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_regularendpoint_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param InventoryRegularendpointRequest body: 
        :return: list[InventoryRegularendpointResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inventory_regularendpoint_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0.0/inventory/regularendpoint', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InventoryRegularendpointResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inventory_vnfendpoint_post(self, **kwargs):  # noqa: E501
        """Create VNF Endpoint  # noqa: E501

        Create VNF Endpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_vnfendpoint_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param InventoryVnfendpointRequest body: 
        :return: list[InventoryVnfendpointResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.inventory_vnfendpoint_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.inventory_vnfendpoint_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def inventory_vnfendpoint_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create VNF Endpoint  # noqa: E501

        Create VNF Endpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_vnfendpoint_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param InventoryVnfendpointRequest body: 
        :return: list[InventoryVnfendpointResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inventory_vnfendpoint_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0.0/inventory/vnfendpoint', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InventoryVnfendpointResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
