all: srpm

tar:
	spectool -g bp4o.spec

srpm: tar
	fedpkg srpm

rpm: tar
	fedpkg local

.PHONY: all tar srpm rpm
