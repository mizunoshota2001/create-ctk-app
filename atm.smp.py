import __relimport
import threading
import customtkinter
from glorycashchanger import RADRT300, RADRT300Emulator, YenUnits
import config


is_emulated = input('Start in emulation mode? (y/n): ') == 'n'
port = config.PORT
radrt300 = RADRT300(port) \
    if is_emulated else \
    RADRT300Emulator(port)


# 外観モードとテーマの設定
customtkinter.set_appearance_mode("Dark")  # 外観モード: Light, Dark
customtkinter.set_default_color_theme("green")  # テーマ: green

# アプリケーションのメインウィンドウを作成
app = customtkinter.CTk()
app.title("ATM")
app.geometry("500x300")  # ウィンドウサイズ

# フレームの切り替え関数


def switch_frame(frame):
    for child in app.winfo_children():
        child.destroy()
    frame()

# メイン画面のフレームを定義


def main_frame():
    frame = customtkinter.CTkFrame(master=app, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    # タイトルラベル
    title_label = customtkinter.CTkLabel(
        master=frame,
        text="ようこそATMへ",
        font=("Arial", 24, "bold"),
        text_color="white"
    )
    title_label.pack(pady=(30, 10))  # 上部に余白を持たせて配置

    # メッセージラベル
    message_label = customtkinter.CTkLabel(
        master=frame,
        text="操作を始めるには以下のボタンを押してください。",
        font=("Arial", 16),
        text_color="#A0A0A0"
    )
    message_label.pack(pady=10, padx=10)  # 上部に余白を持たせて配置

    # 「入金開始」ボタン
    deposit_button = customtkinter.CTkButton(
        master=frame,
        text="入金開始",
        command=lambda: switch_frame(deposit_frame),
        font=("Arial", 18, "bold"),
        fg_color="#4CAF50",  # ボタンの背景色
        hover_color="#45A049",  # ホバー時の色
        text_color="white",  # テキストの色
        corner_radius=10,  # ボタンの角を丸くする
        width=200,
        height=40
    )
    deposit_button.pack(pady=(20, 30))  # 下部に余白を持たせて配置

# 入金画面のフレームを定義


def deposit_frame():
    threading.Thread(target=radrt300.count_start).start()
    frame = customtkinter.CTkFrame(master=app, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    # タイトルラベル
    title_label = customtkinter.CTkLabel(
        master=frame,
        text="入金画面",
        font=("Arial", 24, "bold"),
        text_color="white"
    )
    title_label.pack(pady=(30, 10))  # 上部に余白を持たせて配置

    # 現在の入金金額（リアルタイムに更新）
    deposit_label = customtkinter.CTkLabel(
        master=frame,
        text="読み込み中…",  # 初期値は空
        font=("Arial", 16),
        text_color="#A0A0A0"
    )
    deposit_label.pack(pady=(10, 20), padx=10)  # 上部に余白を持たせて配置

    def update_current_deposit():
        def _thread():
            deposit_count_data = radrt300.count_data_read()
            total = deposit_count_data.get_total()
            if not deposit_label.winfo_exists():
                return
            deposit_label.configure(text=f"現在の入金金額: {total}")
        threading.Thread(target=_thread).start()
        deposit_label.after(1000, update_current_deposit)
    update_current_deposit()

    # 戻るボタン
    back_button = customtkinter.CTkButton(
        master=frame,
        text="戻る",
        command=lambda: switch_frame(main_frame),
        font=("Arial", 18, "bold"),
        fg_color="#FF7043",  # ボタンの背景色
        hover_color="#FF5722",  # ホバー時の色
        text_color="white",  # テキストの色
        corner_radius=10,  # ボタンの角を丸くする
        width=200,
        height=40
    )
    back_button.pack(pady=(20, 0))  # 下部に余白を持たせて配置

    end_button = customtkinter.CTkButton(
        master=frame,
        text="入金停止",
        command=lambda: switch_frame(deposit_end_frame),
        font=("Arial", 18, "bold"),
        fg_color="#FF7043",  # ボタンの背景色
        hover_color="#FF5722",  # ホバー時の色
        text_color="white",  # テキストの色
        corner_radius=10,  # ボタンの角を丸くする
        width=200,
        height=40
    )
    end_button.pack(pady=(5, 30))  # 下部に余白を持たせて配置


def deposit_end_frame():
    def _end():
        radrt300.count_stop()
        radrt300.count_end()
    threading.Thread(target=_end).start()

    frame = customtkinter.CTkFrame(master=app, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    # タイトルラベル
    title_label = customtkinter.CTkLabel(
        master=frame,
        text="入金完了",
        font=("Arial", 24, "bold"),
        text_color="white"
    )
    title_label.pack(pady=(30, 10))  # 上部に余白を持たせて配置


    total_label = customtkinter.CTkLabel(
        master=frame,
        text=f"計算中…",
        font=("Arial", 16),
        text_color="#A0A0A0"
    )
    total_label.pack(pady=(10, 20), padx=10)  # 上部に余白を持たせ���配置

    def _total():
        deposit_count_data = radrt300.count_data_read()
        total = deposit_count_data.get_total()
        if not total_label.winfo_exists():
            return
        total_label.configure(text=f"合計金額: {total}円")
    threading.Thread(target=_total).start()

    # お礼メッセージラベル
    thank_you_label = customtkinter.CTkLabel(
        master=frame,
        text="ご利用ありがとうございました。",
        font=("Arial", 16),
        text_color="#A0A0A0"
    )
    thank_you_label.pack(pady=(10, 20), padx=10)  # 上部に余白を持たせて配置

    # 数秒後にトップに戻る
    frame.after(5000, lambda: switch_frame(main_frame))


# 初期画面を表示
main_frame()

# メインループ
app.mainloop()
