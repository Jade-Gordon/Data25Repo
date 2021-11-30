# slicing = create a substring by extracting elements from
# another string
#       indexing[] or slice()
#       [start:stop:step] or (start,stop,step)

name = "Jade Gordon"

# # create substring:
# first_name = name[:4]
# last_name = name[5:]
# funky_name = name[::2]
# # if you don't specify a start and stop, Python will just assume the first and last indexes
# reversed_name = name[::-1]
# print(first_name) # This is prints out J -> name[0],
# # name[0:4] gives the first 4 characters of the first_name str
# # so does name[:4]
# print(last_name) # This prints out Gordon
# print(funky_name) # This prints out Jd odn
# print(reversed_name) # This reverse the name var -> nodroG edaJ
# lets remove and create a substring based on the website name and nothing else
website = "http://google.com"
#  indexes:0123456789.... .=-4, m=-1
slice = slice(7, -4)
print(website[slice]) # this spits out "google"
