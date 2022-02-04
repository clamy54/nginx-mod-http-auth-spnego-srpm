%global nginx_moduledir %{_libdir}/nginx/modules
%global nginx_moduleconfdir %{_datadir}/nginx/modules

Name:           nginx-mod-http-auth-spnego
Version:        1.20.1
Release:        1%{?dist}
Summary:        WAPT Server nginx kerberos module 

Group:          Development/Tools
License:        GPL
URL:            https://github.com/stnoonan/spnego-http-auth-nginx-module
Source0:        https://nginx.org/download/nginx-%{version}.tar.gz
Source1:        spnego-http-auth-nginx-module.tar.gz

BuildRequires:  gcc
BuildRequires:  make 
BuildRequires:  krb5-devel
BuildRequires:  zlib-devel
Requires:       krb5-workstation
Requires:       nginx

%description
WAPT Server nginx kerberos module

%prep
%setup -a 1 -n nginx-%{version}


%build
./configure --with-compat --add-dynamic-module=spnego-http-auth-nginx-module
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -p -d -m 0755 %{buildroot}%{nginx_moduledir}
install -p -d -m 0755 %{buildroot}%{nginx_moduleconfdir}
install -p -m 0644 ./objs/ngx_http_auth_spnego_module.so %{buildroot}%{nginx_moduledir}/ngx_http_auth_spnego_module.so

echo 'load_module "%{nginx_moduledir}/ngx_http_auth_spnego_module.so";' \
    > %{buildroot}%{nginx_moduleconfdir}/mod-http-auth-spnego.conf



%files
%{nginx_moduleconfdir}/mod-http-auth-spnego.conf
%{nginx_moduledir}/ngx_http_auth_spnego_module.so


%changelog
* Fri Feb 04 2022 Cyril Lamy <root@be-root.com> - 1:1.20.1-1
- First release for Centos 7
