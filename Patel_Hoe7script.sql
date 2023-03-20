

set echo off
Set pagesize 20
set linesize 96
Column painter_num heading 'P#' format 9999 
Column painter_lname heading 'Last name' Format a15 trunc
Column painter_fname heading 'First name' Format a15 trunc
Column painting_num heading 'Painting#' format 9999 
Column painting_title heading 'Title' format a20 trunc
column painting_value format $999,999,999
SPOOL "x:\ Patel_hoe7.txt";
set echo on

Select* from Painter;
Select* from painting;

Spool off;