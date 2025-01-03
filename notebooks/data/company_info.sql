create table company_info
    (
        comp_id int not null auto_increment,
        address_id int,
        gungu_id int,
        type_id int,
        comp_name varchar(32),
        foundation date,
        employees int,
        income int,
        primary key(comp_id),
        constraint FK_type_id foreign key (type_id) references comp_type(comp_type_id),
        constraint FK_address_id foreign key (address_id) references sido_type(sido_id),
        constraint FK_gu_id foreign key (gungu_id) references gungu_type(gungu_id)

    );