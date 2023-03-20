Update Performance_Review_T
GO
Set [Percent Salary Increase] = 4.2 
Where SSN = 
(Select SSN
FROM  Employee_T inner join
performance_review_T on employee_t.SSN = PERFORMANCE_REVIEW_T.SSN
WHERE NAME = 'ALEX BROWN')
GO 
Select * from Performance_Review_T
