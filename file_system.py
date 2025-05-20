import datetime
import json
import os

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
    
    def truncate(self, filename):
        if filename not in self.index:
            return "File not found."

        content = self.index[filename]['content']
        needed = len(content) // 10 + 1
        start = self.index[filename]['start_block']

        if start is not None:
            for i in range(start, start + needed):
                if i < len(self.disk):
                    self.disk[i] = None

    # Reset metadata kecuali nama & waktu dibuat
        self.index[filename]['start_block'] = None
        self.index[filename]['size'] = 0
        self.index[filename]['content'] = ''
        self.index[filename]['timestamp'] = datetime.datetime.now().isoformat()
        return f"File '{filename}' truncated."
    

    def show_disk(self):
        print("\nDisk Status (X = used, . = free):")
        for i in range(0, len(self.disk), 10):
            line = self.disk[i:i+10]
            print(''.join(['X' if blk else '.' for blk in line]))

    def show_metadata(self, filename):
        if filename not in self.index:
            return "File not found."

        info = self.index[filename]  # ← inisialisasi variabel info

        return (
            f"\nMetadata for '{filename}':\n"
            f"  Start Block : {info.get('start_block')}\n"
            f"  Size        : {info.get('size')} block(s)\n"
            f"  Timestamp   : {info.get('timestamp')}\n"
            f"  Content     : '{info.get('content')}'"
        )

    def save_to_file(self, path='data/fs_dump.json'):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump({
                'index': self.index,
                'disk': self.disk
            }, f)
        return "File system saved."

    def load_from_file(self, path='data/fs_dump.json'):
        if not os.path.exists(path):
            return "No saved file system found."
        with open(path, 'r') as f:
            data = json.load(f)
            self.index = data['index']
            self.disk = data['disk']
        return "File system loaded."