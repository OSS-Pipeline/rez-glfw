name = "glfw"

version = "3.3.0"

authors = [
    "GLFW Development Team"
]

description = \
    """
    GLFW is an Open Source, multi-platform library for OpenGL, OpenGL ES and Vulkan application development.
    It provides a simple, platform-independent API for creating windows, contexts and surfaces, reading input,
    handling events, etc.
    """

requires = [
    "gcc-6+",
    "cmake-3+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "glfw-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib64")

    # Helper environment variables.
    env.GLFW_INCLUDE_PATH.set("{root}/include")
    env.GLFW_LIBRARY_PATH.set("{root}/lib64")
