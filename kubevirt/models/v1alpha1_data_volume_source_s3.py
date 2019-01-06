# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1DataVolumeSourceS3(object):
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
        'secret_ref': 'str',
        'url': 'str'
    }

    attribute_map = {
        'secret_ref': 'secretRef',
        'url': 'url'
    }

    def __init__(self, secret_ref=None, url=None):
        """
        V1alpha1DataVolumeSourceS3 - a model defined in Swagger
        """

        self._secret_ref = None
        self._url = None

        if secret_ref is not None:
          self.secret_ref = secret_ref
        if url is not None:
          self.url = url

    @property
    def secret_ref(self):
        """
        Gets the secret_ref of this V1alpha1DataVolumeSourceS3.
        SecretRef provides the secret reference needed to access the S3 source

        :return: The secret_ref of this V1alpha1DataVolumeSourceS3.
        :rtype: str
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """
        Sets the secret_ref of this V1alpha1DataVolumeSourceS3.
        SecretRef provides the secret reference needed to access the S3 source

        :param secret_ref: The secret_ref of this V1alpha1DataVolumeSourceS3.
        :type: str
        """

        self._secret_ref = secret_ref

    @property
    def url(self):
        """
        Gets the url of this V1alpha1DataVolumeSourceS3.
        URL is the url of the S3 source

        :return: The url of this V1alpha1DataVolumeSourceS3.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this V1alpha1DataVolumeSourceS3.
        URL is the url of the S3 source

        :param url: The url of this V1alpha1DataVolumeSourceS3.
        :type: str
        """

        self._url = url

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
        if not isinstance(other, V1alpha1DataVolumeSourceS3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
