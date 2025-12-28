// how to handle unstructured data in snowflake
create stage json_file
url = 's3://bucketsnowflake-jsondemo';

create or replace file format jsonformat
type=json;

create or replace database myjson_db 


// as the data wont be stored in column manner we store as raw data and name as a raw_file and we dont know data type so we give has a varient
create or replace table json_raw (
raw_file variant)

list @json_file

copy into json_raw
from @new_course_db.external_stages.json_file
file_format= new_course_db.file_formats.jsonformat
files =('HR_data.json')

select*from json_raw

// if you see this list it is the complicated json data it also has nested json and list in the datga so now we work this unstructed data and bring it into a structer format
{
  "city": "Bakersfield",
  "first_name": "Portia",
  "gender": "Male",
  "id": 1,
  "job": {
    "salary": 32000,
    "title": "Financial Analyst"
  },
  "last_name": "Gioani",
  "prev_company": [],
  "spoken_languages": [
    {
      "language": "Kazakh",
      "level": "Advanced"
    },
    {
      "language": "Lao",
      "level": "Basic"
    }
  ]
} //

// if you want extract somthing from this raw data follow this syntaxc

select raw_file:city city from json_raw 
select $1:city::string city from json_raw 

// handling nested data
select  $1:job.salary,$1:job.title::string as job from json_raw

// handling array or list format data

select 
raw_file:first_name::string first_name,
f.value:language::string language,
f.value:level::string level
from json_raw , table (flatten(raw_file:spoken_languages)) f

create table languages as
select 
raw_file:first_name::string first_name,
f.value:language::string language,
f.value:level::string level
from json_raw , table (flatten(raw_file:spoken_languages)) f


select * from languages

