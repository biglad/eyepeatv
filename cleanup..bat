cd zips 
del /s /q *.pyo
addons_xml_generator.py
copy addons.xml ..\
copy addons.xml.md5 ..\
del addons.xml
del addons.xml.md5
cd ..


