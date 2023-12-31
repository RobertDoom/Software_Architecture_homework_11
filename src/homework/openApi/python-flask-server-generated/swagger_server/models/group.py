# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Group(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, user_id: int=None):  # noqa: E501
        """Group - a model defined in Swagger

        :param id: The id of this Group.  # noqa: E501
        :type id: int
        :param user_id: The user_id of this Group.  # noqa: E501
        :type user_id: int
        """
        self.swagger_types = {
            'id': int,
            'user_id': int
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId'
        }
        self._id = id
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt) -> 'Group':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Group of this Group.  # noqa: E501
        :rtype: Group
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Group.


        :return: The id of this Group.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Group.


        :param id: The id of this Group.
        :type id: int
        """

        self._id = id

    @property
    def user_id(self) -> int:
        """Gets the user_id of this Group.


        :return: The user_id of this Group.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this Group.


        :param user_id: The user_id of this Group.
        :type user_id: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id
