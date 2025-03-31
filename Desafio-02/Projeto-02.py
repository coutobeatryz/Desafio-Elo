import pandas as pd

tabela_1 = pd.DataFrame([
    [1, "Lucas", "Mendes", 100000, "20/02/2014", "RH"],
    [2, "Arthur", "Vern", 80000, "11/06/2014", "Administrador"],
    [3, "Alfred", "Singal", 300000, "20/02/2014", "RH"],
    [4, "Thiago", "Kumar", 500000, "20/02/2014", "RH"],
    [5, "Thais", "Argônio", 500000, "11/06/2014", "Administrador"],
    [6, "Angela", "Patel", 200000, "11/06/2014", "Contas a Pagar"],
    [7, "Ramon", "Silva", 75000, "20/01/2014", "Contas a Pagar"],
    [8, "Bernardo", "Costa", 90000, "11/04/2014", "TI"],
    [9, "Ligia", "Lamas", 90000, "10/04/2015", "Administrador"],
    [10, "Rafael", "Meira", 65000, "11/04/2015", "TI"],
    [11, "Nadine", "Schmit", 75000, "20/03/2014", "Contas a Pagar"],
    [12, "Luan", "Lien", 85000, "21/03/2014", "RH"]
], columns=["Worker_id", "Nome", "Sobrenome", "Salário", "Data de Contratação", "Departamento"])

tabela_2 = pd.DataFrame([
    [1, "Gerente", "20/02/2016"],
    [2, "Executivo", "11/06/2016"],
    [8, "Executivo", "11/06/2016"],
    [5, "Gerente", "11/06/2016"],
    [4, "Gerente Associado", "11/06/2016"],
    [7, "Gerente de Projetos", "11/06/2016"],
    [6, "Líder", "11/06/2016"]
], columns=["Worker_ref_id", "Título do Trabalhador", "Afetado Desde"])

merged_df = tabela_1.merge(tabela_2, left_on="Worker_id", right_on="Worker_ref_id", how="left")

max_salary = merged_df["Salário"].max()

highest_salary_roles = merged_df[merged_df["Salário"] == max_salary][["Título do Trabalhador", "Salário"]]

print("Cargos com os salários mais altos da companhia:")
print(highest_salary_roles)
