<p align="center">
  <a href="https://github.com/WesGtoX/be-the-hero">
    <img src="../frontend/src/assets/logo-be-the-hero.png" alt="Be The Hero" title="Be The Hero" width="250px">
  </a>
</p>

-----------------

# Be The Hero (Back-end)

Created with Node.js.


## Documentation

### Routes / Resources

|Method  |Endpoint        |Description               |
|--------|----------------|--------------------------|
|`POST`  |`/sessions`     |ONG login.                |
|`POST`  |`/ongs`         |Register a ONG.           |
|`GET`   |`/ongs`         |List all ONGs.            |
|`POST`  |`/incidents`    |Register a incidents.     |
|`GET`   |`/incidents`    |List all incidents.       |
|`GET`   |`/profile`      |List a specific incidents.|
|`DELETE`|`/incidents/:id`|Delete a incidents.       |


### HTTP methods

- **GET:** _Fetching information from the back-end._
- **POST:** _Create information on the back-end._
- **PUT:** _Changing information on the back-end._
- **DELETE:** _Delete an information on the back-end._


### Parameter types

- **Query Params:** _Named parameters sent on the route after the `?` (Filters, Pagination)._
- **Route Params:** _Parameters used to identify resources._
- **Request Body:** _Request body, used to create or change resources._


### Database

- **SQL:** _MySQL, SQLite, PostgreSQL, Oracle, Microsoft SQL Server._
- **NoSQL:** _MongoDB, CouchDB, etc._

- **Driver:** _SELECT * FROM users._
- **Query Builder:** _table('users').select('*').where()._
