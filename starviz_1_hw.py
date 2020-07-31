# My name: Yuhan Xu
# My partner: Nan Yang

""" Our group tries to gather data about average wind speed on months and also compare annual average wind speed between each city
    from our windspeed dataset. And our goal is to see if different locations (coastal or inland) will correlate to different features
    of average wind speed. We use line graph, pie chart and bar chart. Our general conclusion is coastal cities are more likely to
    have higher annual wind speed and different locations actually correspond to different features of average wind speed. I will show 
    conclusions from each graph in detail in my codes later.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("wndspd15.csv") # a csv file about average wind speed

# filter our dataset, and we are only interested in datas in years 198401-201512, which is a fixed time period
filter_dataset = df['YRS'] == "198401-201512"
new_data = df[filter_dataset]

#==================================================1111111111111=========================================

""" First graph: draw a line graph that shows the average wind speed during the period "198401-201512" in two specific locations. 
    One is San Diego which is near the ocean; and another is Minneapolis-St.Paul which is a city in the midwest of USA. We want to 
    see if the location (near or far from the ocean) influences the average wind speed. And we also want to compare them month by 
    month to see in which months the max and the min value of average wind speed will appear 
"""

# choose columns that have only average wind speed data
select = df[['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']]

# 1st city San Diego
x = np.arange(1,13,1)
y1 = select[39:40]  # get a specific row of data which is San Diego
y1 = y1.T # transform row data to array
line1 = plt.plot(x,y1,"ro-",label="Average Wind Speed in San Diego") # plot red dots connected by line

# 2nd city MINNEAPOLIS-ST.PAUL
y2 = select[120:121]
y2 = y2.T
line2 = plt.plot(x,y2,"bs-", label="Average Wind Speed in MINNEAPOLIS-ST.PAUL")

# x-axis labels are chosen to be months
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12],['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC'])
# add x and y labels and title
plt.xlabel('MONTHS')
plt.ylabel('AVERAGE WIND SPEED')
plt.title("Average Wind Speed During 198401-201512")
plt.legend()

plt.show()

""" Conclusion we get from this graph: Since line graph is good to show the relationship between variables on different axis,
    I want to find the relationship between average wind speed and month. And for San Diego (a coastal city), the highest average 
    wind speed appears in May and June which is summer and lowest appears in January which is winter. However, in Minneapolis 
    (an inland city), average wind speed is pretty high between January and April, which is winter and the beginning of the 
    spring. As a result, the trends of line graph representing these two cities are pretty different. And by comparison, 
    we can not only see for each city when the highest and lowest average wind speed occur, but also see the contrast between 
    these two cities' different characteristics in term of average wind speed due to their different locations
"""

#==================================================2222222222222==========================================

""" Second graph: draw a pie chart to compare the average annual wind speed of our randomly chosen 6 cities. Pie chart can easily
    show the proportion of average wind speed of each city. In this way, we can clearly see which city of them has the largest average
    wind speed
"""
random_num = np.random.randint(0,237,size=6) # randomly choose six cities
random_num = random_num.tolist()

values = []
labels = pd.Series()

for i in random_num:
    a = new_data["Unnamed: 0"][i:(i+1)] # use our filtered data here which only have years 198401-201512
    b = pd.to_numeric(new_data["ANN"][i:(i+1)])
    values.append(b)
    labels = labels.append(a)
    
values = pd.Series(values)
fig1, ax1 = plt.subplots()
ax1.pie(values, labels = labels, autopct='%1.2f%%', shadow=True)
plt.axis('equal')
plt.title("Comparison of Annual Average Wind Speed in Randomly Chosen Six Cities")

plt.show()

""" Conclusion we get from this graph: Since it's easy to see the differences in proportion from pie chart, we can see how our randomly
    selected data is displayed in the graph and which of them has the largest area (largest percentage shown in the graph), meaning that
    this particular city has the highest average annual wind speed compared with other cities we choose
"""
#==================================================3333333333333==========================================

""" Third graph: we draw a bar chart to show the average annual wind speed of all cities in the fixed time period. Bar chart represents 
    each data in the dataset by creating a vertical or horizontal bar after each data, which helps us easily observe which city might 
    have the highest annual average wind speed (has the longest bar). In this case, we can do some futher analysis about the reason and
    influences of wind speed and figure out whether the location affect the speed 
"""

objects = new_data["Unnamed: 0"][::20] # get cities' names
performance = new_data["ANN"][::20] # get average wind speed for each city 
y_pos = np.arange(len(objects))

plt.barh(y_pos, performance, align='center', alpha=0.6)
plt.yticks(y_pos, objects)
plt.xlabel("ANNUAL AVERAGE WIND SPEED")
plt.title("Annual Average Wind Speed in Twelve Cities in US")

plt.show()

""" Conclusion we get from this graph: the highest annual average wind speed appears in Corpus Christi, TX, which is a coastal city. And
    the two lowest wind speed occurs in Talkeetna, AK and Augusta, GA, which are not near the ocean. Thus, we can generally conclude that
    coastal city is more likely to have higher average annual wind speed based on our data
"""



