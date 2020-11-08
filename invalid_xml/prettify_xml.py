import xmlschema
from lxml import etree



def validate_xml_1(xml_file, xsd_file):
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


# example of output : Unescaped '<' not allowed in attributes values, line 114, column 60 (bad-xml-from-tuts.xml, line 114)
def validate_xml_2(xml_file, xsd_file):
    """

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

    return  True, None


def prettify_unit_tests_results(in_file, out_file):
    lines_processed = 0
    f_out = open(out_file, 'w')
    with open(in_file) as f_in:

    #lines = f_in.readlines()
    #print('len of lines is ' + len(lines).__str__())

        for line in f_in:
            pretty_line = line
            #if '"""' in pretty_line:
            #    pretty_line = pretty_line.replace('"""', '')
            if '@' in pretty_line:
                pretty_line = pretty_line.replace('@', '"')
            if '<testcase' in pretty_line:
                pretty_line = pretty_line.replace('<testcase', "\n" + '<testcase')
            if '</testcase' in pretty_line:
                pretty_line = pretty_line.replace('</testcase', "\n" + '</testcase')
            if '<skipped' in pretty_line:
                pretty_line = pretty_line.replace('<skipped', "\n" + '<skipped')
            if '</skipped' in pretty_line:
                pretty_line = pretty_line.replace('</skipped', "\n" + '</skipped')
            if '<testsuit' in pretty_line:
                pretty_line = pretty_line.replace('<testsuit', "\n" + '<testsuit')
            if '</testsuite' in pretty_line:
                pretty_line = pretty_line.replace('</testsuite', "\n" + '</testsuite')
            if '</failure' in pretty_line:
                pretty_line = pretty_line.replace('</failure', "\n" + '</failure')
            if '<failure' in pretty_line:
                pretty_line = pretty_line.replace('<failure', "\n" + '<failure')
            if '&gt;' in pretty_line:
                pretty_line = pretty_line.replace('&gt;', '')
            if '&#10;' in pretty_line:
                pretty_line = pretty_line.replace('&#10;', '')
            lines_processed += 1
            f_out.write(pretty_line)

            print('*** ' + pretty_line.rstrip())

    #f_in.close()
    f_out.close()
    print("\n" + 'finished')
    print(lines_processed)


if __name__ == '__main__':
    xsd_file = 'schema/junit10.xsd'
    #xsd_file = 'schema/jenkins.xsd'

    xml_file = 'artifacts/bad-xml-from-tuts.xml'
    #xml_file = 'artifacts/good-xml-from-tuts.xml'
    #xml_file = 'artifacts/test_results.xml'

    prettify_unit_tests_results(xml_file, 'artifacts/prettified.xml')

    result_1, err_msg_1 = validate_xml_1('artifacts/prettified.xml', xsd_file)
    result_2, err_msg_2 = validate_xml_2('artifacts/prettified.xml', xsd_file)

    print('Schema : ' + xsd_file)
    print('Results file : ' + xml_file)

    if result_1:
        print("Valid XML")
    else:
        print("Invalid XML : " + err_msg_1.__str__())

    if result_2:
        print("Valid XML")
    else:
        print("Invalid XML : " + err_msg_2.__str__())