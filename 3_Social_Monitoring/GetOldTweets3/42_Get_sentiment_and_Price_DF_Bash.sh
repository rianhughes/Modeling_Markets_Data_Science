for year in 2018;do
for month in 1 2 3 4 5 6 7 8 9 10 11 12; do

python3 41_Get_sentiment_and_Price_DF_parallel.py $year $month & 

done
done
