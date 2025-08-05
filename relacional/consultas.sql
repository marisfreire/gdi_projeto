
-- consulta Gio
-- lista o nome dos animais que receberam a vacina de raiva
-- Junta as tabelas ANIMAL, CARTEIRA_VACINA e VACINA 
-- filtra os registros onde a vacina aplicada é "Raiva" 
SELECT A.NOME AS NOME_ANIMAL 
FROM ANIMAL A JOIN CARTEIRA_VACINA CV ON A.ID_MICROCHIP = CV.ANIMAL_ID_MICROCHIP JOIN VACINA V ON CV.ID_CARTEIRA_VACINA = V.ID_CARTEIRA_VACINA 
WHERE UPPER(V.NOME_VACINA) = 'RAIVA';



