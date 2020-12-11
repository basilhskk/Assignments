namespace bookstore
{
    partial class Scanner
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
            this.scanbutton = new System.Windows.Forms.Button();
            this.exitbutton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // scanbutton
            // 
            this.scanbutton.BackColor = System.Drawing.Color.OliveDrab;
            this.scanbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.scanbutton.Location = new System.Drawing.Point(14, 14);
            this.scanbutton.Margin = new System.Windows.Forms.Padding(5);
            this.scanbutton.Name = "scanbutton";
            this.scanbutton.Size = new System.Drawing.Size(356, 72);
            this.scanbutton.TabIndex = 0;
            this.scanbutton.Text = "SCAN AND SAVE";
            this.scanbutton.UseVisualStyleBackColor = false;
            this.scanbutton.Click += new System.EventHandler(this.scanbutton_Click);
            // 
            // exitbutton
            // 
            this.exitbutton.BackColor = System.Drawing.Color.DarkRed;
            this.exitbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.exitbutton.Location = new System.Drawing.Point(14, 128);
            this.exitbutton.Name = "exitbutton";
            this.exitbutton.Size = new System.Drawing.Size(210, 51);
            this.exitbutton.TabIndex = 1;
            this.exitbutton.Text = "EXIT WITHOUT SCAN";
            this.exitbutton.UseVisualStyleBackColor = false;
            this.exitbutton.Click += new System.EventHandler(this.exitbutton_Click);
            // 
            // Scanner
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.LightGray;
            this.ClientSize = new System.Drawing.Size(384, 191);
            this.ControlBox = false;
            this.Controls.Add(this.exitbutton);
            this.Controls.Add(this.scanbutton);
            this.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(161)));
            this.Margin = new System.Windows.Forms.Padding(5);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(400, 230);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(400, 230);
            this.Name = "Scanner";
            this.ShowIcon = false;
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Scanner";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button scanbutton;
        private System.Windows.Forms.Button exitbutton;
    }
}