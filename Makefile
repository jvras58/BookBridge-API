SHEll := /bin/zsh
.PHONY: venv

venv:
	@poetry run poetry install

commit:
	@echo "Revisar mudanças para este commit: "
	@echo "-------------------------------------"
	@git status -s 
	@echo "-------------------------------------"
	@read -p "Commit msg: " menssagem ; \
	git add . ;\
	git commit -m "$$menssagem" ;\

update:
	@git fetch origin
	@git pull
	@$(MAKE) venv

lint:
	task lint \
	task format

dev:
	@echo "Iniciando servidor em modo de desenvolvimento"
	@echo "-------------------------------------"
	export PYTHONPATH=/workspace && export FLASK_APP=app/startup.py && export FLASK_ENV=development && flask run --debug
	@echo "-------------------------------------"
	@echo "Servidor iniciado com sucesso"

prod:
	@echo "Iniciando servidor em modo de produção"
	@echo "-------------------------------------"
	export FLASK_APP=app/startup.py && export FLASK_ENV=production && flask run
	@echo "-------------------------------------"
	@echo "Servidor iniciado com sucesso"
	@echo "Acesse: http://localhost:5000"

routes:
	@echo "Listando rotas"
	@echo "-------------------------------------"
	export PYTHONPATH=/workspace && export FLASK_APP=app/startup.py && flask routes
	@echo "-------------------------------------"
	@echo "Rotas listadas com sucesso"

migrate:
	@read -p "Mensagem da migração: " msg ; \
	export PYTHONPATH=/workspace && export FLASK_APP=app/startup.py && flask db migrate -m "$$msg"

upgrade:
	@echo "Deseja realmente aplicar a ultima migração? (y/n)"
	@read -p "Resposta: " resposta ; \
	if [ $$resposta = "y" ]; then \
		export PYTHONPATH=/workspace && export FLASK_APP=app/startup.py && flask db upgrade ;\
	fi
	

downgrade:
	@echo "Deseja realmente reverter a ultima migração? (y/n)"
	@read -p "Resposta: " resposta ; \
	if [ $$resposta = "y" ]; then \
		export PYTHONPATH=/workspace && export FLASK_APP=app/startup.py && flask db downgrade ;\
	fi
	

init-db:
	@echo "Deseja Iniciar o Banco (Utilize apenas uma vez) [somente se migrations não existir]? (y/n)"
	@read -p "Resposta: " resposta ; \
	if [ $$resposta = "y" ]; then \
		export PYTHONPATH=/workspace && export FLASK_APP=app/startup.py && flask db init ;\
	fi
	@echo "Banco de dados iniciado com sucesso"
	@echo "Iniciando banco de dados "

test:
	@echo "Iniciando os Testes:"
	export PYTHONPATH=/workspace export FLASK_APP=app/startup.py && FLASK_ENV=testing && pytest
	
