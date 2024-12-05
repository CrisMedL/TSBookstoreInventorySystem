from databaseConnection import DatabaseConnection
import tabulate

class Genre:
    def __init__(self,genre_id=None, genre_name= None):
        self.genre_id = genre_id
        self.genre_name = genre_name

    def addGenre(self):
        try:
            query = "INSERT INTO genres (genre_name) VALUES (%s)"
            params = (self.genre_name,)  
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Genre added successfully.")
        except Exception as e:
            if e.errno == 1062:
                print("Error: This genre name already exists in the system.")


    def updateGenre(self):
        try:
            query = "UPDATE genres SET genre_name = %s WHERE id = %s"
            params = (self.genre_name, self.genre_id)
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Genre updated successfully.")
        except Exception as e:
            print(f"Error updating genre: {e}")

        
    def deleteGenre(self):
        try:
            query = "DELETE FROM genres WHERE id = %s"
            params = (self.genre_id,) # execute_query expects a tuple
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Genre deleted successfully.")
        except Exception as e:
            if e.errno == 1451:  # Foreign key constraint error
                print("Error: This genre cannot be deleted because they are referenced by one or more books in the system.")


    def checkGenreExistsByName(self):
        query = "SELECT * FROM genres WHERE genre_name = %s"
        params = (self.genre_name,)
        try:
            with DatabaseConnection() as db:
                result = db.execute_query(query, params)
                if result:  # If a result is returned, the genre exists
                    return True
                else:
                    return False
        except Exception as e:
            print(f"Error checking genre: {e}")
            return False

    def checkGenreExistsById(self):
        query = "SELECT * FROM genres WHERE  = %s"
        params = (self.genre_id,)
        try:
            with DatabaseConnection() as db:
                result = db.execute_query(query, params)
                if result:# If a result is returned, the genre exists
                    return True
                else:
                    return False
        except Exception as e:
            print(f"Error checking genre: {e}")
            return False

    # Doesn't need parameters so we make it a static method
    @staticmethod
    def listGenres():
        try:
            query = "SELECT * FROM genres ORDER BY id"
            with DatabaseConnection() as db:
                genres = db.execute_query(query)
                # Prepare the data for tabulation
                headers = ["ID", "Genre"]  # Table headers
                # We gather table information as a tuple
                genre_data = [(genre[0], genre[1]) for genre in genres] 

                # Use tabulate to format and print the table
                # fmt is the format of the table, meaning how it looks.
                print(tabulate.tabulate(genre_data, headers=headers, tablefmt="pretty"))
        except Exception as e:
            print(f"Error listing genres: {e}")
        
