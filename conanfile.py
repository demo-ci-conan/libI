from conans import ConanFile

class libI(ConanFile):
    name = "libI"
    version = "0.0"

    # No settings/options are necessary, this is header only
    no_copy_source = True

    scm = {"type": "git",
           "url": "auto",
           "revision": "auto"}

    exports_sources = ["LICENSE", # to avoid build info bug
                       "include/libI/libI_headerOnly.h"]

    def requirements(self):
        self.requires("libJ/0.0@demo/testing")

    def package(self):
        self.copy("LICENSE", dst="licenses")
        self.copy("include/libI/libI_headerOnly.h")

    def package_id(self):
        self.info.header_only()
