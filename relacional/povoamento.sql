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
('33333333333', 'PE', '3456', '11111111111');

-- ESPECIALIDADE
INSERT INTO ESPECIALIDADE VALUES 
('11111111111', 'Cirurgia'),
('11111111111', 'Dermatologia'),
('33333333333', 'Cardiologia');

-- TUTOR
INSERT INTO TUTOR VALUES 
('22222222222'),
('33333333333'), 
('44444444444'); 

-- ANIMAL
-- mudar id pra int
INSERT INTO ANIMAL VALUES 
('A123', 'Tobi', 'M', '2020-01-10'),
('B456', 'Alvin', 'F', '2019-07-23'),
('C789', 'Thor', 'M', '2021-03-15'), 
('C777', 'Rhaenyra', 'F', '2022-03-11'),
('D123', 'Dudu', 'M', '2022-01-18'),
('E456', 'Paçoca', 'F', '2025-03-23'),
('F789', 'Umbigo', 'M', '2010-10-15');

-- RESPONSAVEL
INSERT INTO RESPONSAVEL VALUES 
('A123', '22222222222'),
('B456', '33333333333'),
('C789', '22222222222'), 
('C777', '22222222222'),
('D123', '44444444444'),
('E456', '44444444444'),
('F789', '44444444444');

-- CONSULTA
INSERT INTO CONSULTA VALUES 
('2025-08-01 09:00:00', '11111111111', 'A123', '12345678000100'),
('2025-08-02 14:30:00', '11111111111', 'B456', '98765432000100'),
('2025-08-03 10:00:00', '33333333333', 'C789', '11112222000100'),
('2025-08-03 11:00:00', '33333333333', 'F789', '11112222000100'); 

-- RECEITA
-- mudar id pra int
INSERT INTO RECEITA VALUES 
('Tomar antibiótico por 7 dias', 'R001', '2025-08-01 09:00:00', '11111111111', 'A123'),
('Aplicar pomada 2x ao dia', 'R002', '2025-08-02 14:30:00', '11111111111', 'B456'),
('Suplemento vitamínico diário', 'R003', '2025-08-03 10:00:00', '33333333333', 'C789');

-- INTERNACAO
INSERT INTO INTERNACAO VALUES 
('2025-08-01 11:00:00', 'A123', 'Cirurgia de emergência'),
('2025-08-02 15:00:00', 'B456', 'Desidratação'),
('2025-08-03 16:30:00', 'C789', 'Recuperação pós-operatória');

-- REGISTRO_DIARIO
INSERT INTO REGISTRO_DIARIO VALUES 
('2025-08-01 18:00:00', 'A123', '2025-08-01 11:00:00', 'Animal estável após cirurgia'),
('2025-08-02 20:00:00', 'B456', '2025-08-02 15:00:00', 'Melhora no quadro clínico'),
('2025-08-03 22:00:00', 'C789', '2025-08-03 16:30:00', 'Animal se alimentando bem');

-- CARTEIRA_VACINA
INSERT INTO CARTEIRA_VACINA VALUES 
('CV001', 'A123'),
('CV002', 'B456'),
('CV003', 'C789'), 
('CV004', 'C777');

-- VACINA
INSERT INTO VACINA VALUES 
('V10', '2026-08-01', 'CV001'),
('Raiva', '2026-08-02', 'CV002'),
('Gripe', '2026-08-03', 'CV003'), 
('Raiva', '2026-08-02', 'CV004');

