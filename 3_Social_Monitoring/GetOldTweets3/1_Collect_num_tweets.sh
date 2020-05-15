query_string="bitcoin"
for day 	in 1 10 20;do
for month 	in 1 2 3 4 5 6 7 8 9 10 11 12 ;do
for year 	in 2017 2018 2019 ;do	

	GetOldTweets3 --since $year-$month-$day --until $year-$month-$((day+1)) --querysearch $query_string --output A_Tweet_Data/A_GetOldTweet_$query_string-$year-$month-$day.csv 
	echo $year-$month-$day
	echo "Sleeping for 15mins to refresh the API call limit. Sleeping Time 0-3mins"
	sleep 3m
	echo "Sleeping for 15mins to refresh the API call limit. Sleeping Time 3-6mins"
        sleep 3m
	echo "Sleeping for 15mins to refresh the API call limit. Sleeping Time 6-9mins"
        sleep 3m
	echo "Sleeping for 15mins to refresh the API call limit. Sleeping Time 9-12mins"
        sleep 3m
	echo "Sleeping for 15mins to refresh the API call limit. Sleeping Time 12-15mins"
        sleep 3m
done
done
done
