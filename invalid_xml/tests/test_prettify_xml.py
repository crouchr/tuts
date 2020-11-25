import pytest

import prettify_xml


@pytest.mark.parametrize(
    "xml_filename, expected_result",
    [
        ('../artifacts/bad-xml-from-tuts.xml', True)
    ]
)
def test_prettify_unit_tests_results(xml_filename, expected_result):
    pretty_output_file = '../artifacts/prettified.xml'

    result, err_msg = prettify_xml.prettify_unit_tests_results(xml_filename, pretty_output_file)

    assert result == expected_result



# sd_file = 'schema/junit10.xsd'
#
#     xml_file = 'artifacts/bad-xml-from-tuts.xml'
#     pretty_file = 'artifacts/prettified.xml'

