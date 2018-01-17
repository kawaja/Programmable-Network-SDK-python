# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.

    OpenAPI spec version: 2.1.3
    
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


class AuthenticationApi(object):
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

    def auth_generatetoken_post(self, grant_type, username, password, **kwargs):
        """
        Create an authentication token
        Create an authentication token
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.auth_generatetoken_post(grant_type, username, password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str grant_type:  (required)
        :param str username:  (required)
        :param str password:  (required)
        :return: Model100AuthGeneratetokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.auth_generatetoken_post_with_http_info(grant_type, username, password, **kwargs)
        else:
            (data) = self.auth_generatetoken_post_with_http_info(grant_type, username, password, **kwargs)
            return data

    def auth_generatetoken_post_with_http_info(self, grant_type, username, password, **kwargs):
        """
        Create an authentication token
        Create an authentication token
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.auth_generatetoken_post_with_http_info(grant_type, username, password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str grant_type:  (required)
        :param str username:  (required)
        :param str password:  (required)
        :return: Model100AuthGeneratetokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['grant_type', 'username', 'password']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_generatetoken_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'grant_type' is set
        if ('grant_type' not in params) or (params['grant_type'] is None):
            raise ValueError("Missing the required parameter `grant_type` when calling `auth_generatetoken_post`")
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `auth_generatetoken_post`")
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `auth_generatetoken_post`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'grant_type' in params:
            form_params.append(('grant_type', params['grant_type']))
        if 'username' in params:
            form_params.append(('username', params['username']))
        if 'password' in params:
            form_params.append(('password', params['password']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/1.0.0/auth/generatetoken', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Model100AuthGeneratetokenResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def auth_validatetoken_get(self, **kwargs):
        """
        Validate authentication token
        Validate the authentication token and get information about the user (roles, permissions, etc.)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.auth_validatetoken_get(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Model100AuthValidatetokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.auth_validatetoken_get_with_http_info(**kwargs)
        else:
            (data) = self.auth_validatetoken_get_with_http_info(**kwargs)
            return data

    def auth_validatetoken_get_with_http_info(self, **kwargs):
        """
        Validate authentication token
        Validate the authentication token and get information about the user (roles, permissions, etc.)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.auth_validatetoken_get_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Model100AuthValidatetokenResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method auth_validatetoken_get" % key
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
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/1.0.0/auth/validatetoken', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Model100AuthValidatetokenResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
