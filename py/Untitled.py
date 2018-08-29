
# coding: utf-8

# In[1]:


with open("20180829.txt", "r") as f:
    data = f.readlines()
 
    for line in data:
        if line[0] == "#":
            print ("<p class=\"style1\" style=\"margin: 0px; padding: 0px; color: #000000; font-size: 28px; font-family: Helvetica, Arial, sans-serif;\">"+line[1:]+"<br></p>")
        else:
            words = line.split('|')
            print ("<p>"+words[0]+" <a href=\""+words[1]+"\" rel=\"nofollow\">"+words[1][:42]+"...</a></p><p><br></p>")

