
-- consulta Gio
-- lista o nome dos animais que receberam a vacina de raiva
-- Junta as tabelas ANIMAL, CARTEIRA_VACINA e VACINA 
-- filtra os registros onde a vacina aplicada é "Raiva" 
SELECT A.NOME AS NOME_ANIMAL 
FROM ANIMAL A JOIN CARTEIRA_VACINA CV ON A.ID_MICROCHIP = CV.ANIMAL_ID_MICROCHIP JOIN VACINA V ON CV.ID_CARTEIRA_VACINA = V.ID_CARTEIRA_VACINA 
WHERE UPPER(V.NOME_VACINA) = 'RAIVA';


-- Consulta Mari
-- Agrupa os veterinários que passaram mais de uma receita 
SELECT P.NOME 
FROM PESSOA P
WHERE P.CPF IN (
	( SELECT V.CPF
	FROM VETERINARIO V
	WHERE V.CPF = P.CPF
	AND V.CPF IN (
	SELECT R.VET_CPF
	FROM RECEITA R
	WHERE R.VET_CPF = V.CPF
	GROUP BY R.VET_CPF
	HAVING COUNT(*) > 1
	)
	
))
;
