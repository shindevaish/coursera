#6.5 Write code using find() and string slicing (see section 6.10)
#to extract the number at the end of the line below.
#Convert the extracted value to a floating point number and print it out.

string="DLH-3947_DKHF-2675"
find2=string.find('2')
find5=string.find('5')
print(float(string[find2:find5+1]))