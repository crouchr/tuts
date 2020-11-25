import pytest

import validate_xml


@pytest.mark.parametrize(
    "xml_filename, xsd_filename, expected_result",
    [
        ('../artifacts/bad-xml-from-tuts-prettified.xml', '../schema/junit10.xsd', True)
        #('../artifacts/good-xml-from-tuts-prettified.xml', '../schema/junit10.xsd', True)
    ]
)
def test_validate_xml(xml_filename, xsd_filename, expected_result):

    result, err_msg = validate_xml.validate_xml(xml_filename, xsd_filename)

    assert result == expected_result


#
#     xml_file = 'artifacts/bad-xml-from-tuts.xmlererer'
#     pretty_file = 'artifacts/prettified.xml'
#
#     result, err_msg = prettify_unit_tests_results(xml_file, pretty_file)
#
#     result, err_msg = validate_xml.validate_xml('artifacts/prettified.xml', xsd_file)
#
#     print('Schema : ' + xsd_file)
#     print('Results file : ' + pretty_file)
#
#     if result:
#         print("SUCCESS : Valid XML")
#     else:
#         print("Invalid XML : " + err_msg.__str__())
