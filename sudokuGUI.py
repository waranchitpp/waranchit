import customtkinter as ctk
from tkinter import messagebox
#Sudoku คือเกมแก้ปัญหาโดย กติกาคือให้เติมตัวเลข 1-9 ในช่องว่าง ขนาด 9x9 หรือ 81 ช่อง
"""
เงื่อนไขการเล่นคือ 
1.rowจะต้องมีตัวเลข 1-9 ไม่ซำ้กัน
2.columnจะต้องเติม 1-9 ไม่ให้ซำ้กัน
3.กลุ่มย่อยหรือ square จะต้องเติม 1-9 ไม่ให้ซำ้กัน

"""
# ตั้งค่า appearance mode และธีมสี
ctk.set_appearance_mode("dark")  # ตั้งค่าเป็นธีม Dark
ctk.set_default_color_theme("dark-blue")  # ใช้ธีมสีที่เป็น dark blue

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]
        self.build_grid()

    def build_grid(self):
        """สร้างตาราง Sudoku GUI"""
        for row in range(9):
            for col in range(9):
                cell = ctk.CTkEntry(self.root, width=50, font=("Arial", 16), justify="center")
                cell.grid(row=row, column=col, padx=5, pady=5)
                self.cells[row][col] = cell

        # ปุ่ม Solve
        solve_button = ctk.CTkButton(self.root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=0, columnspan=4, pady=10)

        # ปุ่ม Reset
        reset_button = ctk.CTkButton(self.root, text="Reset", command=self.reset_board)
        reset_button.grid(row=9, column=5, columnspan=4, pady=10)

    def get_board(self):
        """ดึงค่าจาก GUI และสร้างตาราง Sudoku"""
        board = []
        for row in range(9):
            row_data = []
            for col in range(9):
                val = self.cells[row][col].get()
                row_data.append(int(val) if val.isdigit() else 0)
            board.append(row_data)
        return board

    def set_board(self, board):
        """แสดงค่าตาราง Sudoku ที่แก้ไขแล้วใน GUI"""
        for row in range(9):
            for col in range(9):
                if board[row][col] != 0:
                    self.cells[row][col].delete(0, "end")
                    self.cells[row][col].insert(0, str(board[row][col]))

    def is_valid(self, board, row, col, num):
        """ตรวจสอบว่าหมายเลขนี้สามารถใส่ในตำแหน่งนี้ได้หรือไม่"""
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve(self, board):
        """แบ็คแทร็กเพื่อแก้ปัญหา Sudoku"""
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def solve_sudoku(self):
        """เรียกฟังก์ชันแก้ปัญหาและแสดงผลใน GUI"""
        board = self.get_board()
        if self.solve(board):
            self.set_board(board)
            messagebox.showinfo("Success", "แก้โจทย์เรียบร้อยแล้ว")
        else:
            messagebox.showerror("Error", "ไม่สามารถแก้โจทย์ได้")

    def reset_board(self):
        """เคลียร์ค่าทั้งหมดในกริด"""
        for row in range(9):
            for col in range(9):
                self.cells[row][col].delete(0, "end")

if __name__ == "__main__":
    root = ctk.CTk()
    gui = SudokuSolverGUI(root)
    root.mainloop()
