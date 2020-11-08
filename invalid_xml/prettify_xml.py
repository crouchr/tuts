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

# This is more informative
def validate_xml(xml_file, xsd_file):
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
    doc_string = '"' + '"' + '"'
    f_out = open(out_file, 'w')

    with open(in_file) as f_in:
        for line in f_in:
            pretty_line = line
            if doc_string in pretty_line:
                pretty_line = pretty_line.replace(doc_string, '')
            if '@' in pretty_line:
                pretty_line = pretty_line.replace('@', '"')
            if '<testcase' in pretty_line:
                pretty_line = pretty_line.replace('<testcase', "\n" + '<testcase')
            if '</testcase' in pretty_line:
                pretty_line = pretty_line.replace('</testcase', "\n" + '</testcase')
            if '<skipped' in pretty_line:
                pretty_line = pretty_line.replace('<skipped', "\n" + '<skipped')
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
            #if pretty_line[0] != 'E' and pretty_line[0] != '<':
            #    continue
            if pretty_line[0] == 'E' and 'assert False' in pretty_line:
                continue
            if pretty_line[0] == 'E' and 'AssertionError:' in pretty_line:
                continue
            lines_processed += 1
            f_out.write(pretty_line)

            #print(pretty_line.rstrip())

    f_out.close()


if __name__ == '__main__':
    xsd_file = 'schema/junit10.xsd'

    xml_file = 'artifacts/bad-xml-from-tuts.xml'
    pretty_file = 'artifacts/prettified.xml'

    prettify_unit_tests_results(xml_file, pretty_file)

    result, err_msg = validate_xml('artifacts/prettified.xml', xsd_file)

    print('Schema : ' + xsd_file)
    print('Results file : ' + pretty_file)

    if result:
        print("SUCCESS : Valid XML")
    else:
        print("Invalid XML : " + err_msg.__str__())
