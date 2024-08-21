from Paciente import Paciente
from Funcionario import Funcionario
from Consulta import Consulta
from Medicamento import Medicamento
from Estoque import Estoque

# Criando pacientes
paciente1 = Paciente("Maria", 30, "PR123")
paciente2 = Paciente("João", 45, "PR456")

# Criando funcionários
medico = Funcionario("Dr. Carlos", "Médico", "Diurno")
enfermeiro = Funcionario("Enfermeira Ana", "Enfermeira", "Noturno")

# Criando consultas
consulta1 = Consulta(paciente1, medico, "2024-09-01")
consulta2 = Consulta(paciente2, enfermeiro, "2024-09-02")

# Criando e gerenciando estoque de medicamentos
estoque = Estoque()
medicamento1 = Medicamento("Paracetamol", "LT123", "2025-06")
medicamento2 = Medicamento("Amoxicilina", "LT456", "2025-12")
estoque.adicionar_medicamento(medicamento1)
estoque.adicionar_medicamento(medicamento2)

# Exibindo informações
print(paciente1)
print(medico)
print(consulta1)
print("\nMedicamentos no Estoque:")
for medicamento in estoque.listar_medicamentos():
    print(medicamento)

# Exemplo de interação entre diferentes módulos
print("\nDetalhes das Consultas Agendadas:")
print(consulta1)
print(consulta2)
