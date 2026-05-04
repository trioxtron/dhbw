drop table if exists transaction;
drop table if exists product;
drop table if exists visit;
drop table if exists customer;

create table if not exists customer (
    id serial primary key,
    firstname varchar(50) not null,
    lastname varchar(50) not null,
    age int not null
);

create table if not exists visit (
    id serial primary key,
    customer_id int references customer(id),
    walk_in timestamp not null,
    walk_in timestamp with time zone default current_timestamp,
    walk_out timestamp with time zone default current_timestamp,
);

create table if not exists product (
    id serial primary key,
    name varchar(100) not null,
    price decimal(10,2) not null
);

create table if not exists transaction (
    visit_id int references visit(id),
    product_id int references product(id),
    amount int not null,
    primary key (visit_id, product_id)
);
