env = Environment(
    CPPPATH = ['../sdk/KPHP', '../sdk/common'],
    CXXFLAGS = ['-std=gnu++17', '-fcommon'],
)
env.Append(LIBS = ['kphp-engine'], LIBPATH = '../sdk')
env.ParseConfig('pkg-config re2 --cflags --libs')
env.ParseConfig('pkg-config libpcre --cflags --libs')
env.ParseConfig('pkg-config zlib --cflags --libs')
env.ParseConfig('pkg-config libcrypto --cflags --libs')
env.Program('main', Glob('kphp/*.cpp', exclude = 'kphp/xmain.cpp'))
