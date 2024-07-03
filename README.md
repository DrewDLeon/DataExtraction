
# DataVisiooh Extraction Pipeline

Based on the way DataVisiooh works, we collect the data from the API, then make it a total, translate and then insert into BD.


## API Reference

#### Get customer info

```http
  GET /api/services/customers
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api-token` | `string` | **Required**. Your API key |

#### Get panels info

```http
  GET /api/services/customer-panels/{customer_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `customer_id`      | `string` | **Required**. Customer Id fetched |
| `api-token`      | `string` | **Required**. Your API key |

#### Get panels data hourly

```http
  GET /api/services/hourly-panel-data/{panel_id}?filters[start_date]={start_date}&filters[end_date]={end_date}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `customer-hash`      | `string` | **Required**. Customer Hash fetched |
| `api-token`      | `string` | **Required**. Your API key |
| `panel_id`      | `int` | **Required**. Customer Panel's Id |
| `start_date`      | `string` | **Required**. Format %Y-%m-%d %H:%M:%S |
| `end_date`      | `string` | **Required**. Format %Y-%m-%d %H:%M:%S |





## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`API URL's`

`DATABASE CREDENTIALS`



