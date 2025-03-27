from datetime import datetime
from dateutil.relativedelta import relativedelta


def historico_parcelas(data: datetime, parc: int, val_parc: float) -> None:
    fmt = "%d/%m/%Y %H:%M:%S"
    nova_data = data
    for i in range(1, parc+1):
        print(f"{i} parcela mês {datetime.strftime(nova_data, fmt)}\
        valor R${val_parc:,.2f}")
        nova_data = data + relativedelta(months=i)


def emprestimo(valor: float | int, anos: int) -> None:
    parcelas = anos * 12
    data_emprestimo = datetime(2020, 12, 20)
    valor_parcelado = round(valor / parcelas, 2)
    historico_parcelas(data_emprestimo, parcelas, valor_parcelado)


emprestimo(1_000_000, 5)
