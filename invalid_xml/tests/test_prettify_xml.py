import pytest

import prettify_xml


@pytest.mark.parametrize(
    "xml_filename, expected_result",
    [
        ('../artifacts/bad-xml-from-tuts.xml', True),
        ('../artifacts/good-xml-from-tuts.xml', True)
    ]
)
def test_prettify_unit_tests_results(xml_filename, expected_result):
    pretty_output_filename = xml_filename.split('/')[-1]
    pretty_output_filename = pretty_output_filename.split('.')[0]
    pretty_output_filename = '../artifacts/' + pretty_output_filename + '-prettified.xml'

    result, err_msg = prettify_xml.prettify_unit_tests_results(xml_filename, pretty_output_filename)

    assert result == expected_result

