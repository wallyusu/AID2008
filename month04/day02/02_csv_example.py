import csv

with open('fengyun.csv','w',newline='')as f:  # windows里需要加一段newline=''，lunix不需要加
    writer = csv.writer(f)
    writer.writerow(['聂风','雪饮狂刀'])
    writer.writerow(['步惊云','绝世好剑'])
    writer.writerow(['段浪','英雄剑'])