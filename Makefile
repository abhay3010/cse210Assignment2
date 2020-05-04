.DEFAULT_GOAL := generate
generate: clean compile

clean-arith:
	rm ./while-ss | true; \
	rm ./while-ss.spec | true;

clean-venv:
	deactivate | true; \
	rm -rf ./pyenv | true;  

clean:clean-arith clean-venv
	rm -rf ./dist | true; \
	rm -rf ./build | true;
	 
build-venv:
	python3 -m venv ./pyenv; \
	source ./pyenv/bin/activate; \
	pip install --upgrade pip; \
	pip install -r ./requirements.txt; \
	deactivate;

	
	
compile: build-venv
	source ./pyenv/bin/activate; \
	pyinstaller --onefile --distpath ./  --name ./while-ss ./while-inter/main.py; \
	deactivate;
	

	
	



