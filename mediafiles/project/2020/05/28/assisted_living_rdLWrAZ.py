Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
f
>>> from lxml import html
>>> import requests
>>> from pandas import DataFrame as df
>>> def get_site(number):
	url = f"https://www.floridahealthfinder.gov/facilitylocator/FacilityProfilePage.aspx?id={number}"
	page = requests.get(url)
	tree = html.fromstring(page.text)

	
>>> def get_att(value)
SyntaxError: invalid syntax
>>> def get_att(value):
	try:
		return value[0]
	except:
		return None

	
>>> def get_site(number):
	url = f"https://www.floridahealthfinder.gov/facilitylocator/FacilityProfilePage.aspx?id={number}"
	page = requests.get(url)
	tree = html.fromstring(page.text)

	
>>> def get_site(number):
	url = f"https://www.floridahealthfinder.gov/facilitylocator/FacilityProfilePage.aspx?id={number}"
	page = requests.get(url)
	tree = html.fromstring(page.text)
	name = tree.xpath('//span[@id="ct100_titleParagraphPlaceHolder_lblFacilityName"//span/text()')
	return name

>>> get_site(271060)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    get_site(271060)
  File "<pyshell#21>", line 5, in get_site
    name = tree.xpath('//span[@id="ct100_titleParagraphPlaceHolder_lblFacilityName"//span/text()')
  File "src\lxml\etree.pyx", line 1582, in lxml.etree._Element.xpath
  File "src\lxml\xpath.pxi", line 305, in lxml.etree.XPathElementEvaluator.__call__
  File "src\lxml\xpath.pxi", line 225, in lxml.etree._XPathEvaluatorBase._handle_result
lxml.etree.XPathEvalError: Invalid predicate
>>> url = f"https://www.floridahealthfinder.gov/facilitylocator/FacilityProfilePage.aspx?id=271060"
>>> page = requests.get(url)
>>> tree = html.fromstring(page.text)
>>> name = tree.xpath('//span[@id="ct100_titleParagraphPlaceHolder_lblFacilityName"]//span/text()')
>>> name
[]
>>> name = tree.xpath('//span[@id="ct100_titleParagraphPlaceHolder_lblFacilityName"]')
>>> name
[]
>>> name = tree.xpath('//span[@id="ct100_titleParagraphPlaceHolder_lblFacilityName"]')
>>> name
[]
>>> name = tree.xpath('//span/@id')
>>> name
['ctl00_spanTitle', 'ctl00_titleParagraphPlaceHolder_lblFacilityName', 'ctl00_mainContentPlaceHolder_lblStrAddress1', 'ctl00_mainContentPlaceHolder_lblStrCityStateZip', 'ctl00_mainContentPlaceHolder_lblStreetPhoneText', 'ctl00_mainContentPlaceHolder_lblStreetPhone', 'ctl00_mainContentPlaceHolder_lblStreetCountyText', 'ctl00_mainContentPlaceHolder_lblStreetCounty', 'ctl00_mainContentPlaceHolder_lblMailAddress1', 'ctl00_mainContentPlaceHolder_lblMailCityStateZip', 'ctl00_mainContentPlaceHolder_lblMailPhoneText', 'ctl00_mainContentPlaceHolder_lblMailPhone', 'ctl00_mainContentPlaceHolder_lblMailCountyText', 'ctl00_mainContentPlaceHolder_lblMailCounty', 'ctl00_mainContentPlaceHolder_lblLegalSanctionsText', 'ctl00_mainContentPlaceHolder_lblNoLegalSanctions', 'ctl00_mainContentPlaceHolder_lblReports', 'ctl00_mainContentPlaceHolder_lblType', 'ctl00_mainContentPlaceHolder_lblFacilityType', 'ctl00_mainContentPlaceHolder_lblAdmCEOText', 'ctl00_mainContentPlaceHolder_lblAdminCEO', 'ctl00_mainContentPlaceHolder_lblHCCAdminPrompt', 'ctl00_mainContentPlaceHolder_lblHCCAdmin', 'ctl00_mainContentPlaceHolder_lblCFOText', 'ctl00_mainContentPlaceHolder_lblCFO', 'ctl00_mainContentPlaceHolder_lblOwnerText', 'ctl00_mainContentPlaceHolder_lblOwner', 'ctl00_mainContentPlaceHolder_Label5', 'ctl00_mainContentPlaceHolder_lblOwnerSinceDate', 'ctl00_mainContentPlaceHolder_lblPrincipals', 'ctl00_mainContentPlaceHolder_lblOwnType', 'ctl00_mainContentPlaceHolder_lblOwnership', 'ctl00_mainContentPlaceHolder_lblBedsText', 'ctl00_mainContentPlaceHolder_lblBedsCount', 'ctl00_mainContentPlaceHolder_lblBedBreakdownText', 'ctl00_mainContentPlaceHolder_dgBeds_ctl02_lblBedType', 'ctl00_mainContentPlaceHolder_dgBeds_ctl03_lblBedType', 'ctl00_mainContentPlaceHolder_dgBeds_ctl04_lblBedType', 'ctl00_mainContentPlaceHolder_lblRoomBreakdownText', 'ctl00_mainContentPlaceHolder_dgRooms_ctl02_lblBedType', 'ctl00_mainContentPlaceHolder_dgRooms_ctl03_lblBedType', 'ctl00_mainContentPlaceHolder_lblAhcaNumberText', 'ctl00_mainContentPlaceHolder_lblAhcaNumber', 'ctl00_mainContentPlaceHolder_lblAhcaRegionText', 'ctl00_mainContentPlaceHolder_lblLicNum', 'ctl00_mainContentPlaceHolder_lblLicenseNumber', 'ctl00_mainContentPlaceHolder_lblLicEff', 'ctl00_mainContentPlaceHolder_lblLicenseEffective', 'ctl00_mainContentPlaceHolder_lblLicExp', 'ctl00_mainContentPlaceHolder_lblLicenseExpires', 'ctl00_mainContentPlaceHolder_lblLicType', 'ctl00_mainContentPlaceHolder_lblLicenseType', 'ctl00_mainContentPlaceHolder_Label9', 'ctl00_mainContentPlaceHolder_lblLicenseTypeDate', 'ctl00_mainContentPlaceHolder_lblClsdDt', 'ctl00_mainContentPlaceHolder_lblClosedDate', 'ctl00_mainContentPlaceHolder_Label2', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl02_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl03_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl04_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl05_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl06_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl07_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl08_lblModifierCategory', 'ctl00_mainContentPlaceHolder_Label10', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl02_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl03_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl04_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl05_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl06_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl07_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl08_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl09_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl10_lblModifierCategory', 'ctl00_mainContentPlaceHolder_lblArticles']
>>> name = tree.xpath('//span[@id="ct100_titleParagraphPlaceHolder_lblFacilityName"]')
>>> name
[]
>>> name = tree.xpath('//span[@id="ct100_titleParagraphPlaceHolder_lblFacilityName"]')
>>> name
[]
>>> name.tree.xpath('//span/text()')
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    name.tree.xpath('//span/text()')
AttributeError: 'list' object has no attribute 'tree'
>>> name=tree.xpath('//span/text()')
>>> name
['Provider Profile', 'WEST DADE FAMILY CARE CORP', '4585 SW 159TH COURT', 'MIAMI, FL 33185', 'Phone: ', '(305) 553-8008', 'County: ', 'Miami-Dade', '4585 SW 159TH COURT', 'MIAMI, FL 33185', 'Phone: ', 'Phone', 'County: ', 'Miami-Dade', 'Emergency Actions: ', 'None', 'AHCA Reports: ', 'Facility/Provider Type: ', 'Assisted Living Facility', 'Administrator: ', 'KATIUSKA GUTIERREZ', 'Administrator: ', 'Not Available', 'Financial Officer: ', 'KATIUSKA GUTIERREZ', 'Owner/Licensee: ', 'WEST DADE FAMILY CARE CORP', 'Owner/Licensee Since: ', '8/8/2008', 'Controlling Interest for WEST DADE FAMILY CARE CORP', 'Profit Status: ', 'For-Profit', 'Licensed Beds: ', '6', 'Bed Types:', 'Optional State Supplement', 'Extended Congregate Care', 'Private', 'Room Types:', 'Private Rooms', 'Semi-Private Rooms', 'AHCA Number (File Number): ', '11967413', 'AHCA Field Office: ', 'License Number: ', '11458', 'Current License Effective: ', '10/17/2018', 'Expires: ', '1/14/2021', 'License Status: ', 'LICENSED', 'Effective: ', 'Not Available', 'Closed Date: ', 'Not Available', 'Services/Characteristics:', 'Medicaid Services', 'Bed Hold Policy', 'Continuing Care Retirement Community', 'Adult Day Care Services', 'Activities', 'Languages Spoken', 'Nurse Availability', 'Emergency Power Plan Summary:', 'Onsite Alternate Power Source', 'Emergency Power Supports', 'Plan Approval', 'Implementation Date', 'Cooling Method', 'Areas Cooled', 'Areas Cooled Location', 'Square Footage Cooled', 'Number of People to use Cooled Space', 'Consumer Guides: ', 'Attn Providers:  Requests for changes in data must be sent in writing to the \r\n        ', '.\r\n    ', ' - Order Data/Data Dictionary', 'Social Media', ' - Subscribe for Updates', 'We Appreciate Your Feedback!', '1. Did you find this information useful?', '2. Would you recommend this website to family and friends?']
>>> name = tree.xpath('//span[@class="facProfSubhead"]')
>>> name
[<Element span at 0x2571ab147c8>]
>>> name = tree.xpath('//span[@class="facProfSubhead"]/text')
>>> name
[]
>>> name = tree.xpath('//span[@class="facProfSubhead"]//span/text()')
>>> name
['WEST DADE FAMILY CARE CORP']
>>> str1 = tree.xpath('//span[@id="ct100_mainContentPlaceHolder_lblStrAddress1"]/text()')
>>> str1
[]
>>> str1 = tree.xpath('//span[@id="ct100_mainContentPlaceHolder_lblStrAddress1"]/text()')
>>> url = 'https://www.floridahealthfinder.gov/facilitylocator/FacilityProfilePage.aspx?id=399293'
>>> page = requests.get(url)
>>> tree = html.fromstring(page.text)
>>> name = tree.xpath('//span[@class="facProfSubhead"]')
>>> name
[<Element span at 0x2571ab05ea8>]
>>> name
[<Element span at 0x2571ab05ea8>]
>>> name = tree.xpath('//span[@class="facProfSubhead"]/text')
>>> name
[]
>>> name = tree.xpath('//span[@class="facProfSubhead"]//span/text()')
>>> name
['1 AAA ASSISTED LIVING AT WELLINGTON']
>>> str1 = tree.xpath('//span[@id="ct100_mainContentPlaceHolder_lblStrAddress1"]/text()')
>>> str1
[]
>>> str1 = tree.xpath('//span[@class="addressLine"]
		      
SyntaxError: EOL while scanning string literal
>>> str1 = tree.xpath('//span[@class="addressLine"]')
		      
>>> str1
		      
[<Element span at 0x25709e2f098>, <Element span at 0x2571aad6ef8>, <Element span at 0x2571aad6868>, <Element span at 0x2571aad6598>]
>>> str1 = tree.xpath('//span[@class="addressLine"]/text()')
		      
>>> str1
		      
['1337 PINETTA CIR', 'WELLINGTON, FL 33414', '1337 PINETTA CIR', 'WELLINGTON, FL 33414']
>>> str1 = tree.xpath('//span/@id')
		      
>>> str1
		      
['ctl00_spanTitle', 'ctl00_titleParagraphPlaceHolder_lblFacilityName', 'ctl00_mainContentPlaceHolder_lblStrAddress1', 'ctl00_mainContentPlaceHolder_lblStrCityStateZip', 'ctl00_mainContentPlaceHolder_lblStreetPhoneText', 'ctl00_mainContentPlaceHolder_lblStreetPhone', 'ctl00_mainContentPlaceHolder_lblStreetCountyText', 'ctl00_mainContentPlaceHolder_lblStreetCounty', 'ctl00_mainContentPlaceHolder_lblMailAddress1', 'ctl00_mainContentPlaceHolder_lblMailCityStateZip', 'ctl00_mainContentPlaceHolder_lblMailPhoneText', 'ctl00_mainContentPlaceHolder_lblMailPhone', 'ctl00_mainContentPlaceHolder_lblMailCountyText', 'ctl00_mainContentPlaceHolder_lblMailCounty', 'ctl00_mainContentPlaceHolder_lnkFacilityWebsiteText', 'ctl00_mainContentPlaceHolder_lblLegalSanctionsText', 'ctl00_mainContentPlaceHolder_lblNoLegalSanctions', 'ctl00_mainContentPlaceHolder_lblReports', 'ctl00_mainContentPlaceHolder_lblType', 'ctl00_mainContentPlaceHolder_lblFacilityType', 'ctl00_mainContentPlaceHolder_lblAdmCEOText', 'ctl00_mainContentPlaceHolder_lblAdminCEO', 'ctl00_mainContentPlaceHolder_lblHCCAdminPrompt', 'ctl00_mainContentPlaceHolder_lblHCCAdmin', 'ctl00_mainContentPlaceHolder_lblCFOText', 'ctl00_mainContentPlaceHolder_lblCFO', 'ctl00_mainContentPlaceHolder_lblOwnerText', 'ctl00_mainContentPlaceHolder_lblOwner', 'ctl00_mainContentPlaceHolder_Label5', 'ctl00_mainContentPlaceHolder_lblOwnerSinceDate', 'ctl00_mainContentPlaceHolder_lblPrincipals', 'ctl00_mainContentPlaceHolder_lblOwnType', 'ctl00_mainContentPlaceHolder_lblOwnership', 'ctl00_mainContentPlaceHolder_lblBedsText', 'ctl00_mainContentPlaceHolder_lblBedsCount', 'ctl00_mainContentPlaceHolder_lblBedBreakdownText', 'ctl00_mainContentPlaceHolder_dgBeds_ctl02_lblBedType', 'ctl00_mainContentPlaceHolder_dgBeds_ctl03_lblBedType', 'ctl00_mainContentPlaceHolder_dgBeds_ctl04_lblBedType', 'ctl00_mainContentPlaceHolder_lblRoomBreakdownText', 'ctl00_mainContentPlaceHolder_dgRooms_ctl02_lblBedType', 'ctl00_mainContentPlaceHolder_lblAhcaNumberText', 'ctl00_mainContentPlaceHolder_lblAhcaNumber', 'ctl00_mainContentPlaceHolder_lblAhcaRegionText', 'ctl00_mainContentPlaceHolder_lblLicNum', 'ctl00_mainContentPlaceHolder_lblLicenseNumber', 'ctl00_mainContentPlaceHolder_lblLicEff', 'ctl00_mainContentPlaceHolder_lblLicenseEffective', 'ctl00_mainContentPlaceHolder_lblLicExp', 'ctl00_mainContentPlaceHolder_lblLicenseExpires', 'ctl00_mainContentPlaceHolder_lblLicType', 'ctl00_mainContentPlaceHolder_lblLicenseType', 'ctl00_mainContentPlaceHolder_Label9', 'ctl00_mainContentPlaceHolder_lblLicenseTypeDate', 'ctl00_mainContentPlaceHolder_lblClsdDt', 'ctl00_mainContentPlaceHolder_lblClosedDate', 'ctl00_mainContentPlaceHolder_lblNamesText', 'ctl00_mainContentPlaceHolder_Label2', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl02_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl03_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl04_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl05_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl06_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl07_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl08_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl09_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgModifiers_ctl10_lblModifierCategory', 'ctl00_mainContentPlaceHolder_Label10', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl02_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl03_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl04_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl05_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl06_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl07_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl08_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl09_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl10_lblModifierCategory', 'ctl00_mainContentPlaceHolder_dgPowerPlan_ctl11_lblModifierCategory', 'ctl00_mainContentPlaceHolder_lblArticles']
>>> str1=tree.xpath('//span[@id="ctl00_titleParagraphPlaceHolder_lblFacilityName"]')
		      
>>> str1
		      
[<Element span at 0x2571aad6cc8>]
>>> str1=tree.xpath('//span[@id="ctl00_titleParagraphPlaceHolder_lblFacilityName"]/span')
		      
>>> str1
		      
[<Element span at 0x2571ab05f98>]
>>> str1=tree.xpath('//span[@id="ctl00_titleParagraphPlaceHolder_lblFacilityName"]/span/text()')
		      
>>> str1
		      
['1 AAA ASSISTED LIVING AT WELLINGTON']
>>> name=tree.xpath('//span[@id="ctl00_titleParagraphPlaceHolder_lblFacilityName"]/span/text()')
		      
>>> ceo = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblAdminCEO"]')
		      
>>> ceo
		      
[<Element span at 0x2571ab05ea8>]
>>> ceo = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblAdminCEO"]/text()')
		      
>>> ceo
		      
['JONAS AUGUSTE']
>>> cfo = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblAdminCFO"]')
		      
>>> cfo
		      
[]
>>> ceo = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblCFO"]/text()')
		      
>>> ceo = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblAdminCEO"]/text()')
		      
>>> ceo
		      
['JONAS AUGUSTE']
>>> cfo = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblCFO"]/text()')
		      
>>> cfo
		      
['JONAS AUGUSTE']
>>> phone = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStreetPhone"]/text()')
		      
>>> phone
		      
['(561) 422-7059']
>>> str1 = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStrAddress1"]/text()')
		      
>>> str1
		      
['1337 PINETTA CIR']
>>> str2 = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStrAddress2"]/text()')
		      
>>> str2
		      
[]
>>> city = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStrCityStateZip"]/text()')
		      
>>> city
		      
['WELLINGTON, FL 33414']
>>> get_att
		      
<function get_att at 0x000002571AABD158>
>>> county = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStreetCounty"]/text()')
		      
>>> county
		      
['Palm Beach']
>>> def get_site(number):
	url = f"https://www.floridahealthfinder.gov/facilitylocator/FacilityProfilePage.aspx?id={number}"
	page = requests.get(url)
	tree = html.fromstring(page.text)

		      
>>> def get_site(number):
	url = f"https://www.floridahealthfinder.gov/facilitylocator/FacilityProfilePage.aspx?id={number}"
	page = requests.get(url)
	tree = html.fromstring(page.text)
	name = tree.xpath('//span[@class="facProfSubhead"]//span/text()')
	ceo = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblAdminCEO"]')
	cfo = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblCFO"]/text()')phone = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStreetPhone"]/text()')
		      
SyntaxError: invalid syntax
>>> def get_site(number):
	url = f"https://www.floridahealthfinder.gov/facilitylocator/FacilityProfilePage.aspx?id={number}"
	page = requests.get(url)
	tree = html.fromstring(page.text)
	name = tree.xpath('//span[@class="facProfSubhead"]//span/text()')
	ceo = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblAdminCEO"]')
	cfo = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblCFO"]/text()')
	phone = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStreetPhone"]/text()')
	str1 = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStrAddress1"]/text()')
	str2 = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStrAddress2"]/text()')
	city = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStrCityStateZip"]/text()')
	county = tree.xpath('//span[@id="ctl00_mainContentPlaceHolder_lblStreetCounty"]/text()')
	info = [name,ceo,cfo,phone,str1,str2,city,county]
	data = df([[get_att(i) for i in info]],columns=['name','ceo','cfo','phone','str1','str2','city','county'])
	return data

		      
>>> a = get_site(399294)
		      
>>> a
		      
                                                name ceo              cfo  ...  str2                   city    county
0  COUNTRY COTTAGE ON MAIN STREET ADULT DAY CARE ...  []  TERESA TRENTINO  ...  None  BROOKSVILLE, FL 34601  Hernando

[1 rows x 8 columns]
>>> a.columns
		      
Index(['name', 'ceo', 'cfo', 'phone', 'str1', 'str2', 'city', 'county'], dtype='object')
>>> a = get_site(399295)
		      
>>> a
		      
   name   ceo   cfo phone  str1  str2  city county
0  None  None  None  None  None  None  None   None
>>> a.name
		      
0    None
Name: name, dtype: object
>>> import selenium
		      
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    import selenium
ModuleNotFoundError: No module named 'selenium'
>>> ids = pd.read_csv('ids.csv')
		      
>>> ids
		      
      Unnamed: 0       0
0              0  399293
1              1  313782
2              2    4750
3              3  438214
4              4  357995
...          ...     ...
3096        3096  293382
3097        3097  259897
3098        3098  397415
3099        3099  385797
3100        3100  237462

[3101 rows x 2 columns]
>>> ids = df(pd.read_csv('ids.csv'),columns=['nothing','nada','id'])
		      
>>> ids
		      
      nothing  nada  id
0         NaN   NaN NaN
1         NaN   NaN NaN
2         NaN   NaN NaN
3         NaN   NaN NaN
4         NaN   NaN NaN
...       ...   ...  ..
3096      NaN   NaN NaN
3097      NaN   NaN NaN
3098      NaN   NaN NaN
3099      NaN   NaN NaN
3100      NaN   NaN NaN

[3101 rows x 3 columns]
>>> ids = pd.read_csv('ids.csv')
		      
>>> ids.0
		      
SyntaxError: invalid syntax
>>> ids.columns
		      
Index(['Unnamed: 0', '0'], dtype='object')
>>> ids['0']
		      
0       399293
1       313782
2         4750
3       438214
4       357995
         ...  
3096    293382
3097    259897
3098    397415
3099    385797
3100    237462
Name: 0, Length: 3101, dtype: int64
>>> 
