# Projeto 02:
A EloGroup foi acionada por uma grande empresa de minério com o propósito de realizar um projeto de People Analytics, que visa analisar as pessoas, os cargos, salários e quantidade de mulheres em cargos de lideranças para, assim, garantir equidade dos salários.   Tarefa: O que esperamos nesse momento é que você, como estagiário de engenharia de dados da Elogroup, demonstre conhecimento dos dados disponibilizados e consiga desenvolver um código python para responder a pergunta abaixo.   Pergunta: Desenvolva um código em python para buscar o cargo que tem os salários mais altos na companhia, baseando-se nas duas tabelas que estão abaixo. Marque os cargos que têm os salários mais altos da companhia, de acordo com resultado do seu código:

# Tabela 01:
| Worker_id | Nome    | Sobrenome | Salário | Data de Contratação | Departamento     |
|-----------|---------|-----------|---------|----------------------|------------------|
| 1         | Lucas   | Mendes    | 100000  | 20/02/2014           | RH               |
| 2         | Arthur  | Vern      | 80000   | 11/06/2014           | Administrador    |
| 3         | Alfred  | Singal    | 300000  | 20/02/2014           | RH               |
| 4         | Thiago  | Kumar     | 500000  | 20/02/2014           | RH               |
| 5         | Thais   | Argônio   | 500000  | 11/06/2014           | Administrador    |
| 6         | Angela  | Patel     | 200000  | 11/06/2014           | Contas a Pagar   |
| 7         | Ramon   | Silva     | 75000   | 20/01/2014           | Contas a Pagar   |
| 8         | Bernardo| Costa     | 90000   | 11/04/2014           | TI               |
| 9         | Ligia   | Lamas     | 90000   | 10/04/2015           | Administrador    |
| 10        | Rafael  | Meira     | 65000   | 11/04/2015           | TI               |
| 11        | Nadine  | Schmit    | 75000   | 20/03/2014           | Contas a Pagar   |
| 12        | Luan    | Lien      | 85000   | 21/03/2014           | RH               |

# Tabela 02:
| Worker_ref_id | Título do Trabalhador    | Afetado Desde |
|---------------|--------------------------|---------------|
| 1             | Gerente                  | 20/02/2016    |
| 2             | Executivo                | 11/06/2016    |
| 8             | Executivo                | 11/06/2016    |
| 5             | Gerente                  | 11/06/2016    |
| 4             | Gerente Associado        | 11/06/2016    |
| 7             | Gerente de Projetos      | 11/06/2016    |
| 6             | Líder                    | 11/06/2016    |
