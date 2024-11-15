# coding: utf-8

# flake8: noqa

"""
    Tinq AI V2

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v2
    Contact: boulama@tinq.ai
    A Python wrapper for the Tinq.ai API - an easy-to-use text analysis and natural language processing toolkit.
    Generated by OpenAPI Generator

"""  # noqa: E501


__version__ = "0.2.1"

# import apis into sdk package
from tinq.api.assistant import Assistant
from tinq.api.classifiers import Classifiers
from tinq.api.plagiarism_checker import PlagiarismChecker
from tinq.api.projects import Projects
from tinq.api.scraper import Scraper
from tinq.api.tools import Tools
from tinq.api.workflows import Workflows

# import ApiClient
from tinq.api_response import ApiResponse
from tinq.api_client import ApiClient
from tinq.configuration import Configuration
from tinq.exceptions import OpenApiException
from tinq.exceptions import ApiTypeError
from tinq.exceptions import ApiValueError
from tinq.exceptions import ApiKeyError
from tinq.exceptions import ApiAttributeError
from tinq.exceptions import ApiException

# import models into sdk package
