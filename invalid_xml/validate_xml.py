# XML validation function
from lxml import etree

# import xmlschema
# def validate_xml_1(xml_file, xsd_file):
#     """
#
#     :param xml_file:
#     :param xsd_file:
#     :return:
#     """
#
#     try:
#         xmlschema.validate(xml_file, xsd_file)
#     except Exception as e:
#         return False, e
#
#     return True, None


def validate_xml(xml_file, xsd_file):
    """
    Validate the XML file in xml_file against the XSD in xsd_file
    :param xml_file:
    :param xsd_file:
    :return:
    """

    xmlschema_doc = etree.parse(xsd_file)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    try:
        xml_doc = etree.parse(xml_file)
        result = xmlschema.validate(xml_doc)

    except Exception as e:
        return False, e

    return result, None
