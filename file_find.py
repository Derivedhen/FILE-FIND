import sys
from os import system
from time import sleep

msg_file_find = str("FILE FIND TOOL")
msg_version = str("VERSION: 1.1")
msg_code_by = str("Code By: Derived")

if len(sys.argv) < 2:
	print("---------------------------------------------------------")
	print(f"|--                  {msg_file_find}                   --|")
	print(f"|--                   {msg_version}                    --|")
	print(f"|--                 {msg_code_by}                  --|")
	print("---------------------------------------------------------")
	print("|- MODO DE USO: python3 filefind.py dominio.com.br pdf -|")
	print("|- MODO DE USO: python3 filefind.py dominio.com.br txt -|")
	print("|- MODO DE USO: python3 filefind.py dominio.com.br asp -|")
	print("---------------------------------------------------------")

else:
	dominio = sys.argv[1]
	filetype = sys.argv[2]

	print("---------------------------------------------------------")
	print(f"|--                  {msg_file_find}                   --|")
	print(f"|--                   {msg_version}                    --|")
	print(f"|--                 {msg_code_by}                  --|")
	print("---------------------------------------------------------")
	print("\033[34m[*] PROCURANDO ARQUIVOS...\033[m")
	sleep(4)
	print("-" * 57)

	# REALIZA UM GOOGLE DORKS PELO DOMÍNIO E TIPO DE ARQUIVO
	system(f'lynx --dump "https://google.com/search?q=site:{dominio}+ext:{filetype}" | grep ".{filetype}" | cut -d "=" -f2 | egrep -v "site|google" | sed "s/...$//" > links_{filetype}')

	# TRANSFORMANDO OS LINKS EM UMA LISTA PARA SEREM LIDOS PELO LAÇO FOR
	dir_arquivo = str(f"links_{filetype}")
	arquivo = open(dir_arquivo)
	links = arquivo.readlines()

	if len(links) == 0:
		print("\033[31m[X] ARQUIVOS NÃO ENCONTRADOS :(\033[m")
		sleep(4)
		print("-" * 57)
		system(f"rm links_{filetype}")

	else:
		print("\033[32m[!] ARQUIVOS ENCONTRADOS:\033[m")
		print("-" * 57)
		print(system(f'cat links_{filetype}'))
		print("-" * 57)
		sleep(3)
		print("\033[32m[!] REALIZANDO O DOWNLOAD...\033[m")


		# REALIZA O DOWNLOAD DOS ARQUIVOS
		for url in links:
			system(f'wget -q {url} ')

		# EXCLUI OS ARQUIVOS DE LINKS
		system(f"rm links_{filetype}")

		print("-" * 57)
		print("\033[32m[*] DOWNLOAD CONCLUÍDO. EXTRAIA OS METADADOS E VISUALIZE O CONTEÚDO :D\033[m")
		sleep(4)
		print("-" * 57)
		system("ls -l")
		print("-" * 57)
