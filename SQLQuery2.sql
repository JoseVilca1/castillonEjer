SELECT * FROM USUARIO;
SELECT LOGEO, CLAVE, ESTADO
FROM USUARIO;

SELECT * FROM PRODUCTO;
SELECT COUNT(*) 
FROM USUARIO 
WHERE LOGEO = 'Ramirez_Paredes@gmail.com' 
  AND CLAVE = '52142' 
  AND ESTADO = 1;


SELECT 
  LOGEO, 
  CLAVE, 
  ESTADO, 
  LEN(LOGEO) AS LargoLOGEO, 
  LEN(CLAVE) AS LargoCLAVE
FROM USUARIO
WHERE LOGEO LIKE '%Ramirez_Paredes@gmail.com%';
