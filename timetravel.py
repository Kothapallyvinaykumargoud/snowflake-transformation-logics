CREATE OR REPLACE TABLE new_course_db.public.test (
id int,
first_name string,
last_name string,
email string,
gender string,
Job string,
Phone string);

create or replace file format new_course_db.file_formats.time_csv
type=csv
field_delimiter=','
skip_header=1;

create or replace stage new_course_db.external_stages.time_travel
url='s3://data-snowflake-fundamentals/time-travel/'
file_format = new_course_db.file_formats.time_csv

list @new_course_db.external_stages.time_travel

copy into new_course_db.public.test
from @new_course_db.external_stages.time_travel

select * from new_course_db.public.test1

update new_course_db.public.test
set email=null

truncate new_course_db.public.test


// BELOW THREE ARE WAYS TO FETCH THE UPDATED DATA 

//one way of recovering updated data using query id=01be8604-0106-48a9-000e-e6df0009800a
select * from new_course_db.public.test before (statement=>'01be8604-0106-48a9-000e-e6df0009800a')

// another way using offset mean 1 min or mins back data
update new_course_db.public.test
set first_name='vinay'

select * from new_course_db.public.test before (offset=>-60*4)

// another way using time stamp
alter session set timezone='UTC';
select current_timestamp

//2025-08-21 19:14:53.747 +0000

UPDATE new_course_db.public.test
SET FIRST_NAME='VINAY'

SELECT * FROM new_course_db.public.test BEFORE (TIMESTAMP=>'2025-08-21 19:14:53.747 +0000'::TIMESTAMP)

// BELOW APPRACHES ARE HOW RECOVER THE DATA 

//ONE IS BAD AND OTHER IS GOOD APPROACH 
CREATE OR REPLACE TABLE new_course_db.public.test1 AS
SELECT * FROM new_course_db.public.test BEFORE (TIMESTAMP=>'2025-08-21 19:14:53.747 +0000'::TIMESTAMP)

INSERT INTO new_course_db.public.test
SELECT * FROM new_course_db.public.test1 

