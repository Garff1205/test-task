class QueriesCustomers:
    GET_ALL_DATA = "SELECT * FROM Customers;"

    @staticmethod
    def GET_BY_CITY(city: str):
        # Используем небезопасную сборку запроса потому, что эти запросы не общаются к базе данных а лишь печатаются.
        # Ну и мы пишем тесты, поэтому зачем упрощать жизнь системе и проверять запрос на инъекции за нее)))
        return f"SELECT * FROM Customers WHERE City = '{city}';"

    # В будуем возможно еще понадобится метод Upsert, тогда можно будет добавить в этот ON CONFLICT DO UPDATE
    # Либо создать его копию и доработать ее.

    @staticmethod
    def GET_BY_CUSTOMER_ID(customer_id: str):
        # Используем небезопасную сборку запроса потому, что эти запросы не общаются к базе данных а лишь печатаются.
        # Ну и мы пишем тесты, поэтому зачем упрощать жизнь системе и проверять запрос на инъекции за нее)))
        return f"SELECT * FROM Customers WHERE CustomerID = '{customer_id}';"

    # В будуем возможно еще понадобится метод Upsert, тогда можно будет добавить в этот ON CONFLICT DO UPDATE
    # Либо создать его копию и доработать ее.

    @staticmethod
    def ADD_NEW_ROW(table: str, row_data: dict):
        keys = f"({','.join(row_data.keys())})"
        vals = [[] for _ in range(len(row_data.values()))]
        for val in row_data.values():
            if type(val) in [list, tuple]:
                for i, v in enumerate(val):
                    vals[i].append(v)
            else:
                vals = None
                break
        if vals:
            for i, val in enumerate(vals):
                vals[i] = [f"'{v}'" for v in val]
            ready_vals = [f"({','.join(v)})" for v in vals]
        else:
            ready_vals = [f"'{val}'" for val in row_data.values()]
        values = f"({','.join(ready_vals)})"
        return f"INSERT INTO {table} {keys} VALUES {values};"

    @staticmethod
    def UPDATE_ROW(row_data: dict, condition):
        values = ",".join(f"{key} = '{val}'" for key, val in row_data.items())
        return f"UPDATE Customers SET {values} WHERE {condition};"
