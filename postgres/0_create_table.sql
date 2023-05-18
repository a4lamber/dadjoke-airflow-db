-- creating tables
create table if not exists customer (
        first_name VARCHAR(30) not null,
        last_name VARCHAR(30) not null,
        email VARCHAR(60) not null,
        company VARCHAR(60) not null,
        street VARCHAR(50) not null,
        city VARCHAR(30) not null,
        state CHAR(2) not null,
        zip SMALLINT not null,
        phone VARCHAR(20) not null,
        birth_date DATE null,
        sex CHAR(1) not null,
        date_entered TIMESTAMP not null,
        id Serial primary key
   );
  	
-- inserting values 	
  
INSERT INTO customer (first_name, last_name, email, company, street, city, state, zip, phone, birth_date, sex, date_entered)
VALUES ('John', 'Doe', 'johndoe@example.com', 'Acme Inc.', '123 Main St', 'Anytown', 'CA', 12345, '555-555-1212', '1970-01-01', 'M', NOW());

INSERT INTO customer (first_name, last_name, email, company, street, city, state, zip, phone, birth_date, sex, date_entered)
VALUES ('Jane', 'Doe', 'janedoe@example.com', 'Acme Inc.', '123 Main St', 'Anytown', 'CA', 12345, '555-555-1212', '1970-01-01', 'F', NOW());


DELETE FROM customer WHERE first_name = 'John' AND last_name = 'Doe';
DELETE FROM customer WHERE first_name = 'Jane' AND last_name = 'Doe';

  