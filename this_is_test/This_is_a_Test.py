
import requests
import mechanize
from bs4 import BeautifulSoup
import urllib2
import cookielib

data = requests.get("https://locations.riteaid.com/").text
soup = BeautifulSoup(data, "lxml")
links = set()
stores_list = list()
store_name = list()
addresses = list()
states = list()
file1 = open("RiteAID.txt", "w")

# for e in soup.findAll('div', {"class": "c-directory-list-content-wrapper"}):
#     store = e.text.strip('\n \t')
#     store_name.append(store.encode('ascii', 'ignore'))

# print "Store count:",len(store_name)

stores = list()
AllData = list()
d = dict()
for x in soup.findAll("ul", {"class": "c-directory-list-content"}):
    for i in x:
        str2 = str(i).split(">")
        str3 = str2[2].split("<")
        # print str3[0]
        states.append(str3[0])
        # Innner state names
        str4 = str(i).split("href=\"")
        str5 = str4[1].split("\">")
        d = dict
        # print(str5[0])
        # for foo in soup.find_all('div', attrs={'class': 'foo'}):
        # 	bar = foo.find('div', attrs={'class': 'bar'})
        # 	print(bar.text)
        data1 = requests.get("https://locations.riteaid.com/" + str5[0]).text
        soup1 = BeautifulSoup(data1, 'lxml')
        for x1 in soup1.findAll("ul", {"class": "c-directory-list-content"}):
            for i1 in x1:
                # print i1
                str6 = str(i1).split("..")
                str7 = str6[1].split("\">")
                # print(str7[0])
                data2 = requests.get("https://locations.riteaid.com" + str7[0]).text
                soup2 = BeautifulSoup(data2, 'lxml')
                for foo in soup2.find_all('div', {'class': 'Nap-left'}):
                    for x2 in foo.findAll("span", {"class": "c-address-street"}):
                        for i2 in x2:
                            str8 = str(i2).split(">")
                            str9 = str8[1].split("<")
                            file1.write(str(str9[0]) + ",")
                    for x3 in foo.findAll("span", {"class": "c-address-postal-code"}):
                        for i3 in x3:
                            file1.write(str(i3) + ",")
                    for x4 in foo.findAll("span", {"class": "c-address-city"}):
                        for i4 in x4:
                            # print(i4)
                            str10 = str(i4).split(">")
                            if str10[1].startswith(","):
                                continue
                            else:
                                str11 = str10[1].split("<")
                                file1.write(str(str11[0]) + ",")
                    for x5 in foo.findAll("abbr", {"class": "c-address-state"}):
                        for i5 in x5:
                            file1.write(str(i5) + ",")
                    for x6 in foo.findAll("span", {"class": "c-phone-number-span c-phone-main-number-span"}):
                        for i6 in x6:
                            file1.write(str(i6) + ",")
                    for x7 in foo.findAll("span", {"class": "coordinates"}):
                        for i7 in x7:
                            str12 = str(i7).split("content=")
                            str13 = str12[1].split("itemprop=")
                            if str13[1].__contains__("latitude"):
                                file1.write(str(str13[0]) + ",")
                            else:
                                file1.write(str(str13[0]))
                    file1.write("\n")
                for foo in soup2.find_all('div', {'class': 'location-list-wrap'}):
                    for x2 in foo.findAll("span", {"class": "c-address-street"}):
                        for i2 in x2:
                            str8 = str(i2).split(">")
                            str9 = str8[1].split("<")
                            file1.write(str(str9[0]) + ",")
                    for x3 in foo.findAll("span", {"class": "c-address-postal-code"}):
                        for i3 in x3:
                            file1.write(str(i3) + ",")
                    for x4 in foo.findAll("span", {"class": "c-address-city"}):
                        for i4 in x4:
                            # print(i4)
                            str10 = str(i4).split(">")
                            if str10[1].startswith(","):
                                continue
                            else:
                                str11 = str10[1].split("<")
                                file1.write(str(str11[0]) + ",")
                    for x5 in foo.findAll("abbr", {"class": "c-address-state"}):
                        for i5 in x5:
                            file1.write(str(i5) + ",")
                    for x6 in foo.findAll("span", {"class": "c-phone-number-span c-phone-main-number-span"}):
                        for i6 in x6:
                            file1.write(str(i6) + ",")
                    for x7 in foo.findAll("span", {"class": "coordinates"}):
                        for i7 in x7:
                            str12 = str(i7).split("content=")
                            str13 = str12[1].split("itemprop=")
                            if str13[1].__contains__("latitude"):
                                latitude = str13[0]
                                file1.write(str(str13[0]) + ",")
                            else:
                                file1.write(str(str13[0]))
                    file1.write("\n")
file1.close()

# for e in soup.findAll('div', {"class": "c-directory-list-content-wrapper"}):
# store = e.text.strip('\n \t')
# store_name.append(store.encode('ascii', 'ignore'))
# if isinstance(i, Tag)
#     str1 = i.get("onclick")
#     if str1.startswith("RWD.store.util.store_page_direction('http://"):
#         str2 = str1.split("RWD.store.util.store_page_direction('http://maps.google.com/maps?")
#             else:
#                 str2 = str1.split("RWD.store.util.store_page_direction('https://www.google.com/maps/place/")
#             str3 = str2[1].split("'")
#             str4 = str3[0]
#             str5 = str4.split("&")
#
#          for str6 in str5:
#                 if 'sll=' in str6 or 'll=' in str6:
#                     result = re.search('ll=(.*)', str6)
#                     sll.append((result.group(1).split(',')))
#                     break
#                 elif "/@" in str6:
#                     result = re.search('@(.*)z/', str6)
#                     coordinates = result.group(1).split(',')[0:2]
#                     sll.append(coordinates)
#             stores.append(str5)
#
# print "SLL count:", len(sll)
# print "Store count:", len(stores)
# #
# #
# for e in soup.findAll("p", {"class": "localStoreAddressBar"}):
#     address = []
#     for x in e.text.replace('\n', '').split('\n'):
#         for y in x.strip('\t').split('\t'):
#             if y != '':
#                 address.append(y.encode('ascii', 'ignore'))
#     addresses.append(address)
#
# final_address_list = list()
#
# for store, address , ll in zip(store_name, addresses, sll):
#     final_address_list.append([store] + address + ll)
#
# print final_address_list
#
# print len(final_address_list)
#
# for store in final_address_list:
#     if len(store) == 7:
#         print store
