<p align="center">
   <a href="https://github.com/WesGtoX/be-the-hero">
     <img src="../frontend/src/assets/logo-be-the-hero.png" alt="Be The Hero" title="Be The Hero" width="250px">
   </a>
</p>

-----------------

# Be The Hero (Back-end)

Created with Node.js

- Routes / Resources

|Method  |Endpoint        |Description               |
|--------|----------------|--------------------------|
|`POST`  |`/sessions`     |ONG login.                |
|`POST`  |`/ongs`         |Register a ONG.           |
|`GET`   |`/ongs`         |List all ONGs.            |
|`POST`  |`/incidents`    |Register a incidents.     |
|`GET`   |`/incidents`    |List all incidents.       |
|`GET`   |`/profile`      |List a specific incidents.|
|`DELETE`|`/incidents/:id`|Delete a incidents.       |


- HTTP methods

  - GET: Fetching information from the back-end.
  - POST: Create information on the back-end.
  - PUT: Changing information on the back-end.
  - DELETE: Delete an information on the back-end.


- Parameter types

  - Query Params: Named parameters sent on the route after the `?` (Filters, Pagination).
  - Route Params: Parameters used to identify resources.
  - Request Body: Request body, used to create or change resources.


- Database

  - SQL: MySQL, SQLite, PostgreSQL, Oracle, Microsoft SQL Server.
  - NoSQL: MongoDB, CouchDB, etc.

  - Driver: SELECT * FROM users.
  - Query Builder: table('users').select('*').where().
