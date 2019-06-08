drop table if exists tag_md;
drop table if exists tags;
drop table if exists levels;
drop table if exists library;

create table tag_md(
	tag_id integer primary key autoincrement,
	tag_name text
);

create table tags(
	tag_link_id integer primary key autoincrement,
	child_id integer,
	parent_id integer,
	foreign key(child_id) references tag_md(tag_id),
	foreign key(parent_id) references tag_md(tag_id)
);

create table levels(
	level_id integer primary key autoincrement,
	level_name text
);

create table library(
	item_id integer primary key autoincrement,
	tag_id integer,
	reference text,
	level_low integer,
	level_high integer,
	foreign key(tag_id) references tag_md(tag_id),
	foreign key(level_low) references levels(level_id),
	foreign key(level_high) references levels(level_id)
);

insert into levels(level_name)
values 
('Aware that technique exists'),
('Can recognise terms used in articles on the technique'),
('Can read and understand article on the technique without looking up additional reference material'),
('Can reproduce results from article with help from the text with a full understanding of the individual steps'),
('Can reproduce results from article without any help'),
('Can apply methods in other scenarios'),
('Can freely use techniques in daily work'),
("Can teach techniques to others and contextualise to listener's situation"),
('Can use the technique for uncommon purposes'),
('Can develop new methodology around the technique');

