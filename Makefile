all: srpm

tar:
	spectool -g bp4o.spec

srpm: tar
	fedpkg --dist f24 srpm

rpm: tar
	fedpkg --dist f24 local

.PHONY: all tar srpm rpm
