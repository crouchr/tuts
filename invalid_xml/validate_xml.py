import xmlschema


def validate_xml(xml_file, xsd_file):
    """

    :param xml_file:
    :param xsd_file:
    :return:
    """

    try:
        xmlschema.validate(xml_file, xsd_file)
    except Exception as e:
        return False, e

    return True, None


if __name__ == '__main__':
    xml_file = 'bad-xml-from-tuts.xml'
    xsd_file = 'junit10.xsd'

    result, err_msg = validate_xml(xml_file, xsd_file)

    if result :
        print("Valid XML")
    else:
        print("Invalid XML : " + err_msg.__str__())
