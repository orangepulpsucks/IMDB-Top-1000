create table Movie (
    Poser_Link text not null,
    Series_Title text not null,
    Released_Year int not null,
    Certificate text not null,
    Runtime text not null,
    Genre text not null,
    IMDB_Rating text not null,
    Overview text not null,
    Meta_score text not null,
    Director text not null,
    Star1 text not null,
    Star2 text not null,
    Star3 text not null,
    Star4 text not null,
    No_of_Votes text not null,
    Gross text not null
);

-- create table set (
--     set_num text primary key,
--     name text not null,
--     year int not null,
--     theme_id int not null references theme(id),
--     num_parts int not null
-- );

-- create table inventory(
--     id int primary key,
--     version int not null,
--     set_num text not null references set(set_num)
-- );

-- create table inventory_set(
--     inventory_id int not null references inventory(id),
--     set_num text not null references set(set_num),
--     quantity int not null,
--     unique(inventory_id, set_num)
-- );

-- create table part_category(
--     id int primary key,
--     name text not null
-- );

-- create table part(
--     part_num text primary key,
--     name text not null,
--     part_cat_id int not null references part_category(id)
-- );

-- create table color (
--     id int primary key,
--     name text not null,
--     rgb text not null,
--     is_trans boolean not null
-- );

-- create table inventory_part(
--     inventory_id int not null references inventory(id),
--     part_num text not null, -- references part(part_num),
--     color_id int not null references color(id),
--     quantity int not null,
--     is_spare boolean not null,
--     primary key (inventory_id, part_num, color_id, is_spare)
-- );