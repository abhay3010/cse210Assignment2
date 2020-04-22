.DEFAULT_GOAL := generate
generate: clean compile

clean-arith:
	rm ./while | true; \
	rm ./while.spec | true;

clean-venv:
	deactivate | true; \
	rm -rf ./pyenv | true;  

clean:clean-arith clean-venv
	rm -rf ./dist | true; \
	rm -rf ./build | true;
	 
build-venv:
	python -m venv ./pyenv; \
	source ./pyenv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r ./requirements.txt; \
	deactivate;

	
	
compile: build-venv
	source ./pyenv/bin/activate; \
	pyinstaller --onefile --distpath ./  --name ./while ./while-inter/main.py; \
	deactivate;
	

	
	



