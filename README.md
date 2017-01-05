# ea-apache2-http2
CentOS 7, EA4 and HTTP/2. SEE LINK FOR INFO.

Default symlink protection provided by Cpanel (needs additional steps, see https://documentation.cpanel.net/display/EA4/Symlink+Race+Condition+Protection) . 
Rack911 protection still can be enabled by editing ea-apache2.

Cpanel has updated Apache to .25 and this has caused an issue with graceful restarts with this setup. I'm working on this on my spare time and will update this project to 2.4.25 as soon as I find a solution.
