<p align="center">
  <a href="https://github.com/WesGtoX/be-the-hero">
    <img src="frontend/src/assets/logo-be-the-hero.png" alt="Be The Hero" title="Be The Hero" width="250px">
  </a>
</p>
<p align="center">
    <a href="https://app.netlify.com/sites/bethehero-wes/deploys" alt="Netlify Status">
        <img src="https://api.netlify.com/api/v1/badges/0f800fdc-5a62-4f73-ba6b-b150b929e209/deploy-status" />
    </a>
</p>

-----------------

# Be The Hero

Building using Node.js, React and React Native.

Author: [Wesley Mendes](https://github.com/WesGtoX)


## Mobile

[Be The Hero on Expo](https://expo.io/@wesgtox/bethehero)

<p align="center">
  <a href="https://expo.io/@wesgtox/bethehero">
    <img src="mobile/screenshots/screenshot_01.jpg" alt="Be The Hero Mobile" title="Be The Hero Mobile" width="250px">
  </a>
    <a href="https://expo.io/@wesgtox/bethehero">
    <img src="mobile/screenshots/screenshot_02.jpg" alt="Be The Hero Mobile" title="Be The Hero Mobile" width="250px">
  </a>
    <a href="https://expo.io/@wesgtox/bethehero">
    <img src="mobile/screenshots/screenshot_03.jpg" alt="Be The Hero Mobile" title="Be The Hero Mobile" width="250px">
  </a>
</p>


## Running the application:

To run this application locally, you'll need to:

- Clone this repository:
```bash
git clone https://github.com/WesGtoX/be-the-hero.git
cd be-the-hero/
```

- Run the API:
```bash
# Install dependencies:
yarn install

# Run database migrations:
npx knex migrate:latest

# Run the API:
yarn dev

# To run the tests:
yarn test
```

- Run the Web Application:
```bash
# Access the Web Application project folder:
cd frontend/

# Install dependencies:
yarn install

# Run the Web APP:
yarn start
```

- Run the Mobile Application:
```bash
# Access the Mobile project folder:
cd mobile/

# Install dependencies:
yarn install

# Run the Mobile APP:
yarn start

# Building Standalone Apps:
# Android
expo build:android -t apk

# iOS
expo build:ios
```

**Obs:** If you receive the error: `connect ECONNREFUSED 127.0.0.1: 19001`
```bash
# Leave it running in another terminal window:
expo start

# Then run the build again.
```


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


## License ##

[MIT](LICENSE)
