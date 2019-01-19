import dualnback.core as core
print(core.visual_generator())
l=[core.audio_generator() for i in range(20000)]
for i in range(1,7):
    print(l.count(i))

