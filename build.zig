const std = @import("std");
const dawn = @import("mach_gpu_dawn");

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    // Dummy lib because mach-gpu-dawn insists on having something to link to
    const lib = b.addSharedLibrary(.{
        .name = "dummy",
        .target = target,
        .optimize = optimize,
    });

    dawn.link(b, lib, .{
        .shared_libs = true,
        .from_source = true,
        .install_libs = true,
    });
}
