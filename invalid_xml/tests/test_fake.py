# These tests are written to fail

"""
This module contains Unit Tests for checking a Terraform module against the VCC Terraform Coding Standard.
These unit tests use the PyTest framework and are run by Jenkins when the Terraform module is built.
"""

__copyright__ = "Copyright 2020, Vonage"
__author__ = "Richard Crouch"
__email__ = "richard.crouch@vonage.com"
__maintainer__ = "Richard Crouch"
__maintainer_team__ = "NETWORK"
__language__ = "Python 3"
__status__ = "Production"


# **************************************************
# Tests associated with variables and resource names
# **************************************************


def test_cs_01():
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_01

    TEST PURPOSE : Check that every input variable in variable.tf has an associated description.

    This test does NOT check if the description is non-trivial - that is done in another test.
    """

    local_var_a = 10
    local_var_b = 20
    local_var_c = 30

    # here is some code
    print('Do something')

    # here is more code
    assert False

    # if _failures:
    #     assert False, tuts_sdk_assert_message.make_assert_message("CS_01", _failures)
    # else:
    #     assert True, None


def test_cs_02():
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_02

    TEST PURPOSE : Check that every input variable in variable.tf has an associated description.

    This test does NOT check if the description is non-trivial - that is done in another test.
    """

    local_var_aa = 10
    local_var_ba = 20
    local_var_ca = 30

    # here is some code
    print('Do something as well')

    # here is more code
    assert False

    # if _failures:
    #     assert False, tuts_sdk_assert_message.make_assert_message("CS_01", _failures)
    # else:
    #     assert True, None
