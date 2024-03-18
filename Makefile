VENV := .venv
BIN_DIR := $(HOME)/.local/bin
DIST_DIR := dist
APP := cht.py

setup:
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment..."; \
		python -m venv $(VENV); \
	fi
	@echo "Activating virtual environment..."
	. $(VENV)/bin/activate; \
	echo "Installing dependencies..."; \
	pip install -r requirements.txt

install:
	@echo "Building executable for $(APP)..."
	pyinstaller $(APP) --onefile
	@echo "Copying executable to $(BIN_DIR)..."
	cp $(shell pwd)/$(DIST_DIR)/cht $(BIN_DIR)

