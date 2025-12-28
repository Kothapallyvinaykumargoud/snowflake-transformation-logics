create stage  my_stage
url = "s3://dw-snowflake-account-vinay/instacart2025/"
credentials = (aws_key_id ='AK*********' aws_secret_key='HuuA*******');

 // so now we have access to aws so we can easliy work with the files in aws.

 //2 step we need to define the file format
 create or replace file format csv_file_format
 type='csv'
 field_delimiter = ','
 skip_header = 1
 field_optionally_enclosed_by ='"';

 // step 3 loading our dtaa from s3 bucket
 
create table aisles (
             aisle_id integer primary key,
             aisle    varchar
)

copy into aisles (aisle_id ,aisle)
from @my_stage/aisles.csv
file_format =(format_name = 'csv_file_format');

create table departments (
              department_id integer primary key,
              department    varchar
)

copy into departments (department_id,department)
from @my_stage/departments.csv
file_format =(format_name = 'csv_file_format');

create table departments (
              department_id integer primary key,
              department    varchar
)

CREATE OR REPLACE TABLE products (
product_id INTEGER PRIMARY KEY,
product_name VARCHAR,
aisle_id INTEGER,
department_id INTEGER
);

COPY INTO products (product_id, product_name, aisle_id, department_id)
FROM @my_stage/products.csv
FILE_FORMAT = (FORMAT_NAME = 'csv_file_format');

CREATE OR REPLACE TABLE orders (
order_id INTEGER PRIMARY KEY,
user_id INTEGER,
eval_set STRING,
order_number INTEGER,
order_dow INTEGER,
order_hour_of_day INTEGER,
days_since_prior_order INTEGER
);

COPY INTO orders (order_id, user_id, eval_set, order_number, order_dow, order_hour_of_day,
days_since_prior_order)
FROM @my_stage/orders.csv
FILE_FORMAT = (FORMAT_NAME = 'csv_file_format');

CREATE OR REPLACE TABLE order_products_prior (
order_id INTEGER,
product_id INTEGER,
add_to_cart_order INTEGER,
reordered INTEGER,
PRIMARY KEY (order_id, product_id)
);
COPY INTO order_products_prior(order_id, product_id, add_to_cart_order, reordered)
FROM @my_stage/order_products__prior.csv
FILE_FORMAT = (FORMAT_NAME = 'csv_file_format');

select * from order_products__prior


drop table order__products
