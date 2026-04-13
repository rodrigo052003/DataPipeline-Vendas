-- Total de vendas
SELECT SUM(vendas) FROM vendas;

-- Vendas por categoria
SELECT categoria, SUM(vendas)
FROM vendas
GROUP BY categoria;

-- Lucro por região
SELECT regiao, SUM(lucro)
FROM vendas
GROUP BY regiao;

-- Top produtos
SELECT produto, SUM(vendas) as total
FROM vendas
GROUP BY produto
ORDER BY total DESC;
