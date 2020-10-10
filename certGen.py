from PIL import Image, ImageDraw, ImageFont
import pandas as pd

form = pd.read_csv("test.csv")
#print(form)
#name_list = ["VIDHI DESHMUKH","GARGEE PREMNATH SONAWANE"]
#c_no = ["Kolla Om Vivek", "Sasikumar","Keerthana H K","Aaquib Multani", "Khushi Bhartiya","Heramb Devdutta Chougaonkar","Gargee Premnath Sonawane","Sahil Jamwal","Ashutosh Panigrahi","Suman Patra","Riddhi Kabra","N.Jeevitha", "Linesh Sachin Patil","Sourav Sinha","Palash Burad", "Sathwik Kothapalli","Timiksha Vyas","Harshada Vasudev Patil","Karthik Mikkilineni","Sneha Zambare","Juned Khan", "Jayanth Kumar", "Aditya Patil","Khushi Bhartiya", "Anjali Chandwani", "Sanyam Chhoriya","Makarand Krishnakant Nikam","Aditya Chaudhari"]

#c_no = form['certificate_no'].to_list()
name_list = form['receiver_names'].to_list()

for i in name_list:
    im = Image.open("certi1.jpg")
    d = ImageDraw.Draw(im)
    location = (85, 375)
    text_color = (0, 111, 220)
    font = ImageFont.truetype("C:/Users/Durgacharan Nayak/AppData/Local/Microsoft/Windows/Fonts/SEGOEUIB.ttf",80, encoding="unic")
    d.text(location, i.upper(), fill=text_color,font=font)

   # location_new = (755, 2160)
   # text_color_new = (0, 0, 0)
   # font_new = ImageFont.truetype("arial.ttf", 55, encoding="unic")
   # d.text(location_new, j, fill=text_color_new,font=font_new)
    im.save(i+".pdf")
