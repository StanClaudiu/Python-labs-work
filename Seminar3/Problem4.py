from stat import FILE_ATTRIBUTE_COMPRESSED


def build_xml_element(tag,name,** key_value ) :
    finalPart = "</" + tag + ">"
    firstPart = "<" + tag 
    for couple in key_value.items() : 
        firstPart += " " + str(couple[0]) + "=" + str(couple[1])
    firstPart += ">"
    return firstPart + finalPart


print(build_xml_element("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))