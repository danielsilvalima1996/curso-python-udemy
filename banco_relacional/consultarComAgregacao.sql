-- total por região
select
	regiao as 'Região',
    sum(populacao) as 'Total'
from estados
group by regiao
order by Total desc;

-- total
select
    sum(populacao) as 'Total'
from estados;

-- média
select
    avg(populacao) as 'Total'
from estados;