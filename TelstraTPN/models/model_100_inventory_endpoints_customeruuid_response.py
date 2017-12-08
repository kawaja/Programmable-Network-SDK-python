# coding: utf-8

"""
    Telstra Programmable Network API

    Telstra Programmable Network is a self-provisioning platform that allows its users to create on-demand connectivity services between multiple end-points and add various network functions to those services. Programmable Network enables to connectivity to a global ecosystem of networking services as well as public and private cloud services. Once you are connected to the platform on one or more POPs (points of presence), you can start creating those services based on the use case that you want to accomplish. The Programmable Network API is available to all customers who have registered to use the Programmable Network. To register, please contact your account representative.

    OpenAPI spec version: 2.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Model100InventoryEndpointsCustomeruuidResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'endpointlist': 'list[Endpointlist]'
    }

    attribute_map = {
        'endpointlist': 'endpointlist'
    }

    def __init__(self, endpointlist=None):
        """
        Model100InventoryEndpointsCustomeruuidResponse - a model defined in Swagger
        """

        self._endpointlist = None

        if endpointlist is not None:
          self.endpointlist = endpointlist

    @property
    def endpointlist(self):
        """
        Gets the endpointlist of this Model100InventoryEndpointsCustomeruuidResponse.
        

        :return: The endpointlist of this Model100InventoryEndpointsCustomeruuidResponse.
        :rtype: list[Endpointlist]
        """
        return self._endpointlist

    @endpointlist.setter
    def endpointlist(self, endpointlist):
        """
        Sets the endpointlist of this Model100InventoryEndpointsCustomeruuidResponse.
        

        :param endpointlist: The endpointlist of this Model100InventoryEndpointsCustomeruuidResponse.
        :type: list[Endpointlist]
        """

        self._endpointlist = endpointlist

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Model100InventoryEndpointsCustomeruuidResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other