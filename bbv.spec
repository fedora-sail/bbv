Name:           bbv
Version:        1.4
Release:        %autorelease
Summary:        Bedrock Bit Vector Library

License:        MIT
URL:            https://github.com/mit-plv/%{name}
Source0:        https://github.com/mit-plv/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  coq
BuildRequires:  ocaml-rpm-macros

%global debug_package %{nil}

%description
Several Coq projects at MIT use a file called Word.v, defining bit vectors and lemmas about them.

	
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n bbv-%{version}

%build
%make_build

%install
%make_install
%ocaml_files

%files -f .ofiles
%license LICENSE
%doc README.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
