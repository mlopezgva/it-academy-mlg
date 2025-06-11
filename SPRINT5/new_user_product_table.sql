CREATE TABLE user_products AS
      SELECT user_id, transaction_id
           , product_id
           , CONCAT(u.name, ' ', u.surname) AS "Client Name"
           , p.product_name
           , p.price
        FROM product_transaction AS pt
        JOIN product             AS p  USING(product_id)
        JOIN `transaction`       AS t  USING(transaction_id)
        JOIN `user`              AS u  USING(user_id);
