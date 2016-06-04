EasyApache 4 & BlueHost Symlink Protection Patch
=============

This fork of ea-apache2 includes the BlueHost Symlink Protection Patch for EasyApache 4 from cPanel.

Installation
-----------
0. Go to the following link and click on your architecture: http://download.opensuse.org/repositories/home:/Jperkster:/symlink_patch/
0. Download the .repo file:
```
wget -O /etc/yum.repos.d/EA4-Symlink-Protection.repo $Link_to_repo_file 
yum update
```

Downgrading
-----------
If you ever need to downgrade away from these packages, the following should work:
```
yum downgrade ea-apache24 ea-apache24-tools ea-apache24-mod_headers ea-apache24-mod_proxy ea-apache24-mod_suexec ea-apache24-mod_proxy_http ea-apache24-mod_unique_id ea-apache24-mod_mpm_worker ea-apache24-mod_ssl ea-apache24-mod_proxy_fcgi ea-apache24-mod_cgid ea-apache24-mod_deflate ea-apache24-mod_expires ea-apr
```
