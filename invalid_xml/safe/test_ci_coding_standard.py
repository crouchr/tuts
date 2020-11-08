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

# Standard Module(s)
import os
import glob

# VCC Module(s)
import Tf_plan.nvm_tf_coding_standard_low_level_funcs as nvm_tf_coding_standard_low_level_funcs
import Tf_plan.tuts_config_class as tf_unit_tests_config
import tuts_sdk.tuts_sdk_assert_message as tuts_sdk_assert_message
import tuts_sdk.tuts_sdk_file_funcs as tuts_sdk_file_funcs

# **************************************************
# Tests associated with variables and resource names
# **************************************************


def test_cs_01_input_vars_have_descriptions(stack, module):
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

    _failures = []

    terraform_files = tuts_sdk_file_funcs.match_files_with_recursion(
        stack, module, "variable.tf"
    )

    num_terraform_files = len(terraform_files)
    if num_terraform_files is not 0:

        for file_under_test in terraform_files:
            (
                result,
                _diagnostics,
            ) = nvm_tf_coding_standard_low_level_funcs.all_variables_have_a_description(
                file_under_test
            )
            if not result:
                _failures.append(_diagnostics)

    if _failures:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_01", _failures)
    else:
        assert True, None


def test_cs_02_output_vars_have_descriptions(stack, module):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_02

    TEST PURPOSE : Check that every output variable in output.tf has an associated description.

    This test does NOT check if the description is non-trivial - that is done in another test.
    """

    _failures = []

    terraform_files = tuts_sdk_file_funcs.match_files_with_recursion(
        stack, module, "output.tf"
    )

    # Pass the test if can't find an output.tf file to process - it is not mandatory
    num_terraform_files = len(terraform_files)
    if num_terraform_files is not 0:
        for file_under_test in terraform_files:
            (
                result,
                _diagnostics,
            ) = nvm_tf_coding_standard_low_level_funcs.all_variables_have_a_description(
                file_under_test
            )
            if not result:
                _failures.append(_diagnostics)

    if _failures:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_02", _failures)
    else:
        assert True, None


def test_cs_03_input_vars_descriptions_ok(stack, module):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_03

    TEST PURPOSE : Check that every variable in variable.tf has a non-trivial description
    e.g.
    * The description is not empty ("")
    * The description is not the same as the name of the variable
    * The description is only a few characters long etc.
    """

    _failures = []

    terraform_files = tuts_sdk_file_funcs.match_files_with_recursion(
        stack, module, "variable.tf"
    )

    # Fail the test if can't find one and only one variable file to process
    num_terraform_files = len(terraform_files)
    if num_terraform_files is not 0:
        for file_under_test in terraform_files:
            (
                result,
                _diagnostics,
            ) = nvm_tf_coding_standard_low_level_funcs.all_descriptions_are_compliant(
                file_under_test
            )
            if not result:
                _failures.append(_diagnostics)

    if _failures:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_03", _failures)
    else:
        assert True, None


def test_cs_04_output_vars_descriptions_ok(stack, module):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_04

    TEST PURPOSE : Check that every output variable in output.tf has a non-trivial description
    e.g.
        The description is not empty ("")
        The description is not the same as the name of the variable
        The description is only a few characters long etc.
    """

    _failures = []

    terraform_files = tuts_sdk_file_funcs.match_files_with_recursion(
        stack, module, "output.tf"
    )

    # Note : It is not mandatory to have an output.tf file
    num_terraform_files = len(terraform_files)
    if num_terraform_files is 0:
        return True

    file_under_test = terraform_files[0]

    (
        result,
        _failures,
    ) = nvm_tf_coding_standard_low_level_funcs.all_descriptions_are_compliant(
        file_under_test
    )

    if result:
        assert True, None
    else:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_04", _failures)


def test_cs_05_var_and_resource_names_ok(stack, module):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_05

    TEST PURPOSE : Check that every (input & output) variable, resource and data source has a compliant name
    """

    _failures = []

    terraform_files = tuts_sdk_file_funcs.match_files_with_recursion(
        stack, module, ".tf"
    )

    num_terraform_files = len(terraform_files)
    if num_terraform_files is not 0:
        for file_under_test in terraform_files:
            (
                result,
                file_failures,
            ) = nvm_tf_coding_standard_low_level_funcs.all_variable_names_are_compliant(
                file_under_test
            )
            if not result:
                _failures.append(file_failures)

    if _failures:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_05", _failures)
    else:
        assert True, None


# ***************************
# Tests associated with files
# ***************************


def test_cs_06_module_readme_ok(stack, module):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_06

    TEST PURPOSE : Check Stack / Module README.md file(s)

    Check 1 : Check that a Terraform module has one and only one top-level README.md file
    Check 2 : Check that the README.md file contains (at a minimum), the following  headings 'Module Purpose',
    "Input Variables' and 'Output Variables'

    """

    _failures = []

    # Locate all README.md files in the stack
    readme_files = tuts_sdk_file_funcs.match_files_with_recursion(
        stack, module, "README.md"
    )

    # Fail the test if can't find one and only one README file to process
    num_module_readme_files_found = len(readme_files)
    if num_module_readme_files_found is not 1:
        diagnostic = (
            "Cannot find any README.md file(s) for stack="
            + stack
            + ", module="
            + module
        )
        _failures.append(diagnostic)
        assert False, tuts_sdk_assert_message.make_assert_message("CS_06", _failures)

    result, _failures = nvm_tf_coding_standard_low_level_funcs.readme_files_quality_ok(
        readme_files
    )

    if result:
        assert True, None
    else:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_06", _failures)


# ROADMAP : _MAX_CHARS_IN_TERRAFORM_LINE = 120 store in a single config file
def test_cs_07_tform_line_length_ok(stack, module):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_07

    TEST PURPOSE : Check that every line in a Terraform file is not 'too long'.
    'Too long' is defined by the constant MAX_CHARS_IN_TERRAFORM_LINE.

    Note : If the line of code cannot be shortened by splitting it up, then add the
    TUTS pragma "TUTS: disable=line-too-long" near the start of the file (within a comment) and this
    will disable this unit test on the whole file.

    Terraform files containing lambda definitions, Cloudwatch alarms, variable.tf and output.tf contain lines of
    code (such as description=) that cannot be usefully shortened and thus require the disable=line-too-long pragma.
    For more info on the disable=line-too-long pragma, refer to the CS_07 test in the VCC Terraform Coding Standard.
    """

    MAX_CHARS_IN_TERRAFORM_LINE = 120
    _failures = []

    terraform_files = tuts_sdk_file_funcs.match_files_with_recursion(
        stack, module, ".tf"
    )

    num_terraform_files = len(terraform_files)
    if num_terraform_files is not 0:

        for file_under_test in terraform_files:
            (
                result,
                file_failures,
            ) = nvm_tf_coding_standard_low_level_funcs.terraform_file_line_length_ok(
                file_under_test, MAX_CHARS_IN_TERRAFORM_LINE
            )
            if not result:
                _failures.append(file_failures)

    _num_failures = len(_failures)
    if _num_failures > 0:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_07", _failures)
    else:
        assert True, None


# TODO : split into a low level function that can be unit tested
def test_cs_08_tform_filename_ok(stack, module):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_08

    TEST PURPOSE : Check that Terraform filename is all lowercase and does not contain hyphen (-) character(s).
    """

    _failures = []

    terraform_files = tuts_sdk_file_funcs.match_files_with_recursion(
        stack, module, ".tf"
    )

    # Fail the test if can't find any Terraform files to process
    num_terraform_files = len(terraform_files)
    if num_terraform_files is not 0:

        for file_under_test in terraform_files:
            filename_no_extension = os.path.basename(file_under_test.replace(".tf", ""))
            if filename_no_extension.lower() != filename_no_extension:
                diagnostic = (
                    "File "
                    + tuts_sdk_file_funcs.shorten_full_filename(file_under_test)
                    + " contains mixed case characters"
                )
                _failures.append(diagnostic)
            if "-" in filename_no_extension:
                diagnostic = (
                    "File "
                    + tuts_sdk_file_funcs.shorten_full_filename(file_under_test)
                    + " contains hyphen (-) character(s)"
                )
                _failures.append(diagnostic)

    _num_failures = len(_failures)
    if _num_failures > 0:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_08", _failures)
    else:
        assert True


# REFACTOR _MIN_CHARS_IN_TERRAFORM_FILENAME into a config file
def test_cs_09_tform_filename_length_ok(stack, module):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_09

    TEST PURPOSE : Check that a Terraform filename is not 'too short'

    Walk the stack and check that the filename of each Terraform file is not 'too short'.
    Note : For this unit test, the filename includes the extension i.e. length of 's3.tf' is 5

    Examples :
      f.tf would FAIL the test as len(f.tf) is only 4 characters.
      s3.tf would pass the test as len(s3.tf) is 5 characters.
      foo.tf would pass the test.
      main.tf would pass the test.

    'Too short' is defined by the constant MIN_CHARS_IN_TERRAFORM_FILENAME.
    """

    MIN_CHARS_IN_TERRAFORM_FILENAME = 5

    _failures = []

    glob_pattern = tuts_sdk_file_funcs.match_files_no_recursion(stack, module, "*.tf")

    # terraform_files contains full path/filenames
    terraform_files = glob.glob(glob_pattern)

    # Fail the test if can't find any Terraform files to process
    num_terraform_files = len(terraform_files)
    if num_terraform_files is not 0:

        for full_pathname in terraform_files:
            terraform_filename = os.path.basename(full_pathname)
            terraform_filename_under_test_len = len(terraform_filename)
            if terraform_filename_under_test_len < MIN_CHARS_IN_TERRAFORM_FILENAME:
                diagnostic = (
                    "Filename "
                    + tuts_sdk_file_funcs.shorten_full_filename(terraform_filename)
                    + " has a non-compliant number of characters="
                    + terraform_filename_under_test_len.__str__()
                )
                _failures.append(diagnostic)

    _num_failures = len(_failures)
    if _num_failures > 0:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_09", _failures)
    else:
        assert True


# REFACTOR : move _MAX_LINES_IN_TERRAFORM_FILE to a config file
def test_cs_10_tform_file_num_lines_ok(stack, module):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_10

    TEST PURPOSE : Check that files in a Terraform stack do not contain 'too many' lines.

    'Too many' is defined by the constant MAX_LINES_IN_TERRAFORM_FILE.
    Lines that are inline e.g. using <<EOF, such as JSON-formatted data, do NOT count towards the line count limit

    Note : If the number of lines of code cannot be reduced, then add the TUTS pragma "TUTS: disable=file-too-long"
    near the start of the file (within a comment) and this
    will disable this unit test on the whole file.
    """

    MAX_LINES_IN_TERRAFORM_FILE = 300

    _failures = []

    glob_pattern = tuts_sdk_file_funcs.match_files_no_recursion(stack, module, "*.tf")

    # terraform_files contains full path/filenames
    terraform_files = glob.glob(glob_pattern)

    # Fail the test if can't find any Terraform files to process
    num_terraform_files = len(terraform_files)
    if num_terraform_files is not 0:

        for terraform_filename in terraform_files:
            (
                result,
                diagnostic,
            ) = nvm_tf_coding_standard_low_level_funcs.terraform_file_line_count_ok(
                terraform_filename, MAX_LINES_IN_TERRAFORM_FILE
            )
            if result is False:
                _failures.append(diagnostic)

    _num_failures = len(_failures)
    if _num_failures > 0:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_10", _failures)
    else:
        assert True


# REFACTOR : move _OPEN_TASK_WORDS to a config file
# TODO : There is no unit test for this and it needs to be simplified into calling a function that can be unit tested
def test_cs_11_tform_file_open_tasks_ok(stack, module, capsys):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_11

    TEST PURPOSE : Check that a Terraform file does not contain words such as "TODO" or "FIXME"
    which may indicate that the module code is not complete.
    """

    _failures = []

    OPEN_TASK_WORDS = [
        "todo",
        "fixme",
    ]  # Store as lowercase so Jenkins Open Task plugin does not match on
    # this source file

    OPEN_TASK_WORDS_UPPER = []

    for i in OPEN_TASK_WORDS:
        OPEN_TASK_WORDS_UPPER.append(i.upper())

    glob_pattern = tuts_sdk_file_funcs.match_files_no_recursion(stack, module, "*.tf")

    # terraform_files contains full path/filenames
    terraform_files = glob.glob(glob_pattern)

    # Fail the test if can't find any Terraform files to process
    num_terraform_files = len(terraform_files)
    if num_terraform_files is not 0:

        for full_pathname in terraform_files:
            fp = open(full_pathname, "r")
            for offending_line in fp:
                for open_task_word in OPEN_TASK_WORDS_UPPER:
                    if open_task_word in offending_line.upper():
                        diagnostic = (
                            "File "
                            + tuts_sdk_file_funcs.shorten_full_filename(full_pathname)
                            + " "
                            "contains open task(s) : " + offending_line.rstrip()
                        )
                        _failures.append(diagnostic)

    _num_failures = len(_failures)
    if _num_failures > 0:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_11", _failures)
    else:
        assert True


# TODO : add the various 'imposter' filenames to config file and not be hard-coded
def test_cs_12_no_tform_imposter_filenames(stack, module):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_12

    TEST PURPOSE : Locate Terraform 'imposter' files e.g. files with names that are similar to critical Terraform module
    filenames.

    e.g. vars.tf is an 'imposter' of variable.tf (As per the Terraform Coding Standard)
    """

    _failures = []

    imposter_terraform_files = []
    imposter_filenames = [
        "var.tf",
        "vars.tf",
        "variables.tf",
        "outputs.tf",
        "locals.tf",
    ]

    for imposter_filename in imposter_filenames:
        imposters = tuts_sdk_file_funcs.match_files_with_recursion(
            stack, module, imposter_filename
        )
        if len(imposters) > 0:
            for imposter in imposters:
                imposter_terraform_files.append(imposter)
                diagnostic = (
                    "Found a Terraform imposter file "
                    + tuts_sdk_file_funcs.shorten_full_filename(imposter)
                )

                _failures.append(diagnostic)

    if len(_failures) > 0:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_12", _failures)
    else:
        assert True


def test_cs_13_local_vars_ok(stack, module, unit_tests_config_file):
    """
    *********************************************
    VCC Operations Terraform Coding Standard Test
    *********************************************

    The latest version of the VCC Operations Terraform Coding Standard is stored at
    https://confluence.vonage.com/pages/viewpage.action?pageId=119591668

    TEST ID : CS_13

    TEST PURPOSE : Check that no local variables can be located in any Terraform file (.tf) other than those
    specified in the allowed_locals_filenames parameter in the TUTS Configuration File.

    Note : This test can be disabled on a per-file basis by adding the
    TUTS pragma "TUTS: disable=disable=local-vars-check" near the start of the file.
    """

    _failures = []

    config = tf_unit_tests_config.TFUnitTestsConfig(unit_tests_config_file)

    allowed_locals_filenames = config.allowed_locals_filenames

    terraform_files = tuts_sdk_file_funcs.match_files_with_recursion(
        stack, module, ".tf"
    )

    # Fail the test if can't find any Terraform files to process
    num_terraform_files = len(terraform_files)
    if num_terraform_files is 0:
        diagnostic = (
            "Cannot find any Terraform files for stack=" + stack + ", module=" + module
        )
        _failures.append(diagnostic)
        assert False

    for terraform_filename in terraform_files:
        (
            result,
            diagnostic,
        ) = nvm_tf_coding_standard_low_level_funcs.local_vars_imposters(
            terraform_filename, allowed_locals_filenames
        )

        if result is True:
            _failures.append(diagnostic)

    _num_failures = len(_failures)
    if _num_failures > 0:
        assert False, tuts_sdk_assert_message.make_assert_message("CS_13", _failures)
    else:
        assert True
