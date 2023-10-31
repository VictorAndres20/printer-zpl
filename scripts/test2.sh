curl --location --request POST 'localhost:8989/printer/print-rol' \
--header 'Content-Type: application/json' \
--data-raw '{
    "detail_id":"",
    "desc":"Carrete 1/2",
    "ref":"Ref: 1232312",
    "color":"Color: 123123",
    "mts":"MTS: 30000mt",
    "person":"Encargado: 045"
}'