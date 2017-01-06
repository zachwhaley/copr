all: srpm

tar:
	spectool -g bp4o.spec

srpm: tar
	fedpkg --dist f25 srpm

rpm: tar
	fedpkg --dist f25 local

.PHONY: all tar srpm rpm
