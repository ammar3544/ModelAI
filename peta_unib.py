import heapq
import math

class DijkstraUNIB:
    def __init__(self):
        # Definisi node berdasarkan lokasi di peta UNIB
        self.nodes = {
            'SD_NEGERI_86': 'SD Negeri 86 Kota Bengkulu',
            'PEMAKAMAN_UMUM': 'Pemakaman Umum Kel. Beringin Raya',
            'LAB_AGRONOMI': 'Laboratorium Agronomi Fakultas Pertanian',
            'GEDUNG_LAYANAN_TERPADU': 'Gedung Unit Layanan Terpadu',
            'GEDUNG_C': 'Gedung C Universitas Bengkulu',
            'GEDUNG_I': 'Gedung I Universitas Bengkulu',
            'DEKANAT_HUKUM': 'Dekanat Fakultas Hukum Universitas Bengkulu',
            'GEDUNG_K': 'Gedung K UNIB',
            'REKTORAT': 'Rektorat UNIB',
            'LPTIK': 'LPTIK University of Bengkulu',
            'GEDUNG_SERBA_GUNA': 'Gedung Serba Guna Universitas Bengkulu',
            'PERPUSTAKAAN': 'Perpustakaan UNIB',
            'DEKANAT_FMIPA': 'Dekanat FMIPA UNIB',
            'GB3_DAN4': 'GB 3 dan 4 UNIB',
            'FAKULTAS_KEDOKTERAN': 'Faculty of Medicine and Health Sciences',
            'SEKRETARIAT_PMII': 'Sekretariat PMII FKIP UNIB',
            'MASJID_AL_IKHLAS': 'Masjid Al-Ikhlas',
            'STADION': 'Stadion UNIB'
        }
        
        # Graf dengan bobot (estimasi jarak dalam meter berdasarkan peta)
        self.graph = {
            'SD_NEGERI_86': {
                'PEMAKAMAN_UMUM': 300,
                'LAB_AGRONOMI': 400
            },
            'PEMAKAMAN_UMUM': {
                'SD_NEGERI_86': 300,
                'LAB_AGRONOMI': 200,
                'PERPUSTAKAAN': 250
            },
            'LAB_AGRONOMI': {
                'SD_NEGERI_86': 400,
                'PEMAKAMAN_UMUM': 200,
                'GEDUNG_LAYANAN_TERPADU': 150,
                'PERPUSTAKAAN': 300
            },
            'GEDUNG_LAYANAN_TERPADU': {
                'LAB_AGRONOMI': 150,
                'GEDUNG_C': 200,
                'REKTORAT': 180
            },
            'GEDUNG_C': {
                'GEDUNG_LAYANAN_TERPADU': 200,
                'GEDUNG_I': 150,
                'DEKANAT_HUKUM': 180,
                'REKTORAT': 220
            },
            'GEDUNG_I': {
                'GEDUNG_C': 150,
                'DEKANAT_HUKUM': 120,
                'GEDUNG_K': 200
            },
            'DEKANAT_HUKUM': {
                'GEDUNG_C': 180,
                'GEDUNG_I': 120,
                'GEDUNG_K': 250,
                'REKTORAT': 300
            },
            'GEDUNG_K': {
                'GEDUNG_I': 200,
                'DEKANAT_HUKUM': 250
            },
            'REKTORAT': {
                'GEDUNG_LAYANAN_TERPADU': 180,
                'GEDUNG_C': 220,
                'DEKANAT_HUKUM': 300,
                'LPTIK': 150,
                'PERPUSTAKAAN': 200
            },
            'LPTIK': {
                'REKTORAT': 150,
                'GEDUNG_SERBA_GUNA': 120,
                'PERPUSTAKAAN': 180
            },
            'GEDUNG_SERBA_GUNA': {
                'LPTIK': 120,
                'PERPUSTAKAAN': 100,
                'DEKANAT_FMIPA': 200,
                'GB3_DAN4': 180
            },
            'PERPUSTAKAAN': {
                'PEMAKAMAN_UMUM': 250,
                'LAB_AGRONOMI': 300,
                'REKTORAT': 200,
                'LPTIK': 180,
                'GEDUNG_SERBA_GUNA': 100,
                'DEKANAT_FMIPA': 150
            },
            'DEKANAT_FMIPA': {
                'GEDUNG_SERBA_GUNA': 200,
                'PERPUSTAKAAN': 150,
                'GB3_DAN4': 100,
                'FAKULTAS_KEDOKTERAN': 250
            },
            'GB3_DAN4': {
                'GEDUNG_SERBA_GUNA': 180,
                'DEKANAT_FMIPA': 100,
                'FAKULTAS_KEDOKTERAN': 200,
                'SEKRETARIAT_PMII': 150,
                'MASJID_AL_IKHLAS': 300
            },
            'FAKULTAS_KEDOKTERAN': {
                'DEKANAT_FMIPA': 250,
                'GB3_DAN4': 200,
                'SEKRETARIAT_PMII': 180
            },
            'SEKRETARIAT_PMII': {
                'GB3_DAN4': 150,
                'FAKULTAS_KEDOKTERAN': 180,
                'MASJID_AL_IKHLAS': 200,
                'STADION': 250
            },
            'MASJID_AL_IKHLAS': {
                'GB3_DAN4': 300,
                'SEKRETARIAT_PMII': 200,
                'STADION': 150
            },
            'STADION': {
                'SEKRETARIAT_PMII': 250,
                'MASJID_AL_IKHLAS': 150
            }
        }
    
    def dijkstra(self, start, end):
        """
        Implementasi algoritma Dijkstra untuk mencari jalur terpendek
        """
        # Inisialisasi jarak dan predecessor
        distances = {node: float('infinity') for node in self.graph}
        distances[start] = 0
        predecessors = {}
        
        # Priority queue (min-heap)
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            # Skip jika sudah dikunjungi
            if current_node in visited:
                continue
                
            visited.add(current_node)
            
            # Jika mencapai tujuan
            if current_node == end:
                break
            
            # Periksa tetangga
            for neighbor, weight in self.graph.get(current_node, {}).items():
                distance = current_distance + weight
                
                # Jika ditemukan jalur yang lebih pendek
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
        
        # Rekonstruksi jalur
        if end not in predecessors and start != end:
            return None, float('infinity')
        
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = predecessors.get(current)
        path.reverse()
        
        return path, distances[end]
    
    def get_all_shortest_paths(self, start):
        """
        Mendapatkan jalur terpendek dari satu titik ke semua titik lainnya
        """
        distances = {node: float('infinity') for node in self.graph}
        distances[start] = 0
        predecessors = {}
        
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            if current_node in visited:
                continue
                
            visited.add(current_node)
            
            for neighbor, weight in self.graph.get(current_node, {}).items():
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances, predecessors
    
    def print_path_info(self, path, distance, start, end):
        """
        Menampilkan informasi jalur
        """
        print(f"\n=== JALUR TERPENDEK ===")
        print(f"Dari: {self.nodes[start]}")
        print(f"Ke: {self.nodes[end]}")
        print(f"Jarak Total: {distance} meter")
        print(f"\nRute:")
        
        for i, node in enumerate(path):
            if i < len(path) - 1:
                next_node = path[i + 1]
                segment_distance = self.graph[node][next_node]
                print(f"{i+1}. {self.nodes[node]} -> {self.nodes[next_node]} ({segment_distance}m)")
            else:
                print(f"{i+1}. {self.nodes[node]} (Tujuan)")
    
    def print_all_nodes(self):
        """
        Menampilkan semua node yang tersedia
        """
        print("=== LOKASI YANG TERSEDIA ===")
        for i, (key, value) in enumerate(self.nodes.items(), 1):
            print(f"{i:2d}. {key:<20} - {value}")

# Contoh penggunaan
def main():
    dijkstra_unib = DijkstraUNIB()
    
    print("ALGORITMA DIJKSTRA - UNIVERSITAS BENGKULU")
    print("=" * 50)
    
    # Menampilkan semua lokasi
    dijkstra_unib.print_all_nodes()
    
    # Contoh pencarian jalur terpendek
    print("\n" + "=" * 50)
    print("CONTOH PENCARIAN JALUR TERPENDEK")
    
    # Dari Rektorat ke Fakultas Kedokteran
    start = 'REKTORAT'
    end = 'FAKULTAS_KEDOKTERAN'
    
    path, distance = dijkstra_unib.dijkstra(start, end)
    
    if path:
        dijkstra_unib.print_path_info(path, distance, start, end)
    else:
        print(f"Tidak ada jalur dari {start} ke {end}")
    
    # Contoh lain: Dari Perpustakaan ke Stadion
    print("\n" + "=" * 50)
    start2 = 'PERPUSTAKAAN'
    end2 = 'STADION'
    
    path2, distance2 = dijkstra_unib.dijkstra(start2, end2)
    
    if path2:
        dijkstra_unib.print_path_info(path2, distance2, start2, end2)
    else:
        print(f"Tidak ada jalur dari {start2} ke {end2}")
    
    # Menampilkan jarak dari satu titik ke semua titik
    print("\n" + "=" * 50)
    print("JARAK DARI REKTORAT KE SEMUA LOKASI")
    distances, _ = dijkstra_unib.get_all_shortest_paths('REKTORAT')
    
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    for node, dist in sorted_distances:
        if dist != float('infinity'):
            print(f"{dijkstra_unib.nodes[node]:<40}: {dist:>6} meter")

if __name__ == "__main__":
    main()