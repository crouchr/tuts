# XML validation function
from lxml import etree


def validate_xml(xml_file, xsd_file):
    """
    Validate the XML file in xml_file against the XSD in xsd_file
    :param xml_file:
    :param xsd_file:
    :return:
    """

    try:
        xmlschema_doc = etree.parse(xsd_file)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        xml_doc = etree.parse(xml_file)
        result = xmlschema.validate(xml_doc)

    except Exception as e:
        return False, e

    return result, None
