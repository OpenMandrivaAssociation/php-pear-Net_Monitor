%define		_class		Net
%define		_subclass	Monitor
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.3.0
Release:	1
Summary:	Remote service monitor

License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_Monitor/
Source0:	http://download.pear.php.net/package/Net_Monitor-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
A unified interface for checking the availability services on external
servers and sending meaningful alerts through a variety of media if a
service becomes unavailable.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%doc %{upstream_name}-%{version}/doc/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
%{php_pear_dir}/data/Net_Monitor/README
%{php_pear_dir}/data/Net_Monitor/build.xml
%{php_pear_dir}/data/Net_Monitor/composer.json



