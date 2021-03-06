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


class Params(object):
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
        'description': 'str',
        'duration': 'int',
        'bandwidth': 'int',
        'latency': 'int',
        'linkid': 'str',
        'contractid': 'str',
        'price': 'int',
        'tag': 'str',
        'connections': 'list[str]',
        'topology_tag_uuid': 'str',
        'billing_id': 'str',
        'renewal_option': 'int',
        'latency_sla': 'str',
        'linkstatus': 'int',
        'link_type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'duration': 'duration',
        'bandwidth': 'bandwidth',
        'latency': 'latency',
        'linkid': 'linkid',
        'contractid': 'contractid',
        'price': 'price',
        'tag': 'tag',
        'connections': 'connections',
        'topology_tag_uuid': 'topology_tag_uuid',
        'billing_id': 'billing-id',
        'renewal_option': 'renewal-option',
        'latency_sla': 'latency-sla',
        'linkstatus': 'linkstatus',
        'link_type': 'link-type'
    }

    def __init__(self, description=None, duration=None, bandwidth=None, latency=None, linkid=None, contractid=None, price=None, tag=None, connections=None, topology_tag_uuid=None, billing_id=None, renewal_option=None, latency_sla=None, linkstatus=None, link_type=None):  # noqa: E501
        """Params - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._duration = None
        self._bandwidth = None
        self._latency = None
        self._linkid = None
        self._contractid = None
        self._price = None
        self._tag = None
        self._connections = None
        self._topology_tag_uuid = None
        self._billing_id = None
        self._renewal_option = None
        self._latency_sla = None
        self._linkstatus = None
        self._link_type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if latency is not None:
            self.latency = latency
        if linkid is not None:
            self.linkid = linkid
        if contractid is not None:
            self.contractid = contractid
        if price is not None:
            self.price = price
        if tag is not None:
            self.tag = tag
        if connections is not None:
            self.connections = connections
        if topology_tag_uuid is not None:
            self.topology_tag_uuid = topology_tag_uuid
        if billing_id is not None:
            self.billing_id = billing_id
        if renewal_option is not None:
            self.renewal_option = renewal_option
        if latency_sla is not None:
            self.latency_sla = latency_sla
        if linkstatus is not None:
            self.linkstatus = linkstatus
        if link_type is not None:
            self.link_type = link_type

    @property
    def description(self):
        """Gets the description of this Params.  # noqa: E501

          # noqa: E501

        :return: The description of this Params.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Params.

          # noqa: E501

        :param description: The description of this Params.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def duration(self):
        """Gets the duration of this Params.  # noqa: E501

        Duration of contract in minutes  # noqa: E501

        :return: The duration of this Params.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Params.

        Duration of contract in minutes  # noqa: E501

        :param duration: The duration of this Params.  # noqa: E501
        :type: int
        """
        if duration is not None and duration < 3600:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must be a value greater than or equal to `3600`")  # noqa: E501

        self._duration = duration

    @property
    def bandwidth(self):
        """Gets the bandwidth of this Params.  # noqa: E501

        Bandwidth in kB/s  # noqa: E501

        :return: The bandwidth of this Params.  # noqa: E501
        :rtype: int
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this Params.

        Bandwidth in kB/s  # noqa: E501

        :param bandwidth: The bandwidth of this Params.  # noqa: E501
        :type: int
        """
        if bandwidth is not None and bandwidth > 0:  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value less than or equal to `0`")  # noqa: E501
        if bandwidth is not None and bandwidth < 0:  # noqa: E501
            raise ValueError("Invalid value for `bandwidth`, must be a value greater than or equal to `0`")  # noqa: E501

        self._bandwidth = bandwidth

    @property
    def latency(self):
        """Gets the latency of this Params.  # noqa: E501

        Latency: 0=Low, 1=Standard, 2=Best Effort  # noqa: E501

        :return: The latency of this Params.  # noqa: E501
        :rtype: int
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this Params.

        Latency: 0=Low, 1=Standard, 2=Best Effort  # noqa: E501

        :param latency: The latency of this Params.  # noqa: E501
        :type: int
        """

        self._latency = latency

    @property
    def linkid(self):
        """Gets the linkid of this Params.  # noqa: E501

        Identifier of a link  # noqa: E501

        :return: The linkid of this Params.  # noqa: E501
        :rtype: str
        """
        return self._linkid

    @linkid.setter
    def linkid(self, linkid):
        """Sets the linkid of this Params.

        Identifier of a link  # noqa: E501

        :param linkid: The linkid of this Params.  # noqa: E501
        :type: str
        """

        self._linkid = linkid

    @property
    def contractid(self):
        """Gets the contractid of this Params.  # noqa: E501

        Identifier of a contract  # noqa: E501

        :return: The contractid of this Params.  # noqa: E501
        :rtype: str
        """
        return self._contractid

    @contractid.setter
    def contractid(self, contractid):
        """Sets the contractid of this Params.

        Identifier of a contract  # noqa: E501

        :param contractid: The contractid of this Params.  # noqa: E501
        :type: str
        """

        self._contractid = contractid

    @property
    def price(self):
        """Gets the price of this Params.  # noqa: E501

          # noqa: E501

        :return: The price of this Params.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Params.

          # noqa: E501

        :param price: The price of this Params.  # noqa: E501
        :type: int
        """

        self._price = price

    @property
    def tag(self):
        """Gets the tag of this Params.  # noqa: E501

          # noqa: E501

        :return: The tag of this Params.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Params.

          # noqa: E501

        :param tag: The tag of this Params.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def connections(self):
        """Gets the connections of this Params.  # noqa: E501

          # noqa: E501

        :return: The connections of this Params.  # noqa: E501
        :rtype: list[str]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this Params.

          # noqa: E501

        :param connections: The connections of this Params.  # noqa: E501
        :type: list[str]
        """

        self._connections = connections

    @property
    def topology_tag_uuid(self):
        """Gets the topology_tag_uuid of this Params.  # noqa: E501

          # noqa: E501

        :return: The topology_tag_uuid of this Params.  # noqa: E501
        :rtype: str
        """
        return self._topology_tag_uuid

    @topology_tag_uuid.setter
    def topology_tag_uuid(self, topology_tag_uuid):
        """Sets the topology_tag_uuid of this Params.

          # noqa: E501

        :param topology_tag_uuid: The topology_tag_uuid of this Params.  # noqa: E501
        :type: str
        """

        self._topology_tag_uuid = topology_tag_uuid

    @property
    def billing_id(self):
        """Gets the billing_id of this Params.  # noqa: E501

          # noqa: E501

        :return: The billing_id of this Params.  # noqa: E501
        :rtype: str
        """
        return self._billing_id

    @billing_id.setter
    def billing_id(self, billing_id):
        """Sets the billing_id of this Params.

          # noqa: E501

        :param billing_id: The billing_id of this Params.  # noqa: E501
        :type: str
        """

        self._billing_id = billing_id

    @property
    def renewal_option(self):
        """Gets the renewal_option of this Params.  # noqa: E501

        Renewal Option: 0=Auto Disconnect, 1=Auto Renew, 2=Pay per hour  # noqa: E501

        :return: The renewal_option of this Params.  # noqa: E501
        :rtype: int
        """
        return self._renewal_option

    @renewal_option.setter
    def renewal_option(self, renewal_option):
        """Sets the renewal_option of this Params.

        Renewal Option: 0=Auto Disconnect, 1=Auto Renew, 2=Pay per hour  # noqa: E501

        :param renewal_option: The renewal_option of this Params.  # noqa: E501
        :type: int
        """

        self._renewal_option = renewal_option

    @property
    def latency_sla(self):
        """Gets the latency_sla of this Params.  # noqa: E501

          # noqa: E501

        :return: The latency_sla of this Params.  # noqa: E501
        :rtype: str
        """
        return self._latency_sla

    @latency_sla.setter
    def latency_sla(self, latency_sla):
        """Sets the latency_sla of this Params.

          # noqa: E501

        :param latency_sla: The latency_sla of this Params.  # noqa: E501
        :type: str
        """

        self._latency_sla = latency_sla

    @property
    def linkstatus(self):
        """Gets the linkstatus of this Params.  # noqa: E501

          # noqa: E501

        :return: The linkstatus of this Params.  # noqa: E501
        :rtype: int
        """
        return self._linkstatus

    @linkstatus.setter
    def linkstatus(self, linkstatus):
        """Sets the linkstatus of this Params.

          # noqa: E501

        :param linkstatus: The linkstatus of this Params.  # noqa: E501
        :type: int
        """

        self._linkstatus = linkstatus

    @property
    def link_type(self):
        """Gets the link_type of this Params.  # noqa: E501

          # noqa: E501

        :return: The link_type of this Params.  # noqa: E501
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this Params.

          # noqa: E501

        :param link_type: The link_type of this Params.  # noqa: E501
        :type: str
        """

        self._link_type = link_type

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
        if not isinstance(other, Params):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
