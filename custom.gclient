solutions = [
  { "name"        : ".",
    "url"         : "https://dawn.googlesource.com/dawn",
    "deps_file"   : "DEPS",
    "managed"     : False,

    # Disable sysroot
    "custom_hooks": [
        {"name": "sysroot_x86", "action": ["true"]},
        {"name": "sysroot_x64", "action": ["true"]},
    ],
  },
]
