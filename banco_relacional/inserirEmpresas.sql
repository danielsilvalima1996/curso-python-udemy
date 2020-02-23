INSERT INTO empresas
	(nome, cnpj)
VALUES
	('Bradesco', 95694114785236),
    ('Vale', 98654231479624),
    ('Cielo', 57946321469854);
    
ALTER TABLE empresas MODIFY cnpj VARCHAR(14);

desc empresas;

INSERT INTO empresas_unidades
	(empresa_id, cidade_id, sede)
VALUES
	(1,1,1),
    (1,2,0),
    (2,1,0),
    (2,2,1);