Set Environment
set echo off
set linesize 86
set pagesize 40

--drop table Member;



--column formatting
CLEAR COLUMNS;
COLUMN CarrierID            Heading 'CarrierID'          Format A10 trunc   
COLUMN CarName              Heading 'Carname'            Format A15 trunc
COLUMN Caraddress           Heading 'Caraddress'         Format A11 trunc
COLUMN CarCity              Heading 'CarCity'            Format A12 trunc
COLUMN CarStCode            Heading 'CarStCode'          Format A12 trunc
COLUMN CarZip               Heading 'CarZip'             Format A5 trunc
COLUMN CarPhone             Heading 'Carphone'           Format A12 trunc
COLUMN CarWebSite           Heading 'CarWeb'             Format A21 trunc
COLUMN CarContactFirstName  Heading 'CarFname'           format A12 trunc
COLUMN CarContactLastName   Heading 'CarLname'           format A12 trunc     
COLUMN CarEmail             Heading 'CarEmail'		       format A14 trunc  
COLUMN PlanID               Heading 'PlanID'             format A12 trunc
COLUMN plndescription       Heading 'PlnDesc'            Format A7 Trunc    
COLUMN Plncost              Heading 'Plncost'            Format $999
COLUMN MemberNo             Heading 'MemberNo'           Format A10 trunc
COLUMN mbrFirstName         Heading 'MbrFName'           Format A10 trunc
COLUMN mbrLastName          Heading 'MbrLname'		       Format A10 trunc

COLUMN mbrStreet            Heading 'MbrStreet' 	       format A10 trunc
COLUMN mbrCity              Heading 'MbrCity'            Format A13 trunc
COLUMN mbrzip               Heading 'Mbrzip'             Format A20 trunc
COLUMN mbrPhoneNo           Heading 'MbrPhoneNo'          Format A10 trunc
COLUMN mbrEmail            Heading 'MbrEmail'		          format A25 trunc
COLUMN MbrDateEffective     Heading 'MbrDateEffective'     Format A12 trunc
COLUMN EmployerID           Heading 'EmployerID'    

COLUMN emplname               Heading 'EmplName'         Format A8 trunc
COLUMN empladdress            Heading 'EmplAddress'      Format A12 trunc
COLUMN emplCity               Heading 'EmplCity'         Format A8 trunc
COLUMN emplState              Heading 'EmplState'        Format A9 trunc
COLUMN EmplZip                Heading 'EmplZip'          Format A7 trunc
COLUMN EmplPhone              Heading 'EmplPhone'        Format A9 trunc
COLUMN EmplCOntactFirstName   Heading 'EmplFname'     Format A9 trunc
COLUMN EmplContactLastName    Heading 'EmplLname'     Format A9 trunc
COLUMN emplContactEmail       Heading 'EmplConEmail'     Format A12 trunc
COLUMN AgentId                Heading 'AgentId'
column AGENTUPERID            heading 'AgentSid'      Format A8 trunc
Column AgentFname             Heading 'AgentFname'    Format A10 trunc
Column AgentLname             Heading 'AgentLname'    Format A10 trunc
Column AgentPhone             Heading 'AgentPhone'    Format A13 trunc
Column AgentSuperID           Heading 'AgentSuperID'  Format A12 trunc

Column AgentTitle             Heading 'Agenttitle'    Format A10 trunc
Column AreaCode         Heading 'AreaCode'           Format A8 trunc
Column MBRPhone         Heading 'MBRPhone'          Format A8 trunc
Column  MbrName         Heading 'MbrName'           Format A7 trunc
Column  ctype           Heading 'C-type'            Format A10 trunc
 Column plState         Heading 'plState'           Format A7 trunc
 Column Planavg         Heading 'PlanAvg'           Format $999.999 trunc
 Column EMPCNT          Heading 'EmpCnt'            Format A6 trunc
 Column MEMCNT          Heading 'MemCnt'            Format A6 trunc
 Column PCT             Heading 'PCT'               Format A3 trunc
  Column EmCNT          Heading 'EmCnt'             Format A5 trunc
  Column PlnCount       Heading 'PlnCount'          Format A6 trunc
  Column CarCnt         heading 'CarCnt'            Format A6 trunc
  Column Caravgpln      Heading 'Caravgpln'         Format $999
  Column Avgpln         Heading 'Avgpln'            Format $999
 Column MBRCNT          Heading 'MbrCnt'            Format A6 trunc
 column Fname           Heading 'Fname'             Format A5 trunc 
 Column Lname           Heading 'Lname'             Format A5 trunc
 Column PlanCNT         Heading 'PlanCnt'           Format A7 trunc 
 column MbrName         Heading 'MbrName'           Format A11 trunc 
---------------------

Spool  x:\Patel_P8Spool.txt

set echo on;

set echo off;
-------------------------------------------------------------
TTITLE LEFT '**Query 1 **    Page' Format 99 sql.pno skip 1;
set echo on;
--***********************************************************
Select count(MemberNo) as "MemberNo"
from Member;

Insert into member (MemberNo, mbrFirstName, mbrLastName, MbrStreet, MbrCity, MbrState, MbrZip, MbrPhoneNo, PlanID, mbrEmail, MbrDateEffective, EmployerID)
Values (99, 'Abhi', 'Patel', '3921 Leroy Lane', 'Pikeville', 'OH','41501', '9153608888',  '7', 'ta2b2pdozdl@gmail.com', '5-NOV-2021', '2'); 
commit;

Select count(MemberNo) as "MemberNo"
from Member;







set echo off;
-------------------------------------------------------------
TTITLE LEFT '**Query 2 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Select mbrLastName ||', '|| MbrFirstName as "MbrName", Substr(MbrPhoneNo,1,3) as "AreaCode", substr(MbrPhoneNo,4,7) As "MBRPhone"
from Member
Where Substr(MbrPhoneNo,1,3) = 915
Order by MbrLastName;


set echo off;


----------------------------------------------------
TTITLE LEFT '**Query 3 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Update Agent 
Set AgentTitle = 'Sales Rep'
Where AgentTitle = 'Salesman';

Select AgentID, AgentFname, AgentLname, AgentPhone, AGENTUPERID, AgentTitle
From Agent
ORder by AgentLname asc;




set echo off;
----------------------------------------------------

TTITLE LEFT '**Query 4 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Select MbrFirstname as "Fname", MbrLastname  as "Lname", MbrEmail, 'Member' as "ctype"
 
From Member
Where mbrState = 'OH'
Union
Select EmplContactFirstName as "Fname", EmplcontactLastname  as "Lname", EmplcontactEmail,  'Employer' as "ctype"
from Employer
Where emplState = 'OH'
Union
Select CarContactFirstName as "Fname", CarContactLastName   as "Lname", CarEmail,  'Carrier' as "ctype" 
From Carrier
Where CarStCode = 'OH'

Order by "Lname";




set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 5 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Select CarStCode as "plState" from Carrier 
intersect 
Select EmplState as "plState" from Employer
order by "plState";






set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 6 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Select emplstate as "plState" from employer 
Where emplstate in(select CarStCode as "State" from Carrier)
Order by "plState";




set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 7 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************

Select CarrierID, Carname from Carrier
Minus 
Select CarrierId, carname from PLAN natural join carrier
order by carname;






set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 8 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Select CarrierID, Carname, Carwebsite
from carrier 
Where carrierid in (select plan.carrierid from plan)
order by carname;





set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 9 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Select plan.planid, plndescription, plncost, count(memberNO) as "MemberNo"
from plan left join member on plan.planid = member.planid
group by plan.planid, plndescription, plncost
order by plan.planid;







set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 10 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
select plan.planid, plndescription, plncost, count(memberNO) as "MemberNo"
from plan full outer join member on plan.planid = member.planid
group by plan.planid, plndescription, plncost
order by planid;






set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 11 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
select planid, plndescription, plncost, (select AVG(PLNCOST) from plan) as "Planavg"
From plan
group by planid, plndescription, plncost
having sum(plncost) > (select avg(plncost) from plan)
order by PlanId;







set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 12 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Select Agent.AgentID, AgentFname, AgentLname, Count(distinct employer.EmployerId) as "EMPCNT", Count(Member.MemberNo) as "MEMCNT"
From Agent left join employer on employer.AGENTID = Agent.AGENTID 
left join Member on Member.EmployerId = Employer.EmployerID

group by Agent.AgentID, AgentFname, AgentLname
order by Agent.AgentID;
 









set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 13 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************





Select * from PatelView13;




set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 14 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Select carrier.carrierId, CarName, plan.PlanID, PlnDescription, Count(memberNo) as "MemberNo", count(plan.planid) as "PlanCNT", (Count(memberNo) / count(carrier.carrierid) * 100 ) as "PCT"

From Carrier Left Join Plan on Carrier.CarrierID = Plan.CarrierID 
Left Join Member on plan.PlanId = member.PlanID


Group by  carrier.carrierId, CarName, plan.PlanID, PlnDescription

order by carrier.CarrierID, plan.planID;









set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 15 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Select emplName, Count(Distinct MemberNo) as "emCnt", Count(distinct Planid) as "PlnCount", count(distinct carrierID) as "CarCnt"
from employer natural join member natural join plan natural join carrier
group by emplname
order by emplname;




set echo off;
----------------------------------------------------
TTITLE LEFT '**Query 16 **    Page' Format 99 sql.pno skip 1;
set echo on;

--***********************************************************
Select carrier.CarrierID, CarName, PlanId, PLndescription, plncost, Avg(Plncost) as "CARAVGPLN", (select Avg(plncost) from plan) as "AVGPLN"
from carrier left join plan on carrier.carrierID = plan.CarrierID
group by carrier.CarrierID, CarName, PlanId, PLndescription, plncost
order by PlanID; 






set echo off;
----------------------------------------------------

----------------------------------------------------

SPOOL OFF
TTITLE OFF
CLEAR COLUMNS














