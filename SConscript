env = Environment(
    CPPPATH = ['../sdk/KPHP', '../sdk/common'],
    CXXFLAGS = ['-std=gnu++17', '-fcommon'],
)
env.Program('main', Glob('kphp/*.cpp', exclude = 'kphp/xmain.cpp'), LIBS = ['kphp-engine', 're2', 'pcre', 'z', 'crypto'], LIBPATH = '../sdk')
