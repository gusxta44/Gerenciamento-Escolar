import sys
import os
# Adiciona a raiz do projeto (Gerenciamento-Escolar) no caminho de busca do Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
# IMPORTAÇÃO CORRIGIDA: Puxa o Controller da pasta controller!
from App.controller.reportController import ReportController

def test_deve_barrar_criacao_de_ocorrencia_sem_descricao():
    with pytest.raises(ValueError, match="Falta a descricao"):
        ReportController.create(description="", studentID=1, parentID=2)

def test_deve_barrar_id_do_aluno_se_nao_for_inteiro():
    with pytest.raises(TypeError, match="ID incorreto"):
        ReportController.create(description="Aluno conversando", studentID="dois", parentID=2)

def test_deve_barrar_id_do_aluno_se_for_menor_ou_igual_a_zero():
    with pytest.raises(ValueError, match="Id invalido"):
        ReportController.create(description="Aluno conversando", studentID=0, parentID=2)
