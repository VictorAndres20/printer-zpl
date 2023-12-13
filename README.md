# Deploy

- [OPTIONAL] May be create tar to upload in host server
````
tar -cvf printer-zpl.tar --exclude='printer-zpl/venv' --exclude='printer-zpl/.git' --exclude='printer-zpl/scripts' printer-zpl/
````
  
- [OPTIONAL] Create image specifying version x.x
````
docker build printer-zpl/ -t printer_zpl:x.x
````

- Create container
````
docker run --restart always --network network-ks-orders --ip 172.124.0.10 -e TZ=UTC+5 --name printer_zpl -p 8989:8989 -d printer_zpl:v.v
````
