hora = str(input('Que horas você está vendo isso?'))
if hora[0:2] in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
    print(f'Bom dia, são exatamente {hora}')
elif hora[0:2] in ['13', '14', '15', '16', '17', '18']:
    print(f'Boa tarde, são exatamente {hora}')
elif hora[0:2] in ['19', '20', '21', '22', '23', '00']:
    print(f'Boa noite, são exatamente {hora}')
