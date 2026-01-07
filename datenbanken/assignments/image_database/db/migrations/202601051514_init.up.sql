create table if not exists images (
    id serial primary key,
    filename varchar(255) not null,
    image_data bytea not null,  
    description varchar(500),
    embedding JSONB
);

create table if not exists tags (
    id serial primary key,
    name varchar(100) not null unique
);

create table if not exists image_tags (
    image_id integer not null,
    tag_id integer not null,
    primary key (image_id, tag_id),
    foreign key (image_id) references images(id) on delete cascade,
    foreign key (tag_id) references tags(id) on delete cascade
);
