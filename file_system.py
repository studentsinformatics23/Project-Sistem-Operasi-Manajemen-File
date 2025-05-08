import datetime

class MiniFileSystem:
    def __init__(self, total_blocks=100):
        self.disk = [None] * total_blocks
        self.index = {}

    def create(self, filename):
        if filename in self.index:
            return "File already exists."
        self.index[filename] = {
            'start_block': None,
            'size': 0,
            'timestamp': datetime.datetime.now().isoformat(),
            'content': ''
        }
        return f"File '{filename}' created."

    def write(self, filename, data):
        if filename not in self.index:
            return "File not found."

        # Cari blok kosong
        needed = len(data) // 10 + 1
        free_blocks = [i for i, blk in enumerate(self.disk) if blk is None]
        if len(free_blocks) < needed:
            return "Not enough space on disk."

        # Simpan data
        for i in range(needed):
            chunk = data[i*10:(i+1)*10]
            self.disk[free_blocks[i]] = chunk

        self.index[filename]['start_block'] = free_blocks[0]
        self.index[filename]['size'] = needed
        self.index[filename]['content'] = data
        self.index[filename]['timestamp'] = datetime.datetime.now().isoformat()
        return f"Data written to '{filename}'."

    def read(self, filename):
        if filename not in self.index:
            return "File not found."
        return self.index[filename]['content']

    def delete(self, filename):
        if filename not in self.index:
            return "File not found."

        # Hapus isi dari disk
        content = self.index[filename]['content']
        needed = len(content) // 10 + 1
        start = self.index[filename]['start_block']
        if start is not None:
            for i in range(start, start + needed):
                if i < len(self.disk):
                    self.disk[i] = None

        del self.index[filename]
        return f"File '{filename}' deleted."

    def list_files(self):
        return list(self.index.keys())
