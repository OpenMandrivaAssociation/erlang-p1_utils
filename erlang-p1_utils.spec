%global srcname p1_utils
# Erlang packages do not provide debug subpackages
%global debug_package %{nil}


Name:       erlang-%{srcname}
Version:    1.0.5
Release:    %mkrel 1
Group:      Development/Erlang
Summary:    Erlang utility modules from ProcessOne

License:    ASL 2.0
URL:        https://github.com/processone/p1_utils/
Source0:    https://github.com/processone/p1_utils/archive/%{version}.tar.gz

BuildRequires: erlang-rebar


%description
p1_utils is an application containing ProcessOne modules and tools that are
leveraged in other development projects.


%prep
%autosetup -n %{srcname}-%{version}
# This file was 755 upstream, which causes an rpmlint warning. This pull request has
# been created to fix the issue upstream:
# https://github.com/processone/p1_utils/pull/4
chmod 0644 doc/style.css


%build
%{rebar_compile}
%{rebar_doc}


%install
%{erlang_install}


%files
%license LICENSE.txt
%doc CHANGELOG.md
%doc doc
%doc README.md
%{erlang_appdir}




%changelog
* Thu Nov 17 2016 neoclust <neoclust> 1.0.5-1.mga6
+ Revision: 1067871
- New version 1.0.5

* Fri May 06 2016 neoclust <neoclust> 1.0.4-1.mga6
+ Revision: 1009832
- imported package erlang-p1_utils

