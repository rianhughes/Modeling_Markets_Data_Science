for year in 2017;do
for month in 10 11 12; do

python3 41_Get_sentiment_and_Price_DF_parallel.py $year $month & 

done
done
