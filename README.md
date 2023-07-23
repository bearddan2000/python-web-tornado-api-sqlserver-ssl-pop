# python-web-tornado-api-sqlserver-ssl-pop

## Description
Simple api for a tornado project.
Creates and return table `pop`.

Sql server uses self-signed ssl.

## Tech stack
- python
- tornado
- sqlalchemy
- mssql

## Docker stack
- alpine:edge
- python
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu

## To run
`sudo ./install.sh -u`
- http://localhost/pop

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credit
- [HTTPServer config](https://phrase.com/blog/posts/tornado-web-framework-i18n/)
- [Code based on](https://www.tornadoweb.org/en/stable/)
- [Sqlalchemy code](https://medium.com/swlh/tornado-and-sqlalchemy-847eecbc0445)
