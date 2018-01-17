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


class TopologiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def ttms100_topology_tag_by_topotaguuid_delete(self, topotaguuid, **kwargs):  # noqa: E501
        """Delete a topology tag  # noqa: E501

        Delete a topology tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_by_topotaguuid_delete(topotaguuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topotaguuid: Unique identifier representing a specific topology tag (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.ttms100_topology_tag_by_topotaguuid_delete_with_http_info(topotaguuid, **kwargs)  # noqa: E501
        else:
            (data) = self.ttms100_topology_tag_by_topotaguuid_delete_with_http_info(topotaguuid, **kwargs)  # noqa: E501
            return data

    def ttms100_topology_tag_by_topotaguuid_delete_with_http_info(self, topotaguuid, **kwargs):  # noqa: E501
        """Delete a topology tag  # noqa: E501

        Delete a topology tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_by_topotaguuid_delete_with_http_info(topotaguuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topotaguuid: Unique identifier representing a specific topology tag (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['topotaguuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ttms100_topology_tag_by_topotaguuid_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'topotaguuid' is set
        if ('topotaguuid' not in params or
                params['topotaguuid'] is None):
            raise ValueError("Missing the required parameter `topotaguuid` when calling `ttms100_topology_tag_by_topotaguuid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'topotaguuid' in params:
            path_params['topotaguuid'] = params['topotaguuid']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ttms/1.0.0/topology_tag/{topotaguuid}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ttms100_topology_tag_by_topotaguuid_get(self, topotaguuid, **kwargs):  # noqa: E501
        """Get information about the specified topology tag  # noqa: E501

        Get information about the specified topology tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_by_topotaguuid_get(topotaguuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topotaguuid: Unique identifier representing a specific topology tag (required)
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.ttms100_topology_tag_by_topotaguuid_get_with_http_info(topotaguuid, **kwargs)  # noqa: E501
        else:
            (data) = self.ttms100_topology_tag_by_topotaguuid_get_with_http_info(topotaguuid, **kwargs)  # noqa: E501
            return data

    def ttms100_topology_tag_by_topotaguuid_get_with_http_info(self, topotaguuid, **kwargs):  # noqa: E501
        """Get information about the specified topology tag  # noqa: E501

        Get information about the specified topology tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_by_topotaguuid_get_with_http_info(topotaguuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topotaguuid: Unique identifier representing a specific topology tag (required)
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['topotaguuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ttms100_topology_tag_by_topotaguuid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'topotaguuid' is set
        if ('topotaguuid' not in params or
                params['topotaguuid'] is None):
            raise ValueError("Missing the required parameter `topotaguuid` when calling `ttms100_topology_tag_by_topotaguuid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'topotaguuid' in params:
            path_params['topotaguuid'] = params['topotaguuid']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ttms/1.0.0/topology_tag/{topotaguuid}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Topology',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ttms100_topology_tag_by_topotaguuid_put(self, topotaguuid, **kwargs):  # noqa: E501
        """Update a topology tag&#39;s name and/or description  # noqa: E501

        Update a topology tag's name and/or description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_by_topotaguuid_put(topotaguuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topotaguuid: Unique identifier representing a specific topology tag (required)
        :param Ttms100TopologyTagRequest body: 
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.ttms100_topology_tag_by_topotaguuid_put_with_http_info(topotaguuid, **kwargs)  # noqa: E501
        else:
            (data) = self.ttms100_topology_tag_by_topotaguuid_put_with_http_info(topotaguuid, **kwargs)  # noqa: E501
            return data

    def ttms100_topology_tag_by_topotaguuid_put_with_http_info(self, topotaguuid, **kwargs):  # noqa: E501
        """Update a topology tag&#39;s name and/or description  # noqa: E501

        Update a topology tag's name and/or description  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_by_topotaguuid_put_with_http_info(topotaguuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topotaguuid: Unique identifier representing a specific topology tag (required)
        :param Ttms100TopologyTagRequest body: 
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['topotaguuid', 'body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ttms100_topology_tag_by_topotaguuid_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'topotaguuid' is set
        if ('topotaguuid' not in params or
                params['topotaguuid'] is None):
            raise ValueError("Missing the required parameter `topotaguuid` when calling `ttms100_topology_tag_by_topotaguuid_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'topotaguuid' in params:
            path_params['topotaguuid'] = params['topotaguuid']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ttms/1.0.0/topology_tag/{topotaguuid}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Topology',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ttms100_topology_tag_get(self, **kwargs):  # noqa: E501
        """List all topology tags  # noqa: E501

        List all topology tags  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_get(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Topology]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.ttms100_topology_tag_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.ttms100_topology_tag_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def ttms100_topology_tag_get_with_http_info(self, **kwargs):  # noqa: E501
        """List all topology tags  # noqa: E501

        List all topology tags  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[Topology]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ttms100_topology_tag_get" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ttms/1.0.0/topology_tag', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Topology]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ttms100_topology_tag_objects_by_topotaguuid_get(self, topotaguuid, **kwargs):  # noqa: E501
        """List objects for Topology  # noqa: E501

        List all objects (Endpoints, Links, VPorts, etc.) associated with the topology tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_objects_by_topotaguuid_get(topotaguuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topotaguuid: Unique identifier representing a specific topology tag (required)
        :return: Ttms100TopologyTagObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.ttms100_topology_tag_objects_by_topotaguuid_get_with_http_info(topotaguuid, **kwargs)  # noqa: E501
        else:
            (data) = self.ttms100_topology_tag_objects_by_topotaguuid_get_with_http_info(topotaguuid, **kwargs)  # noqa: E501
            return data

    def ttms100_topology_tag_objects_by_topotaguuid_get_with_http_info(self, topotaguuid, **kwargs):  # noqa: E501
        """List objects for Topology  # noqa: E501

        List all objects (Endpoints, Links, VPorts, etc.) associated with the topology tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_objects_by_topotaguuid_get_with_http_info(topotaguuid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topotaguuid: Unique identifier representing a specific topology tag (required)
        :return: Ttms100TopologyTagObjectsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['topotaguuid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method ttms100_topology_tag_objects_by_topotaguuid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'topotaguuid' is set
        if ('topotaguuid' not in params or
                params['topotaguuid'] is None):
            raise ValueError("Missing the required parameter `topotaguuid` when calling `ttms100_topology_tag_objects_by_topotaguuid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'topotaguuid' in params:
            path_params['topotaguuid'] = params['topotaguuid']  # noqa: E501

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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ttms/1.0.0/topology_tag/{topotaguuid}/objects/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Ttms100TopologyTagObjectsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def ttms100_topology_tag_post(self, **kwargs):  # noqa: E501
        """Create a named topology tag  # noqa: E501

        Create a named topology tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_post(async=True)
        >>> result = thread.get()

        :param async bool
        :param Ttms100TopologyTagRequest body: 
        :return: Topology
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.ttms100_topology_tag_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.ttms100_topology_tag_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def ttms100_topology_tag_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create a named topology tag  # noqa: E501

        Create a named topology tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.ttms100_topology_tag_post_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param Ttms100TopologyTagRequest body: 
        :return: Topology
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
                    " to method ttms100_topology_tag_post" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/ttms/1.0.0/topology_tag', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Topology',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
