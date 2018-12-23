#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-PKI
Version  : 0.1.5.1
Release  : 13
URL      : https://cran.r-project.org/src/contrib/PKI_0.1-5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/PKI_0.1-5.1.tar.gz
Summary  : Public Key Infrastucture for R Based on the X.509 Standard
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-PKI-lib = %{version}-%{release}
Requires: R-base64enc
Requires: R-gmp
BuildRequires : R-base64enc
BuildRequires : R-gmp
BuildRequires : buildreq-R
BuildRequires : openssl-dev

%description
No detailed description available

%package lib
Summary: lib components for the R-PKI package.
Group: Libraries

%description lib
lib components for the R-PKI package.


%prep
%setup -q -c -n PKI

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542430843

%install
export SOURCE_DATE_EPOCH=1542430843
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library PKI
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library PKI
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library PKI
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library PKI|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/PKI/DESCRIPTION
/usr/lib64/R/library/PKI/INDEX
/usr/lib64/R/library/PKI/LICENSE
/usr/lib64/R/library/PKI/Meta/Rd.rds
/usr/lib64/R/library/PKI/Meta/features.rds
/usr/lib64/R/library/PKI/Meta/hsearch.rds
/usr/lib64/R/library/PKI/Meta/links.rds
/usr/lib64/R/library/PKI/Meta/nsInfo.rds
/usr/lib64/R/library/PKI/Meta/package.rds
/usr/lib64/R/library/PKI/NAMESPACE
/usr/lib64/R/library/PKI/NEWS
/usr/lib64/R/library/PKI/R/PKI
/usr/lib64/R/library/PKI/R/PKI.rdb
/usr/lib64/R/library/PKI/R/PKI.rdx
/usr/lib64/R/library/PKI/certs/RForge-ca.crt
/usr/lib64/R/library/PKI/certs/demo.crt
/usr/lib64/R/library/PKI/help/AnIndex
/usr/lib64/R/library/PKI/help/PKI.rdb
/usr/lib64/R/library/PKI/help/PKI.rdx
/usr/lib64/R/library/PKI/help/aliases.rds
/usr/lib64/R/library/PKI/help/paths.rds
/usr/lib64/R/library/PKI/html/00Index.html
/usr/lib64/R/library/PKI/html/R.css
/usr/lib64/R/library/PKI/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/PKI/libs/PKI.so
/usr/lib64/R/library/PKI/libs/PKI.so.avx2
/usr/lib64/R/library/PKI/libs/PKI.so.avx512
