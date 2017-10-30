nsf_test = read.csv ('nsf_test.csv',stringsAsFactors = TRUE)

sum_by_state = tapply (nsf_test$AwardAmount, nsf_test$StateCode,sum)
par(mfrow = c(2,1))
barplot(sort(sum_by_state,decreasing = TRUE)[1:20],
        xlab = "State",ylab = "Total amount of award",
        main= 'Top twenty states')
barplot(sort(sum_by_state,decreasing = FALSE)[20:1],
        xlab = "State",ylab = "Total amount of award",
        main= 'Last twenty states')

class(nsf_test$AwardEffectiveDate)
table(nsf_test$Directorate_Name)
Mon_year = format(as.Date(nsf_test$AwardEffectiveDate, format="%m/%d/%Y"),"%Y-%m")

sum_by_time = tapply (nsf_test$AwardAmount, Mon_year, mean)




sum_by_type = tapply (nsf_test$AwardAmount, nsf_test$Value, mean)

barplot(sum_by_time,xlab = "Time",ylab = "Average amount of award",
        main= 'Award amount change over time')

barplot(sum_by_type,xlab = "Type",ylab = "Average amount of award",
        main= 'Award amount on different type')
