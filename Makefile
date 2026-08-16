AS = xtensa-esp-elf-as
LD = xtensa-esp-elf-ld
OBJCOPY = xtensa-esp-elf-objcopy

SRCS = $(wildcard patches/*.s)
OBJS = $(SRCS:patches/%.s=build/%.o)

all: patches.hex

build/%.o: patches/%.s
	mkdir -p build
	$(AS) --no-transform --longcalls -o $@ $<

build/patches.elf: $(OBJS) patches/link.ld
	$(LD) -o $@ -T patches/link.ld $(OBJS)

patches.hex: build/patches.elf
	$(OBJCOPY) -O ihex $< $@

clean:
	rm -rf build patches.hex

.PHONY: all clean
