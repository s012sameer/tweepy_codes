from textblob import TextBlob
import csv


file ="csv/realdonaldtrump.csv"
file_out ="csv/realdonaldtrump_sentiment_analysis.csv"   #csv file in which text sentiment analysis gets saved
r_no = 11          # row number of text field

with open(file, 'r') as f, open(file_out, 'w',newline='') as f_out:
    reader = csv.reader(f)
    writer = csv.writer(f_out)
    for row in reader:
        #sentiments are on scale of -1 to 1, so multiplying by 2 to get on scale of -2 to 2
        writer.writerow( row + [2*TextBlob(row[r_no]).sentiment.polarity] )
