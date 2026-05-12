insert or ignore into darbinieki values("D_03","Līze","Kalniņa", 26352712 ,43, "12.06.2018", 270);
insert or ignore into darbinieki values("D_04","Pēteris","Roze", 26497154 ,23 ,"12.07.2019", 210);


select * FROM darbinieki;
select Vards,Uzvards,Bonuss FROM darbinieki;
select max(Bonuss) from darbinieki;
select avg(Vecums) from darbinieki;
select min(vecums) from darbinieki;
select sum(Bonuss) from darbinieki;
