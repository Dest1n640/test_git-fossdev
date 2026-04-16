create-structure:
ifndef NAME
	$(error Надо указать имя папки: make create-structure NAME=my_project)
endif
	mkdir -p $(NAME)/src $(NAME)/tests $(NAME)/docs
	touch $(NAME)/README.md $(NAME)/setup.py $(NAME)/requirements.txt
	touch $(NAME)/docs/DOMAIN.md
	touch $(NAME)/src/.gitkeep $(NAME)/tests/.gitkeep
	@echo "Проект $(NAME) успешно создан"
