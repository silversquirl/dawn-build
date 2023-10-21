solutions = [
  { "name"        : ".",
    "url"         : "https://dawn.googlesource.com/dawn",
    "deps_file"   : "DEPS",
    "managed"     : False,

    "custom_hooks": [
        # Disable x86 sysroot; we only need x64
        {"name": "sysroot_x86", "action": ["true"]},
    ],
  },
]
