Для запуска достаточно клонировать репозиторий и запустить сервисы из файла docker_compose.

При первом запуске несмотря на то, что контейнеру тестов приказано ждать поднятия контейнера с браузером, 
тесты все равно могут постучаться в еще не поднявщийся браузер. Поэтому если при первом запуске все тесты упали,
стоит попробовать перезапустить только контейнер тестов.

Причина этого в том, что ожидание реализуется на уровне контейнеров и контейнер с тестами начинает подниматься только
когда контейнер с браузером поднят, но в поднятом контейнере еще поднимается сам браузер, и до готовности браузера 
тесты могут успеть поднять контейнер и подняться сами, из-за этого и возникает проблема.

Отдельно хочется отметить, что в CI такой проблемы не возникает, т.к. там как правильно инстансы браузера поднимаются 
в отдельной джобе предшествующей тестам.
