%define release %(/bin/date +"%Y%m%d.%H%M")

Name:    lua-resty-kafka
Version: 0.08.2
Release: 1%{?dist}
Summary: HMAC functions for ngx_lua and LuaJIT
License: BSD
Source0: %{name}.tar.gz
Group:   Openresty/Lua
URL:     https://github.com/Mjolkhare/lua-resty-kafka

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Lua Kafka client driver for the ngx_lua based on the cosocket API

%if %{?GBRANCH:1}%{!?GBRANCH:0} && %{?GCOMMIT:1}%{!?GCOMMIT:0}
It was built from repo: %{url}
Branch: %{GBRANCH}
Commit: %{GCOMMIT}
%endif

%prep
%setup -q -n %{name}

%install
install -d -m 0755 %{buildroot}/usr/share/lua/5.1/nginx/resty/kafka
cp -aR resty/kafka/*.lua %{buildroot}/usr/share/lua/5.1/nginx/resty/kafka

%files
%dir /usr/share/lua/5.1/nginx/resty/kafka
/usr/share/lua/5.1/nginx/resty/kafka/*.lua

%changelog