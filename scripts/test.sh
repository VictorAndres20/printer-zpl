curl --location --request POST 'localhost:8989/printer/print' \
--header 'Content-Type: application/json' \
--data-raw '{
    "detail_id":"12345678912",
    "client_name":"Cliente",
    "ref":"1232312",
    "color":"123123",
    "mts":"MTS: 30000mt",
    "kg":"KG: 5kg",
    "person":"045"
}'