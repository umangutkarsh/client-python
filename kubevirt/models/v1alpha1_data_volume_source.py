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


class V1alpha1DataVolumeSource(object):
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
        'blank': 'V1alpha1DataVolumeBlankImage',
        'http': 'V1alpha1DataVolumeSourceHTTP',
        'imageio': 'V1alpha1DataVolumeSourceImageIO',
        'pvc': 'V1alpha1DataVolumeSourcePVC',
        'registry': 'V1alpha1DataVolumeSourceRegistry',
        's3': 'V1alpha1DataVolumeSourceS3',
        'upload': 'V1alpha1DataVolumeSourceUpload',
        'vddk': 'V1alpha1DataVolumeSourceVDDK'
    }

    attribute_map = {
        'blank': 'blank',
        'http': 'http',
        'imageio': 'imageio',
        'pvc': 'pvc',
        'registry': 'registry',
        's3': 's3',
        'upload': 'upload',
        'vddk': 'vddk'
    }

    def __init__(self, blank=None, http=None, imageio=None, pvc=None, registry=None, s3=None, upload=None, vddk=None):
        """
        V1alpha1DataVolumeSource - a model defined in Swagger
        """

        self._blank = None
        self._http = None
        self._imageio = None
        self._pvc = None
        self._registry = None
        self._s3 = None
        self._upload = None
        self._vddk = None

        if blank is not None:
          self.blank = blank
        if http is not None:
          self.http = http
        if imageio is not None:
          self.imageio = imageio
        if pvc is not None:
          self.pvc = pvc
        if registry is not None:
          self.registry = registry
        if s3 is not None:
          self.s3 = s3
        if upload is not None:
          self.upload = upload
        if vddk is not None:
          self.vddk = vddk

    @property
    def blank(self):
        """
        Gets the blank of this V1alpha1DataVolumeSource.

        :return: The blank of this V1alpha1DataVolumeSource.
        :rtype: V1alpha1DataVolumeBlankImage
        """
        return self._blank

    @blank.setter
    def blank(self, blank):
        """
        Sets the blank of this V1alpha1DataVolumeSource.

        :param blank: The blank of this V1alpha1DataVolumeSource.
        :type: V1alpha1DataVolumeBlankImage
        """

        self._blank = blank

    @property
    def http(self):
        """
        Gets the http of this V1alpha1DataVolumeSource.

        :return: The http of this V1alpha1DataVolumeSource.
        :rtype: V1alpha1DataVolumeSourceHTTP
        """
        return self._http

    @http.setter
    def http(self, http):
        """
        Sets the http of this V1alpha1DataVolumeSource.

        :param http: The http of this V1alpha1DataVolumeSource.
        :type: V1alpha1DataVolumeSourceHTTP
        """

        self._http = http

    @property
    def imageio(self):
        """
        Gets the imageio of this V1alpha1DataVolumeSource.

        :return: The imageio of this V1alpha1DataVolumeSource.
        :rtype: V1alpha1DataVolumeSourceImageIO
        """
        return self._imageio

    @imageio.setter
    def imageio(self, imageio):
        """
        Sets the imageio of this V1alpha1DataVolumeSource.

        :param imageio: The imageio of this V1alpha1DataVolumeSource.
        :type: V1alpha1DataVolumeSourceImageIO
        """

        self._imageio = imageio

    @property
    def pvc(self):
        """
        Gets the pvc of this V1alpha1DataVolumeSource.

        :return: The pvc of this V1alpha1DataVolumeSource.
        :rtype: V1alpha1DataVolumeSourcePVC
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """
        Sets the pvc of this V1alpha1DataVolumeSource.

        :param pvc: The pvc of this V1alpha1DataVolumeSource.
        :type: V1alpha1DataVolumeSourcePVC
        """

        self._pvc = pvc

    @property
    def registry(self):
        """
        Gets the registry of this V1alpha1DataVolumeSource.

        :return: The registry of this V1alpha1DataVolumeSource.
        :rtype: V1alpha1DataVolumeSourceRegistry
        """
        return self._registry

    @registry.setter
    def registry(self, registry):
        """
        Sets the registry of this V1alpha1DataVolumeSource.

        :param registry: The registry of this V1alpha1DataVolumeSource.
        :type: V1alpha1DataVolumeSourceRegistry
        """

        self._registry = registry

    @property
    def s3(self):
        """
        Gets the s3 of this V1alpha1DataVolumeSource.

        :return: The s3 of this V1alpha1DataVolumeSource.
        :rtype: V1alpha1DataVolumeSourceS3
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """
        Sets the s3 of this V1alpha1DataVolumeSource.

        :param s3: The s3 of this V1alpha1DataVolumeSource.
        :type: V1alpha1DataVolumeSourceS3
        """

        self._s3 = s3

    @property
    def upload(self):
        """
        Gets the upload of this V1alpha1DataVolumeSource.

        :return: The upload of this V1alpha1DataVolumeSource.
        :rtype: V1alpha1DataVolumeSourceUpload
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """
        Sets the upload of this V1alpha1DataVolumeSource.

        :param upload: The upload of this V1alpha1DataVolumeSource.
        :type: V1alpha1DataVolumeSourceUpload
        """

        self._upload = upload

    @property
    def vddk(self):
        """
        Gets the vddk of this V1alpha1DataVolumeSource.

        :return: The vddk of this V1alpha1DataVolumeSource.
        :rtype: V1alpha1DataVolumeSourceVDDK
        """
        return self._vddk

    @vddk.setter
    def vddk(self, vddk):
        """
        Sets the vddk of this V1alpha1DataVolumeSource.

        :param vddk: The vddk of this V1alpha1DataVolumeSource.
        :type: V1alpha1DataVolumeSourceVDDK
        """

        self._vddk = vddk

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
        if not isinstance(other, V1alpha1DataVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
