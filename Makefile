.PHONY: _pwd_prompt decrypt_conf encrypt_conf

CONF_FILE=.env

# 'private' task for echoing instructions
_pwd_prompt:
	@echo "Contact rukmal.weerawarana@gmail.com for the password."

# to create .env
decrypt_conf: _pwd_prompt
	openssl cast5-cbc -d -in ${CONF_FILE}.cast5 -out ${CONF_FILE}
	chmod +x ${CONF_FILE}

# for updating .env.cast5
encrypt_conf: _pwd_prompt
	openssl cast5-cbc -e -in ${CONF_FILE} -out ${CONF_FILE}.cast5

# run tests
test:
	pip install -r requirements.txt
	py.test -v tests/*