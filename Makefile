.PHONY: install
install:
	@echo "Creating virtual environment. You may need to install venv."
	python3 -m venv env; \
	source ./env/bin/activate; \
	pip3 install pyautogui; \
	pip3 install AppKit; \
	pip3 install opencv-python;

.PHONY: run
run:
	@echo "Running program."
	./env/bin/python3 zoom_mate;
