from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView


class IndexView(TemplateView):
    template_name = 'index.html'


class DadosJSONView(BaseLineChartView):

    def get_labels(self):
        #retorna 12 labels para a representação do x
        labels =  [
            "Janeiro", 
            "Fevereiro", 
            "Março", 
            "Abril", 
            "Maio", 
            "Junho", 
            "Julho", 
            "Agosto", 
            "Setembro", 
            "Outubro", 
            "Novembro", 
            "Dezembro"]

        return labels


    def get_providers(self):
        #retorna o nome dos datasets

        datasets = [
            "Programação para Leigos",
            "Algoritmo e Lógica de programação",
            "Programação em C",
            "Programação em Java",
            "Programação em Python",
            "Banco de Dados"]
        return datasets

    def get_data(self):
        #retorna 6 datasets para lotar o gráfico
        #cada linha representa um dataset
        #cada coluna representa um label
        #a quantidade de dados precisa ser igual aos datasets/labels
        #12 colunas 6 linhas
        dados = []
        for l in range(6):
            for c in range(12):
                dado = [
                    randint(1, 100), # Jan
                    randint(1, 100), # Fev
                    randint(1, 100), # Mar
                    randint(1, 100), # Abr
                    randint(1, 100), # Mai
                    randint(1, 100), # Jun
                    randint(1, 100), # Jul
                    randint(1, 100), # Ago
                    randint(1, 100), # Set
                    randint(1, 100), # Out
                    randint(1, 100), # Nov
                    randint(1, 100) ]  # Dez
            dados.append(dado)
        return dados