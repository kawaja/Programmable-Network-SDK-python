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

from TelstraTPN.models.endpoint import Endpoint  # noqa: F401,E501
from TelstraTPN.models.link66 import Link66  # noqa: F401,E501


class Ttms100TopologyTagObjectsResponse(object):
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
        'endpoints': 'list[Endpoint]',
        'links': 'list[Link66]',
        'sharedvports': 'list[str]',
        'topology_tag': 'str'
    }

    attribute_map = {
        'endpoints': 'endpoints',
        'links': 'links',
        'sharedvports': 'sharedvports',
        'topology_tag': 'topology_tag'
    }

    def __init__(self, endpoints=None, links=None, sharedvports=None, topology_tag=None):  # noqa: E501
        """Ttms100TopologyTagObjectsResponse - a model defined in Swagger"""  # noqa: E501

        self._endpoints = None
        self._links = None
        self._sharedvports = None
        self._topology_tag = None
        self.discriminator = None

        if endpoints is not None:
            self.endpoints = endpoints
        if links is not None:
            self.links = links
        if sharedvports is not None:
            self.sharedvports = sharedvports
        if topology_tag is not None:
            self.topology_tag = topology_tag

    @property
    def endpoints(self):
        """Gets the endpoints of this Ttms100TopologyTagObjectsResponse.  # noqa: E501

          # noqa: E501

        :return: The endpoints of this Ttms100TopologyTagObjectsResponse.  # noqa: E501
        :rtype: list[Endpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this Ttms100TopologyTagObjectsResponse.

          # noqa: E501

        :param endpoints: The endpoints of this Ttms100TopologyTagObjectsResponse.  # noqa: E501
        :type: list[Endpoint]
        """

        self._endpoints = endpoints

    @property
    def links(self):
        """Gets the links of this Ttms100TopologyTagObjectsResponse.  # noqa: E501

          # noqa: E501

        :return: The links of this Ttms100TopologyTagObjectsResponse.  # noqa: E501
        :rtype: list[Link66]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Ttms100TopologyTagObjectsResponse.

          # noqa: E501

        :param links: The links of this Ttms100TopologyTagObjectsResponse.  # noqa: E501
        :type: list[Link66]
        """

        self._links = links

    @property
    def sharedvports(self):
        """Gets the sharedvports of this Ttms100TopologyTagObjectsResponse.  # noqa: E501

          # noqa: E501

        :return: The sharedvports of this Ttms100TopologyTagObjectsResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._sharedvports

    @sharedvports.setter
    def sharedvports(self, sharedvports):
        """Sets the sharedvports of this Ttms100TopologyTagObjectsResponse.

          # noqa: E501

        :param sharedvports: The sharedvports of this Ttms100TopologyTagObjectsResponse.  # noqa: E501
        :type: list[str]
        """

        self._sharedvports = sharedvports

    @property
    def topology_tag(self):
        """Gets the topology_tag of this Ttms100TopologyTagObjectsResponse.  # noqa: E501

          # noqa: E501

        :return: The topology_tag of this Ttms100TopologyTagObjectsResponse.  # noqa: E501
        :rtype: str
        """
        return self._topology_tag

    @topology_tag.setter
    def topology_tag(self, topology_tag):
        """Sets the topology_tag of this Ttms100TopologyTagObjectsResponse.

          # noqa: E501

        :param topology_tag: The topology_tag of this Ttms100TopologyTagObjectsResponse.  # noqa: E501
        :type: str
        """

        self._topology_tag = topology_tag

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
        if not isinstance(other, Ttms100TopologyTagObjectsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
