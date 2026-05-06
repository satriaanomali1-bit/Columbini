import time
import random
import sys
import json

# =========================================================
# 1. SYSTEM UTILITY
# =========================================================

def ketik(teks, speed=0.02):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def garis():
    print("=" * 60)

# =========================================================
# 2. DATABASE MUSUH
# =========================================================

MUSUH_DATABASE = {
    "hutan": [
        {"nama": "Slime Hijau", "hp": 35, "atk": 7, "xp": 20, "gold": 15},
        {"nama": "Goblin Liar", "hp": 60, "atk": 10, "xp": 35, "gold": 25},
        {"nama": "Serigala Hutan", "hp": 80, "atk": 15, "xp": 50, "gold": 40}
    ],

    "gua": [
        {"nama": "Zombie Penambang", "hp": 120, "atk": 20, "xp": 70, "gold": 60},
        {"nama": "Kelelawar Raksasa", "hp": 100, "atk": 25, "xp": 80, "gold": 70},
        {"nama": "Golem Batu", "hp": 180, "atk": 18, "xp": 120, "gold": 100}
    ],

    "kastil": [
        {"nama": "Ksatria Kegelapan", "hp": 250, "atk": 35, "xp": 180, "gold": 150},
        {"nama": "Penyihir Terlarang", "hp": 220, "atk": 45, "xp": 200, "gold": 170}
    ],

    "boss": [
        {"nama": "RAJA NAGA ABYSSAL", "hp": 600, "atk": 60, "xp": 1000, "gold": 1000}
    ]
}

# =========================================================
# 3. ITEMS
# =========================================================

ITEMS = {
    "1": {"nama": "Small Potion", "heal": 40, "harga": 25},
    "2": {"nama": "Mega Potion", "heal": 100, "harga": 60},
}

# =========================================================
# 4. PLAYER CLASS
# =========================================================

class Pemain:
    def __init__(self, nama):
        self.nama = nama
        self.level = 1
        self.exp = 0

        self.hp_max = 120
        self.hp = 120

        self.atk = 15
        self.defense = 5

        self.gold = 100

        self.inventory = {
            "Small Potion": 3
        }

        # ===== SKILL =====
        self.skills = {
            "Fire Slash": {
                "damage": 35,
                "mana": 15
            },

            "Thunder Break": {
                "damage": 60,
                "mana": 30
            }
        }

        self.mana_max = 50
        self.mana = 50

        self.chapter = 1

    # =====================================================

    def status(self):
        garis()
        print(f"NAMA   : {self.nama}")
        print(f"LEVEL  : {self.level}")
        print(f"HP     : {self.hp}/{self.hp_max}")
        print(f"MANA   : {self.mana}/{self.mana_max}")
        print(f"ATK    : {self.atk}")
        print(f"GOLD   : {self.gold}")
        print(f"XP     : {self.exp}/100")
        print(f"CHAPTER: {self.chapter}")
        print(f"ITEM   : {self.inventory}")
        garis()

    # =====================================================

    def level_up(self):

        while self.exp >= 100:

            self.level += 1
            self.exp -= 100

            self.hp_max += 30
            self.hp = self.hp_max

            self.mana_max += 10
            self.mana = self.mana_max

            self.atk += 8
            self.defense += 3

            ketik(f"\n⭐ LEVEL UP! Kamu sekarang level {self.level}!")

            # Unlock skill baru
            if self.level == 3:
                self.skills["Shadow Strike"] = {
                    "damage": 90,
                    "mana": 40
                }

                ketik("🔥 Skill baru terbuka: Shadow Strike!")

            if self.level == 5:
                self.skills["Dragon Fury"] = {
                    "damage": 150,
                    "mana": 60
                }

                ketik("🐉 Skill LEGENDARY terbuka: Dragon Fury!")

    # =====================================================

    def save_game(self):

        data = self.__dict__

        with open("savegame.json", "w") as f:
            json.dump(data, f)

        ketik("💾 Game berhasil disimpan!")

# =========================================================
# 5. STORY SYSTEM
# =========================================================

def intro_story():

    garis()

    ketik("🌑 Tahun 1450...")
    ketik("Kerajaan Aetheria diselimuti kegelapan.")
    ketik("Monster mulai muncul dari celah misterius.")
    ketik("Raja menghilang tanpa jejak.")
    ketik("Dan hanya satu orang yang bisa menghentikannya...")

    garis()

def chapter_story(player):

    if player.chapter == 1:

        ketik("\n📖 CHAPTER 1 - AWAL PETUALANGAN")
        ketik("Kepala desa meminta bantuanmu untuk membersihkan hutan.")
        ketik("Monster di hutan mulai menyerang warga.")

    elif player.chapter == 2:

        ketik("\n📖 CHAPTER 2 - GUA KEGELAPAN")
        ketik("Kamu menemukan simbol aneh di gua.")
        ketik("Ternyata seseorang membangkitkan pasukan undead.")

    elif player.chapter == 3:

        ketik("\n📖 CHAPTER 3 - KASTIL TERKUTUK")
        ketik("Di kastil tua, kamu melihat naga hitam tertidur.")
        ketik("Aura jahat memenuhi seluruh ruangan...")

    elif player.chapter == 4:

        ketik("\n📖 FINAL CHAPTER")
        ketik("RAJA NAGA ABYSSAL telah bangkit.")
        ketik("Nasib dunia berada di tanganmu.")

# =========================================================
# 6. SISTEM BATTLE
# =========================================================

def battle(player, musuh):

    enemy_hp = musuh["hp"]

    ketik(f"\n⚔️ {musuh['nama']} muncul!")

    while enemy_hp > 0 and player.hp > 0:

        garis()

        print(f"{musuh['nama']} HP : {enemy_hp}")
        print(f"{player.nama} HP : {player.hp}")
        print(f"MANA : {player.mana}")

        garis()

        print("1. Attack")
        print("2. Skill")
        print("3. Gunakan Potion")
        print("4. Bertahan")

        pilih = input(">> ")

        # =================================================

        if pilih == "1":

            damage = random.randint(player.atk - 5, player.atk + 10)

            enemy_hp -= damage

            ketik(f"⚔️ Kamu menyerang {musuh['nama']}!")
            ketik(f"Damage: {damage}")

        # =================================================

        elif pilih == "2":

            print("\n=== SKILL ===")

            daftar_skill = list(player.skills.keys())

            for i, s in enumerate(daftar_skill):
                print(f"{i+1}. {s}")

            pilih_skill = input("Gunakan skill nomor: ")

            if pilih_skill.isdigit():

                idx = int(pilih_skill) - 1

                if idx < len(daftar_skill):

                    nama_skill = daftar_skill[idx]

                    skill = player.skills[nama_skill]

                    if player.mana >= skill["mana"]:

                        player.mana -= skill["mana"]

                        damage = random.randint(
                            skill["damage"] - 10,
                            skill["damage"] + 15
                        )

                        enemy_hp -= damage

                        ketik(f"🔥 Kamu menggunakan {nama_skill}!")
                        ketik(f"💥 Damage besar: {damage}")

                    else:
                        ketik("❌ Mana tidak cukup!")

        # =================================================

        elif pilih == "3":

            if "Small Potion" in player.inventory and player.inventory["Small Potion"] > 0:

                heal = 40

                player.hp = min(player.hp + heal, player.hp_max)

                player.inventory["Small Potion"] -= 1

                ketik(f"🧪 HP pulih {heal}!")

            else:
                ketik("❌ Potion habis!")

        # =================================================

        elif pilih == "4":

            ketik("🛡️ Kamu bertahan.")
            reduce = True

        # =================================================
        # MUSUH MENYERANG
        # =================================================

        if enemy_hp > 0:

            enemy_damage = random.randint(
                musuh["atk"] - 5,
                musuh["atk"] + 5
            )

            player.hp -= enemy_damage

            ketik(f"👹 {musuh['nama']} menyerang!")
            ketik(f"💢 Kamu terkena {enemy_damage} damage!")

    # =====================================================
    # MENANG
    # =====================================================

    if player.hp > 0:

        ketik(f"\n🏆 Kamu mengalahkan {musuh['nama']}!")

        player.exp += musuh["xp"]
        player.gold += musuh["gold"]

        ketik(f"+{musuh['xp']} XP")
        ketik(f"+{musuh['gold']} GOLD")

        player.level_up()

        return True

    else:

        ketik("\n💀 Kamu kalah...")
        player.hp = 50
        return False

# =========================================================
# 7. SHOP
# =========================================================

def shop(player):

    garis()

    ketik("🏪 TOKO DESA")

    for k, v in ITEMS.items():
        print(f"{k}. {v['nama']} - {v['harga']} Gold")

    beli = input("Beli nomor (n untuk keluar): ")

    if beli in ITEMS:

        item = ITEMS[beli]

        if player.gold >= item["harga"]:

            player.gold -= item["harga"]

            player.inventory[item["nama"]] = player.inventory.get(item["nama"], 0) + 1

            ketik(f"✅ Membeli {item['nama']}")

        else:
            ketik("❌ Gold tidak cukup!")

# =========================================================
# 8. MAIN GAME
# =========================================================

def main():

    intro_story()

    nama = input("Masukkan nama hero: ")

    player = Pemain(nama)

    ketik(f"\nSelamat datang, {nama}...")

    while True:

        player.status()

        print("\n=== MENU ===")
        print("1. Eksplorasi Hutan")
        print("2. Masuk Gua")
        print("3. Kastil Terkutuk")
        print("4. Boss Final")
        print("5. Toko")
        print("6. Istirahat")
        print("7. Save")
        print("8. Keluar")

        pilih = input(">> ")

        # =================================================

        if pilih == "1":

            chapter_story(player)

            musuh = random.choice(MUSUH_DATABASE["hutan"])

            menang = battle(player, musuh)

            if menang:
                player.chapter = max(player.chapter, 2)

        # =================================================

        elif pilih == "2":

            if player.level < 3:

                ketik("⚠️ Kamu harus minimal level 3!")

            else:

                chapter_story(player)

                musuh = random.choice(MUSUH_DATABASE["gua"])

                menang = battle(player, musuh)

                if menang:
                    player.chapter = max(player.chapter, 3)

        # =================================================

        elif pilih == "3":

            if player.level < 5:

                ketik("⚠️ Kamu harus minimal level 5!")

            else:

                chapter_story(player)

                musuh = random.choice(MUSUH_DATABASE["kastil"])

                menang = battle(player, musuh)

                if menang:
                    player.chapter = max(player.chapter, 4)

        # =================================================

        elif pilih == "4":

            if player.level < 7:

                ketik("⚠️ Kamu terlalu lemah untuk melawan boss akhir!")

            else:

                chapter_story(player)

                boss = MUSUH_DATABASE["boss"][0]

                menang = battle(player, boss)

                if menang:

                    garis()

                    ketik("🎉 SELAMAT!")
                    ketik("Kamu berhasil mengalahkan Raja Naga Abyssal!")
                    ketik("Kerajaan kembali damai.")
                    ketik("Namamu menjadi legenda sepanjang masa.")

                    garis()

                    break

        # =================================================

        elif pilih == "5":

            shop(player)

        # =================================================

        elif pilih == "6":

            if player.gold >= 20:

                player.gold -= 20
                player.hp = player.hp_max
                player.mana = player.mana_max

                ketik("💤 Kamu beristirahat...")

            else:
                ketik("❌ Gold tidak cukup!")

        # =================================================

        elif pilih == "7":

            player.save_game()

        # =================================================

        elif pilih == "8":

            ketik("Terima kasih sudah bermain!")
            break

# =========================================================
# START GAME
# =========================================================

if __name__ == "__main__":
    main()