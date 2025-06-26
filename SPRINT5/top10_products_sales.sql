/**
 * Query SQL que sirve de base para na consulta DAX que debería traer
 * los mismos resultados.
 */
SELECT product_name, price
     , COUNT(transaction_id)   AS transaction_count
     , COUNT(DISTINCT user_id) AS buyers_count
  FROM user_products
 GROUP BY product_name, price
 ORDER BY 3 DESC, 4 DESC,2 DESC
 LIMIT 50;
