ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

########### list
ft_list[1] = "World!"

########### tuple
temp_list = list(ft_tuple)
temp_list[1] = "France!"
ft_tuple = tuple(temp_list)

########### set
temp_list = list(ft_set)
if (temp_list[0] == "tutu!"):
	temp_list[0] = "Paris!"
else:
	temp_list[1] = "Paris!"
ft_set = set(temp_list)

########### dict
ft_dict["Hello"] = "42Paris!"

###########
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)