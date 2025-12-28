CREATE OR REPLACE TABLE new_course_db.public.employees (
id INT,
first_name STRING,
last_name STRING,
email STRING,
Location STRING,
department STRING
)


create or replace file format new_course_db.file_formats.csv1_file
type=csv
field_delimiter=','
skip_header=1
null_if= ('NULL','null')
empty_field_as_null=true

create or replace stage new_course_db.external_stages.snowpipe
url='s3://snowflake-demo-kotha/snowpipe/'
storage_integration=s3_inti
file_format = new_course_db.file_formats.csv1_file


list @new_course_db.external_stages.snowpipe
create or replace schema new_course_db.pipe

create or replace pipe new_course_db.pipe.employee1
auto_ingest=true
as
copy into new_course_db.public.employees
from @new_course_db.external_stages.snowpipe

desc pipe new_course_db.pipe.employee1

select * from employees
