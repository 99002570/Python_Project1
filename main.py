from donor import *
A = blooddb("GBG", "saxaxi", "dlodjc", "spiqsid", "xjnsdkci")
A.read_data(thelist)
A.write_data(thelist)
B = input("Enter phone num to search:")
A.search_donor(B)
