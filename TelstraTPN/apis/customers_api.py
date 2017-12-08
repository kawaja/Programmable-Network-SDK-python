# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.

    OpenAPI spec version: 2.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CustomersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_account_information_details(self, customeruuid, **kwargs):
        """
        Get account information details
        Get the account information for the specified customer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_information_details(customeruuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str customeruuid: Unique identifier representing a specific customer (required)
        :return: Model100AccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_account_information_details_with_http_info(customeruuid, **kwargs)
        else:
            (data) = self.get_account_information_details_with_http_info(customeruuid, **kwargs)
            return data

    def get_account_information_details_with_http_info(self, customeruuid, **kwargs):
        """
        Get account information details
        Get the account information for the specified customer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_account_information_details_with_http_info(customeruuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str customeruuid: Unique identifier representing a specific customer (required)
        :return: Model100AccountResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customeruuid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_account_information_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customeruuid' is set
        if ('customeruuid' not in params) or (params['customeruuid'] is None):
            raise ValueError("Missing the required parameter `customeruuid` when calling `get_account_information_details`")


        collection_formats = {}

        path_params = {}
        if 'customeruuid' in params:
            path_params['customeruuid'] = params['customeruuid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['auth']

        return self.api_client.call_api('/1.0.0/account/{customeruuid}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Model100AccountResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_users(self, customeruuid, **kwargs):
        """
        List users
        List all users associated with the specified customer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_users(customeruuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str customeruuid: Unique identifier representing a specific customer (required)
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_users_with_http_info(customeruuid, **kwargs)
        else:
            (data) = self.list_users_with_http_info(customeruuid, **kwargs)
            return data

    def list_users_with_http_info(self, customeruuid, **kwargs):
        """
        List users
        List all users associated with the specified customer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_users_with_http_info(customeruuid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str customeruuid: Unique identifier representing a specific customer (required)
        :return: list[User]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customeruuid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customeruuid' is set
        if ('customeruuid' not in params) or (params['customeruuid'] is None):
            raise ValueError("Missing the required parameter `customeruuid` when calling `list_users`")


        collection_formats = {}

        path_params = {}
        if 'customeruuid' in params:
            path_params['customeruuid'] = params['customeruuid']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['auth']

        return self.api_client.call_api('/1.0.0/account/{customeruuid}/user', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[User]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)