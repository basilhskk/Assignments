namespace bookstore
{
    partial class Printer
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.colorbox = new System.Windows.Forms.ComboBox();
            this.sizebox = new System.Windows.Forms.ComboBox();
            this.label2 = new System.Windows.Forms.Label();
            this.printbutton = new System.Windows.Forms.Button();
            this.exitbutton = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.copiesbox = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.copiesbox)).BeginInit();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(34, 34);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(75, 20);
            this.label1.TabIndex = 4;
            this.label1.Text = "COLOR:";
            // 
            // colorbox
            // 
            this.colorbox.BackColor = System.Drawing.Color.LightGray;
            this.colorbox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.colorbox.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.colorbox.FormattingEnabled = true;
            this.colorbox.Items.AddRange(new object[] {
            "BLACK AND WHITE",
            "COLORED"});
            this.colorbox.Location = new System.Drawing.Point(129, 32);
            this.colorbox.Name = "colorbox";
            this.colorbox.Size = new System.Drawing.Size(173, 26);
            this.colorbox.TabIndex = 5;
            // 
            // sizebox
            // 
            this.sizebox.BackColor = System.Drawing.Color.LightGray;
            this.sizebox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.sizebox.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.sizebox.FormattingEnabled = true;
            this.sizebox.Items.AddRange(new object[] {
            "A2",
            "A3",
            "A4",
            "A5",
            "A6"});
            this.sizebox.Location = new System.Drawing.Point(129, 85);
            this.sizebox.Name = "sizebox";
            this.sizebox.Size = new System.Drawing.Size(86, 26);
            this.sizebox.TabIndex = 6;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(34, 87);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(55, 20);
            this.label2.TabIndex = 7;
            this.label2.Text = "SIZE:";
            // 
            // printbutton
            // 
            this.printbutton.BackColor = System.Drawing.Color.OliveDrab;
            this.printbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.printbutton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.printbutton.Location = new System.Drawing.Point(195, 209);
            this.printbutton.Name = "printbutton";
            this.printbutton.Size = new System.Drawing.Size(107, 40);
            this.printbutton.TabIndex = 8;
            this.printbutton.Text = "Print";
            this.printbutton.UseVisualStyleBackColor = false;
            this.printbutton.Click += new System.EventHandler(this.printbutton_Click);
            // 
            // exitbutton
            // 
            this.exitbutton.BackColor = System.Drawing.Color.DarkRed;
            this.exitbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.exitbutton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.exitbutton.Location = new System.Drawing.Point(12, 209);
            this.exitbutton.Name = "exitbutton";
            this.exitbutton.Size = new System.Drawing.Size(102, 40);
            this.exitbutton.TabIndex = 10;
            this.exitbutton.Text = "Exit";
            this.exitbutton.UseVisualStyleBackColor = false;
            this.exitbutton.Click += new System.EventHandler(this.exitbutton_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(34, 136);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(80, 20);
            this.label3.TabIndex = 11;
            this.label3.Text = "COPIES:";
            // 
            // copiesbox
            // 
            this.copiesbox.Location = new System.Drawing.Point(129, 136);
            this.copiesbox.Name = "copiesbox";
            this.copiesbox.Size = new System.Drawing.Size(86, 20);
            this.copiesbox.TabIndex = 13;
            this.copiesbox.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            // 
            // Printer
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.DarkCyan;
            this.ClientSize = new System.Drawing.Size(314, 261);
            this.ControlBox = false;
            this.Controls.Add(this.copiesbox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.exitbutton);
            this.Controls.Add(this.printbutton);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.sizebox);
            this.Controls.Add(this.colorbox);
            this.Controls.Add(this.label1);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(330, 300);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(330, 300);
            this.Name = "Printer";
            this.ShowIcon = false;
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Printer";
            ((System.ComponentModel.ISupportInitialize)(this.copiesbox)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.ComboBox colorbox;
        private System.Windows.Forms.ComboBox sizebox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button printbutton;
        private System.Windows.Forms.Button exitbutton;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.NumericUpDown copiesbox;
    }
}