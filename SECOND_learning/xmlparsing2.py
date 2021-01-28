import xml.etree.ElementTree as ET

data='''<stuff>
                <users>
                    <user>
                            <name>praveen</name>
                            <phone type="intl">35131616</phone>
                            <email>jhbd@gmail.com</email>
                    </user>

                    <user>
                            <name>chuck</name>
                            <phone type="intl">51316166161</phone>
                            <email>jfufb@gmail.com</email>
                    </user>


                </users>

            </stuff>'''


info=ET.fromstring(data)
lst=info.findall("users/user")
print("length:",len(info))
for item in lst:
    print(item.find('name').text)
    print(item.find('phone').text)
    print(item.find('phone').get('type'))
