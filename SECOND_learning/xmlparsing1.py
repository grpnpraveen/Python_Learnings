import xml.etree.ElementTree as ET

data='''<person>
                        <name>chuck</name>
                        <phone type="intl">51316166161</phone>
                        <email>jfufb@gmail.com</email>
                </person> '''


info=ET.fromstring(data)
print(info.find("email").text)
print(info.find("phone").get('type'))
