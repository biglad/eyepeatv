cd zips 
del /s /q *.pyo
start addons_xml_generator.py
copy addons.xml ..\
copy addons.xml.md5 ..\


