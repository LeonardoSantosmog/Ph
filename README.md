# 🧪 Sistema de Classificação de Substâncias com Base no pH

Este é um projeto simples em Python que solicita ao usuário um valor de pH e classifica a substância como **ácida**, **neutra** ou **básica**, com base no valor informado.

## 🎯 Objetivo

Praticar a entrada de dados (`input`), conversão de tipos (`float`) e uso de condicionais (`if`, `elif`, `else`) em Python, aplicando conceitos de química.

---

## ⚗️ Regras de Classificação

- **pH < 7**: Substância **Ácida**
- **pH == 7**: Substância **Neutra**
- **pH > 7**: Substância **Básica**
- **Fora da faixa 0 a 14**: Valor inválido

---

## 🚀 Como usar

1. Tenha o **Python 3** instalado em sua máquina.
2. Baixe ou clone o repositório:

```bash
git clone https://github.com/LeonardoSantosmog/seu-repositorio.git
```

3. Execute o script:

```bash
python classificacao_ph.py
```

4. Digite um valor de pH entre 0 e 14.

---

## 💬 Exemplo de uso

```bash
Digite um valor de pH entre 0 e 14: 3.5
Ácido
```

---

## 🧾 Código-fonte

```python
# Sistema de Classificação de Substâncias com Base no pH

# Solicita ao usuário um valor de pH
ph = float(input("Digite um valor de pH entre 0 e 14: "))

# Verifica se o valor está dentro do intervalo válido
if ph < 0 or ph > 14:
    print("Valor de pH inválido! Deve estar entre 0 e 14.")
elif ph > 7:
    print("Básico")
elif ph < 7:
    print("Ácido")
else:
    print("Neutro")
```

---

## 📄 Licença

Este projeto é livre para uso educacional e pessoal.

---

## 👨‍🔬 Autor

Desenvolvido por [Leonardo Santos](https://github.com/LeonardoSantosmog) ✨
