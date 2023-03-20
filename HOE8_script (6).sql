--Set Environment
set echo off
set linesize 86
set pagesize 40

--column formatting statements go here -- 3 examples provided 
CLEAR COLUMNS;
COLUMN cust_balance  Heading 'Balance'     Format $99,999.99
COLUMN cust_code     Heading 'Cust#'       Format 999999
COLUMN cust_fname    Heading 'First'       Format A10 trunc
COLUMN cust_lname    Heading 'Last'        Format A12 trunc
COLUMN cust_street   Heading 'Street'      Format A14 trunc
COLUMN cust_city     Heading 'City'        Format A10 trunc
COLUMN cust_state    Heading 'State'       Format A5 
COLUMN cust_zip      Heading 'Zip'         Format A5 

/*spool the result sets to a single output file 
  if you watched the lecture on the VLAB, you might use this: */
-- spool y:\Keefe_hoe8Spool.txt
spool C:\Users\tkeefe\Documents\Keefe_hoe8Spool.txt
set echo on;
--Hands on Exercise 8
--written by Teresa Keefe
set echo off;
-------------------------------------------------------------
TTITLE LEFT '**Query 1 **    Page' Format 99 sql.pno skip 1;
set echo on;
--***********************************************************
SELECT * from hw8customer;
set echo off;
-------------------------------------------------------------
TTITLE LEFT '**Query 2 **    Page' Format 99 sql.pno skip 1;
set echo on;
--***********************************************************
--SELECT goes here;
set echo off;
----------------------------------------------------


----------------------------------------------------
/*then some final PL statements to clear the environment and close the spool file*/
SPOOL OFF
TTITLE OFF
CLEAR COLUMNS



