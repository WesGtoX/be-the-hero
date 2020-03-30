const request = require('supertest')
const app = require('../../src/app')
const connection = require('../../src/database/connection')

describe('POST /ongs, GET /incidents', () => {
  beforeEach( async () => {
    await connection.migrate.rollback()
    await connection.migrate.latest()
  })

  afterAll( async () => {
    await connection.destroy()
  })

  it('Should be able to create a new ONG and three INCIDENTS', async () => {
    ong = await request(app)
      .post('/ongs')
      .send({
        name: "APAD",
        email: "contato@apad.com.br",
        whatsapp: "551691999999",
        city: "Sertãozinho",
        uf: "SP",
      })
      .expect(200)
    expect(ong.body).toHaveProperty('id')
    expect(ong.body.id).toHaveLength(8)

    await request(app).post('/incidents').set('Authorization', ong.body.id)
      .send({
        title: "Caso Teste 1",
        description: "Detalhe do caso teste 1",
        value: 100
      })

    await request(app).post('/incidents').set('Authorization', ong.body.id)
      .send({
        title: "Caso Teste 2",
        description: "Detalhe do caso teste 2",
        value: 150
      })

    await request(app).post('/incidents').set('Authorization', ong.body.id)
      .send({
        title: "Caso Teste 3",
        description: "Detalhe do caso teste 3",
        value: 200
      })

    response = await request(app)
      .get('/incidents')
      .expect(200)

    expect(response.body).toHaveLength(3)
  })
})
