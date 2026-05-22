from fortune_cookie import fortune

print(f'Esperado: Feedback de mensagem adicionada ou repetida\nResultado: {fortune(1, "Assista Jogos Vorazes")}\n')
print(f'Esperado: Fortuna aleatória\nResultado: {fortune(2)}')
print(f'Esperado: Erro\nResultado: {fortune(3)}')