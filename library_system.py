class ReservationNode:
    
    def __init__(self, member_name):
        self.member_name = member_name
        self.next = None


class ReservationList:
   
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, member_name):
        new_node = ReservationNode(member_name)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def pop_left(self):
        if self.head is None:
            return None
        next_member = self.head.member_name
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return next_member

    def is_empty(self):
        return self.head is None

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count


class BookNode:
    
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.available = True
        self.reservations = ReservationList()
        self.left = None
        self.right = None


class BookBST:
    
    def __init__(self):
        self.root = None

    def insert(self, isbn, title, author):
        if self.root is None:
            self.root = BookNode(isbn, title, author)
            return True
        return self._insert(self.root, isbn, title, author)

    def _insert(self, current, isbn, title, author):
        if isbn == current.isbn:
            return False
        if isbn < current.isbn:
            if current.left is None:
                current.left = BookNode(isbn, title, author)
                return True
            return self._insert(current.left, isbn, title, author)
        else:
            if current.right is None:
                current.right = BookNode(isbn, title, author)
                return True
            return self._insert(current.right, isbn, title, author)

    def find(self, isbn):
        return self._find(self.root, isbn)

    def _find(self, current, isbn):
        if current is None:
            return None
        if isbn == current.isbn:
            return current
        if isbn < current.isbn:
            return self._find(current.left, isbn)
        return self._find(current.right, isbn)

    def inorder(self):
        ordered = []
        self._inorder(self.root, ordered)
        return ordered

    def _inorder(self, current, ordered):
        if current is None:
            return
        self._inorder(current.left, ordered)
        ordered.append(current)
        self._inorder(current.right, ordered)


library_tree = BookBST()
member_set = set()


def add_book():
    isbn = input("ISBN girin: ")
    title = input("Kitap adı girin: ")
    author = input("Yazar adı girin: ")
    inserted = library_tree.insert(isbn, title, author)
    if inserted:
        print("Kitap başarıyla eklendi.")
    else:
        print("Bu ISBN zaten kayıtlı, ekleme yapılmadı.")


def register_member():
    member_name = input("Üye adı girin: ")
    if member_name in member_set:
        print("Bu üye zaten kayıtlı.")
        return
    member_set.add(member_name)
    print("Üye başarıyla kaydedildi.")


def lend_book():
    isbn = input("Ödünç verilecek kitabın ISBN'i: ")
    member_name = input("Kitabı alacak üyenin adı: ")
    if member_name not in member_set:
        print("Üye bulunamadı, lütfen önce kayıt olun.")
        return
    node = library_tree.find(isbn)
    if node is None:
        print("Bu ISBN kayıtlı değil.")
        return
    if node.available:
        node.available = False
        print(f"{node.title} kitabı {member_name} adına ödünç verildi.")
    else:
        decision = input("Kitap meşgul. Rezervasyon kuyruğuna eklenmek ister misiniz? (E/H): ")
        if decision.upper() == "E":
            node.reservations.append(member_name)
            print("Üye rezervasyon listesine eklendi.")
        else:
            print("Rezervasyon yapılmadı.")


def return_book():
    isbn = input("İade edilecek kitabın ISBN'i: ")
    node = library_tree.find(isbn)
    if node is None:
        print("Bu ISBN kayıtlı değil.")
        return
    if node.available:
        print("Bu kitap zaten kütüphanede görünüyor.")
        return
    if node.reservations.is_empty():
        node.available = True
        print("Kitap iade edildi ve tekrar müsait durumda.")
    else:
        next_member = node.reservations.pop_left()
        node.available = False
        print(f"Kitap sıradaki üye {next_member} adına hazırlandı ve ödünç verildi.")


def list_books():
    ordered_books = library_tree.inorder()
    if not ordered_books:
        print("Henüz kitap eklenmedi.")
        return
    print("\n--- Kayıtlı Kitaplar ---")
    for node in ordered_books:
        status = "Müsait" if node.available else "Ödünçte"
        reservation_count = len(node.reservations)
        print(f"ISBN: {node.isbn} | Ad: {node.title} | Yazar: {node.author} | Durum: {status} | Rezervasyon: {reservation_count}")


def list_members():
    if not member_set:
        print("Henüz üye eklenmedi.")
        return
    print("\n--- Kayıtlı Üyeler ---")
    for member in sorted(member_set):
        print(f"Üye: {member}")


def show_menu():
    print("\n==============================")
    print("||   Kütüphane Yönetimi    ||")
    print("==============================")
    print("1. Kitap ekle")
    print("2. Üye ekle")
    print("3. Kitap ödünç ver")
    print("4. Kitap iade al")
    print("5. Kitapları listele")
    print("6. Üyeleri listele")
    print("7. Çıkış")
    print("==============================")


def main():
    while True:
        show_menu()
        choice = input("Seçiminizi yapın (1-7): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            register_member()
        elif choice == "3":
            lend_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            list_books()
        elif choice == "6":
            list_members()
        elif choice == "7":
            print("Programdan çıkılıyor. Hoşça kalın!")
            break
        else:
            print("Geçersiz seçim, lütfen 1-7 arasında bir değer girin.")


if __name__ == "__main__":
    main()
