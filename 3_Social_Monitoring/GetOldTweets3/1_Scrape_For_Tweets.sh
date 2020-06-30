query_string="bitcoin"

for year	in 2017 	;do
for day 	in 3 4 10 19 2  	;do
for month 	in 1 2 3 4 5 6 7 8 9 10 11 12 ;do
	
	time GetOldTweets3 --since $year-$month-$day --until $year-$month-$((day+1)) --querysearch $query_string --output A_Tweet_Data/A_GetOldTweet_$query_string-$year-$month-$day.csv 
	echo $year-$month-$day
	
done
done
done
