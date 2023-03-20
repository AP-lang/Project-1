Select name, Department, Salary,
(select [Performance rating] From Performance_Review_T Where SSN= A.SSN) [Performance Rating]
(Select [Percent Salary Increase] From Performance_Review_T Where SSN = A.SSN) [Percent Salary Increase]
From Employee_T A
Where position = 'worker'