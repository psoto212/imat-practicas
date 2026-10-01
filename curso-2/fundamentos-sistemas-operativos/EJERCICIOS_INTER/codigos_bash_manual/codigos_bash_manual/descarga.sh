#!/bin/bash

wget --no-check-certificate -q --output-document francisco_goya.html https://simple.wikipedia.org/wiki/Francisco_de_Goya

curl https://simple.wikipedia.org/wiki/Francisco_de_Goya > francisco_goya_2.html
