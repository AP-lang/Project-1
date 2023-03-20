Select SSN,
(Select Name From Employee_T Where SSN = A.SSN) [worker Name], [Performance Rating], [Percent Salary Increase],
(Select Name From Employee_T Where SSN = A.[Supervisor SSN]) [Supervisor Name]
From performance_Review_t A