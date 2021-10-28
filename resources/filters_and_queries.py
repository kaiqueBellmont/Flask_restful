def normalize_path_params(
        cidade: str = None,
        estrelas_min: float = 0,
        estrelas_max: float = 5,
        diaria_min: float = 0,
        diaria_max: float = 10000,
        limit: int = 50,
        offset: int = 0,
        **data) -> dict:
    if cidade:
        return {
            'estrelas_min': estrelas_min,
            'estrelas_max': estrelas_max,
            'diaria_min': diaria_min,
            'diaria_max': diaria_max,
            'cidade': cidade,
            'limit': limit,
            'offset': offset
        }
    return {
        'estrelas_min': estrelas_min,
        'estrelas_max': estrelas_max,
        'diaria_min': diaria_min,
        'diaria_max': diaria_max,
        'limit': limit,
        'offset': offset
    }


without_city_query = "SELECT * FROM hotels " \
                     "WHERE (estrelas >= ? and estrelas <= ?)" \
                     "and (diaria >= ? and diaria <= ?)" \
                     "LIMIT ? OFFSET ?"


with_city_query = "SELECT * FROM hotels " \
                    "WHERE(estrelas >= ? and estrelas <= ?)" \
                    "and (diaria >= ? and diaria <= ?)" \
                    "and cidade = ? LIMIT ? OFFSET ?"