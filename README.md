# Devgrid Process
Python Tech Test  of Devigrid process
`GET \?id=1`

**Response**
- `404 Not Found` don't have this id
```json
{
    "data": {},
    "message": "ID do not exists"
}
```
- `200 OK` for success
```json
{
  "data":{
    'complete percent': '100%',
    cities:[
    {
      "city":3439525,
      "humidity":93.0,
      "temp":20.68,
      "user_request_id":1
    }
    ]
  },
"message": "Process status"
}
```
## Create a new request of cities

`Post \`
**Args**
- `"id":int` user defined id
- `cities:list[int]`city ​​ids to collect data

**Response**
- `409 Conflict` don't have this id
```json
{
    "data": {},
    "message": "ID already exists"
}
```
- `202 Accepted` for success
```json
{
  "data":{
    'session': '{
		"id": 1,
		"num_cities":1,
		"time":"2021-11-02T21:47:12.093642"
    },
    cities:[
    {
      "city":3439525,
      "humidity":93.0,
      "temp":20.68,
      "user_request_id":1
    }
    ]
  },
"message": "Process status"
}
```
- `500 Internal error`erros with the serve or system

```json
{
    "data": {},
    "message": "unable to create"
}
