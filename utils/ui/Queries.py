class QueriesCustomers:
    GET_ALL_DATA = "SELECT * FROM Customers;"

    @staticmethod
    def GET_BY_CITY(city: str):
        # We use insecure query creation because they are not sending to db but only wrote to the field.
        # And this is tests, so it can be another case.
        return f"SELECT * FROM Customers WHERE City = '{city}';"

    @staticmethod
    def GET_BY_CUSTOMER_ID(customer_id: str):
        return f"SELECT * FROM Customers WHERE CustomerID = '{customer_id}';"

    # Maybe in future we will need upsert method. In that case we can modify this method with ON CONFLICT DO UPDATE.
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
