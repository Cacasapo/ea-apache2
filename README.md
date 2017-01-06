# ea-apache2-http2
CentOS 7, EA4 and HTTP/2. SEE LINK FOR INFO.

Default symlink protection provided by Cpanel (needs additional steps, see https://documentation.cpanel.net/display/EA4/Symlink+Race+Condition+Protection) . 
Rack911 protection still can be enabled by editing ea-apache2.

Cpanel has updated Apache to .25 and this has caused an issue with http2. I'm looking into it, but it seems related to this:
https://bz.apache.org/bugzilla/show_bug.cgi?id=60510
