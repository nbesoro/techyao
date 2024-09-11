echo POSTGRES_USER=$POSTGRES_USER >> ./.env
echo POSTGRES_PASSWORD=$POSTGRES_PASSWORD >> ./.env
echo POSTGRES_DB=$POSTGRES_DB >> ./.env

echo SQL_ENGINE=django.db.backends.postgresql >> ./.env
echo SQL_DATABASE=$POSTGRES_DB >> ./.env
echo SQL_USER=$POSTGRES_USER >> ./.env
echo SQL_HOST=db >> ./.env
echo SQL_PASSWORD=$POSTGRES_PASSWORD >> ./.env
echo SQL_PORT=$SQL_PORT >> ./.env
echo USE_POSTGRES_DATABASE=1 >> ./.env