def load_prompt(file_path):
    """
    Carrega o conteúdo do arquivo de prompt.
    """
    try:
        with open(file_path, 'r') as file:
            return " ".join(line.strip() for line in file)
    except FileNotFoundError:
        print(f"Erro: Arquivo de prompt não encontrado em {file_path}")
        return ""