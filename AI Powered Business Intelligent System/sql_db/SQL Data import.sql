create database project;
use project;


-- I want to import sales file but it will take more time if i use import table wizard soo i will use load infile for this

# create table for sales 

create table sales(order_id int primary key,
                    order_date date,
                    product_id varchar(30),
                    customer_id varchar(30),
                    quantity_sold int,
                    payment_mode varchar(30),
                    region varchar(30),
                    sales_amount int,
                    profit decimal(7,2));
                    
--  show variables like 'Local_infile';                  
-- 							 
-- load data local infile
-- 'C:/Users/HP/Desktop/Cybrom work/Internship/AI Powered Business Intelligent System/data_cleaned/sales.csv'
-- INTO TABLE sales
-- FIELDS TERMINATED BY ','
-- ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;    


# creating Primary key in each table

--------------------------------------------  Inventory Table -------------------------------------------------------------

describe inventory;
select * from inventory;

alter table inventory modify column inventory_id varchar(30);
alter table inventory modify column product_id varchar(30);

alter table inventory add primary key (inventory_id);

select product_id, count(*) from inventory group by product_id having count(*) > 1;

alter table inventory add foreign key (product_id) references products (product_id);

--------------------------------------------  Product Table -------------------------------------------------------------

describe products;

alter table products modify column product_id varchar(30);

alter table products add primary key (product_id);
               
select product_id , count(*) from products group by product_id having count(*) > 1;



      -- Creating relation with supplier table 

# cleaning the duplicates vales in product_id

create table clean_products as select 
distinct product_id ,
product_name,
category,
brand,
supplier_id,
unit_price
from products;

rename table clean_products to products;

describe products;

alter table products add primary key (product_id);

select product_id , count(*) from clean_products group by product_id having count(*) > 1;

alter table products add foreign key (supplier_id) references suppliers (supplier_id);


--------------------------------------------  Suppliers Table -------------------------------------------------------------    
    
describe suppliers;

select supplier_id , count(*) from  suppliers group by supplier_id having count(*) > 1;

alter table suppliers modify column supplier_id varchar(30) primary key ;

alter table suppliers add primary key (supplier_id);
                    
alter table products add foreign key (supplier_id) references suppliers(supplier_id);


alter table products modify column supplier_id varchar(30);          



--------------------------------------------  Sales Table -------------------------------------------------------------    
  
  
describe sales;

alter table sales modify column product_id varchar(30);

alter table sales add foreign key (product_id) references products (product_id);

select product_id , count(*) from sales group by product_id having count(*) > 1;

alter table sales add region_id VARCHAR(30);

alter table sales add constraint fK_1 foreign key (region_id) references regions (region_id);

alter table sales modify column customer_id varchar(30);

alter table sales add constraint fk_2 foreign key (customer_id) references customers (customer_id);

--------------------------------------------  regions Table -------------------------------------------------------------    

# some extra relation was created soo i deleted it using below queries

alter table sales drop foreign key fk_product_sales;

alter table inventory drop foreign key inventory_ibfk_1;

alter table products drop foreign key products_ibfk_1;


