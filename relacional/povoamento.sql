-- PESSOA
INSERT INTO PESSOA VALUES 
('11111111111', 'Ana Silva', '1985-06-12', 'Rua A', '123', 'Centro', 'Recife', 'PE', '50000000'),
('22222222222', 'Carlos Souza', '1990-02-28', 'Rua B', '456', 'Boa Vista', 'Olinda', 'PE', '53000000'),
('33333333333', 'Beatriz Lima', '1978-11-03', 'Rua C', '789', 'Casa Forte', 'Jaboatão', 'PE', '54000000'),
('44444444444', 'Maria Fátima', '2003-04-11', 'Rua D', '934', 'Várzea', 'Recife', 'PE', '56000000'),
('55555555555', 'Robson Fidalgo', '1970-12-04', 'Rua D', '934', 'Iputinga', 'Recife', 'PE', '57000000'),
('66666666666', 'Paulo Gustavo', '2005-01-20', 'Rua E', '101', 'Graças', 'Recife', 'PE', '59000000'),
('77777777777', 'Andson Baladeiro', '1980-06-13', 'Rua F', '112', 'Madalena', 'Recife', 'PE', '51000000');

-- TEL_PESSOA
INSERT INTO TEL_PESSOA VALUES 
('81999998888', '11111111111'),
('81988887777', '22222222222'),
('81977776666', '33333333333'),
('81966666666', '44444444444'), 
('81922222222', '55555555555'),
('81988888888', '66666666666'),
('81999999999', '77777777777'); 

-- CONSULTORIO
INSERT INTO CONSULTORIO VALUES 
('12345678000100', 'Clínica VetVida', 'Av. Recife, 1000'),
('98765432000100', 'Clínica Animais&Cia', 'Rua Olinda, 222'),
('11112222000100', 'Hospital PetAmor', 'Av. Boa Viagem, 333');

-- VETERINARIO (um é supervisor do outro)
INSERT INTO VETERINARIO VALUES 
('11111111111', 'PE', '1234', NULL),
('33333333333', 'PE', '3456', '11111111111'),
('66666666666', 'PE', '7891', '11111111111');

-- ESPECIALIDADE
INSERT INTO ESPECIALIDADE VALUES 
('11111111111', 'Cirurgia'),
('11111111111', 'Dermatologia'),
('33333333333', 'Cardiologia'),
('66666666666', 'Cirurgia');

-- TUTOR
INSERT INTO TUTOR VALUES 
('22222222222'),
('33333333333'), 
('44444444444'); 

-- ANIMAL
-- mudar id pra int
INSERT INTO ANIMAL VALUES 
( 1, 'Tobi', 'M', '2020-01-10'),
( 2, 'Alvin', 'F', '2019-07-23'),
( 3, 'Thor', 'M', '2021-03-15'), 
( 4, 'Rhaenyra', 'F', '2022-03-11'),
( 5, 'Dudu', 'M', '2022-01-18'),
( 6, 'Paçoca', 'F', '2025-03-23'),
( 7, 'Umbigo', 'M', '2010-10-15');

-- RESPONSAVEL
INSERT INTO RESPONSAVEL VALUES 
( 1, '22222222222'),
( 2, '33333333333'),
( 3, '22222222222'), 
( 4, '22222222222'),
( 5, '44444444444'),
( 6, '44444444444'),
( 7, '44444444444');

-- CONSULTA
INSERT INTO CONSULTA VALUES 
('2025-08-01 09:00:00', '11111111111',  1, '12345678000100'),
('2025-08-02 14:30:00', '11111111111',  2, '98765432000100'),
('2025-08-03 10:00:00', '33333333333',  3, '11112222000100'),
('2025-08-03 11:00:00', '33333333333',  7, '11112222000100'),
('2025-07-12 10:00:20', '66666666666', 4, '11112222000100');

-- RECEITA
INSERT INTO RECEITA VALUES 
('Ração especial por 60 dias', 4, '2025-07-12 10:00:20', '66666666666', 4),
('Pingar remédio pela manhã e noite', 5, '2025-07-12 10:00:20', '66666666666', 4),
('Tomar antibiótico por 7 dias', 1, '2025-08-01 09:00:00', '11111111111',  1),
('Aplicar pomada 2x ao dia', 2, '2025-08-02 14:30:00', '11111111111',  2),
('Suplemento vitamínico diário', 3, '2025-08-03 10:00:00', '33333333333',  3);

-- INTERNACAO
INSERT INTO INTERNACAO VALUES 
('2025-08-01 11:00:00',  1, 'Cirurgia de emergência'),
('2025-08-02 15:00:00',  2, 'Desidratação'),
('2025-08-03 16:30:00',  3, 'Recuperação pós-operatória');

-- REGISTRO_DIARIO
INSERT INTO REGISTRO_DIARIO VALUES 
('2025-08-01 18:00:00',  1, '2025-08-01 11:00:00', 'Animal estável após cirurgia'),
('2025-08-02 20:00:00',  2, '2025-08-02 15:00:00', 'Melhora no quadro clínico'),
('2025-08-03 22:00:00',  3, '2025-08-03 16:30:00', 'Animal se alimentando bem');

-- CARTEIRA_VACINA
INSERT INTO CARTEIRA_VACINA VALUES 
(1,  1),
(2,  2),
(3,  3), 
(4,  4);

-- VACINA
INSERT INTO VACINA VALUES 
('V10', '2026-08-01', 1),
('Raiva', '2026-08-02', 2),
('Gripe', '2026-08-03', 3), 
('Raiva', '2026-08-02', 4);

