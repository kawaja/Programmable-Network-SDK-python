# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.  # noqa: E501

    OpenAPI spec version: 2.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Error(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ns': 'str',
        'error_code': 'int',
        'error_message': 'str',
        'error_auxiliary': 'str'
    }

    attribute_map = {
        'ns': 'ns',
        'error_code': 'error-code',
        'error_message': 'error-message',
        'error_auxiliary': 'error-auxiliary'
    }

    def __init__(self, ns=None, error_code=None, error_message=None, error_auxiliary=None):  # noqa: E501
        """Error - a model defined in Swagger"""  # noqa: E501

        self._ns = None
        self._error_code = None
        self._error_message = None
        self._error_auxiliary = None
        self.discriminator = None

        if ns is not None:
            self.ns = ns
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message
        if error_auxiliary is not None:
            self.error_auxiliary = error_auxiliary

    @property
    def ns(self):
        """Gets the ns of this Error.  # noqa: E501

          # noqa: E501

        :return: The ns of this Error.  # noqa: E501
        :rtype: str
        """
        return self._ns

    @ns.setter
    def ns(self, ns):
        """Sets the ns of this Error.

          # noqa: E501

        :param ns: The ns of this Error.  # noqa: E501
        :type: str
        """

        self._ns = ns

    @property
    def error_code(self):
        """Gets the error_code of this Error.  # noqa: E501

          # noqa: E501

        :return: The error_code of this Error.  # noqa: E501
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this Error.

          # noqa: E501

        :param error_code: The error_code of this Error.  # noqa: E501
        :type: int
        """

        self._error_code = error_code

    @property
    def error_message(self):
        """Gets the error_message of this Error.  # noqa: E501

          # noqa: E501

        :return: The error_message of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this Error.

          # noqa: E501

        :param error_message: The error_message of this Error.  # noqa: E501
        :type: str
        """

        self._error_message = error_message

    @property
    def error_auxiliary(self):
        """Gets the error_auxiliary of this Error.  # noqa: E501

          # noqa: E501

        :return: The error_auxiliary of this Error.  # noqa: E501
        :rtype: str
        """
        return self._error_auxiliary

    @error_auxiliary.setter
    def error_auxiliary(self, error_auxiliary):
        """Sets the error_auxiliary of this Error.

          # noqa: E501

        :param error_auxiliary: The error_auxiliary of this Error.  # noqa: E501
        :type: str
        """

        self._error_auxiliary = error_auxiliary

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
