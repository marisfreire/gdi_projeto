-- BRUCE RHAENYRA DUDU ALVIN MIA KIKI NYA LUA PAÇOCA UMBIGO 

-- povoamento da tabela PESSOAS

-- povoamento da tabela TEL_PESSOAS

-- povoamento da tabela ESPECIALIDADE

-- povoamento da tabela CONSULTORIO

-- povoamento da tabela VETERINARIO

-- povoamento da tabela TUTOR

-- povoamento da tabela RESPONSAVEL

-- povoamento da tabela ANIMAL

-- povoamento da tabela CONSULTA

-- povoamento da tabela RECEITA

-- povoamento da tabela INTERNACAO

-- povoamento da tabela REGISTRO_DIARIO

-- povoamento da tabela CARTEIRA_VACINA

-- PESSOA
INSERT INTO PESSOA VALUES 
('11111111111', 'Ana Silva', '1985-06-12', 'Rua A', '123', 'Centro', 'Recife', 'PE', '50000000'),
('22222222222', 'Carlos Souza', '1990-02-28', 'Rua B', '456', 'Boa Vista', 'Olinda', 'PE', '53000000'),
('33333333333', 'Beatriz Lima', '1978-11-03', 'Rua C', '789', 'Casa Forte', 'Jaboatão', 'PE', '54000000');

-- TEL_PESSOA
INSERT INTO TEL_PESSOA VALUES 
('81999998888', '11111111111'),
('81988887777', '22222222222'),
('81977776666', '33333333333');

-- CONSULTORIO
INSERT INTO CONSULTORIO VALUES 
('12345678000100', 'Clínica VetVida', 'Av. Recife, 1000'),
('98765432000100', 'Clínica Animais&Cia', 'Rua Olinda, 222'),
('11112222000100', 'Hospital PetAmor', 'Av. Boa Viagem, 333');

-- VETERINARIO (um é supervisor do outro)
INSERT INTO VETERINARIO VALUES 
('11111111111', 'PE', '1234', NULL),
('22222222222', 'PE', '2345', '11111111111'),
('33333333333', 'PE', '3456', '11111111111');

-- ESPECIALIDADE
INSERT INTO ESPECIALIDADE VALUES 
('11111111111', 'Cirurgia'),
('22222222222', 'Dermatologia'),
('33333333333', 'Cardiologia');

-- TUTOR
INSERT INTO TUTOR VALUES 
('22222222222'),
('33333333333'),
('11111111111');

-- ANIMAL
INSERT INTO ANIMAL VALUES 
('A123', 'Tobi', 'M', '2020-01-10'),
('B456', 'Alvin', 'F', '2019-07-23'),
('C789', 'Thor', 'M', '2021-03-15');

-- RESPONSAVEL
INSERT INTO RESPONSAVEL VALUES 
('A123', '22222222222'),
('B456', '33333333333'),
('C789', '11111111111');

-- CONSULTA
INSERT INTO CONSULTA VALUES 
('2025-08-01 09:00:00', '11111111111', 'A123', '12345678000100'),
('2025-08-02 14:30:00', '22222222222', 'B456', '98765432000100'),
('2025-08-03 10:00:00', '33333333333', 'C789', '11112222000100');

-- RECEITA
INSERT INTO RECEITA VALUES 
('Tomar antibiótico por 7 dias', 'R001', '2025-08-01 09:00:00', '11111111111', 'A123'),
('Aplicar pomada 2x ao dia', 'R002', '2025-08-02 14:30:00', '22222222222', 'B456'),
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
('CV003', 'C789');

-- VACINA
INSERT INTO VACINA VALUES 
('V10', '2026-08-01', 'CV001'),
('Raiva', '2026-08-02', 'CV002'),
('Gripe', '2026-08-03', 'CV003');

