namespace bookstore
{
    partial class Computer
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Computer));
            this.scannerbutton = new System.Windows.Forms.Button();
            this.printerbutton = new System.Windows.Forms.Button();
            this.exitbutton = new System.Windows.Forms.Button();
            this.eshopbutton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // scannerbutton
            // 
            this.scannerbutton.BackColor = System.Drawing.Color.Transparent;
            this.scannerbutton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("scannerbutton.BackgroundImage")));
            this.scannerbutton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.scannerbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.scannerbutton.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(161)));
            this.scannerbutton.Location = new System.Drawing.Point(12, 144);
            this.scannerbutton.Name = "scannerbutton";
            this.scannerbutton.Size = new System.Drawing.Size(107, 105);
            this.scannerbutton.TabIndex = 0;
            this.scannerbutton.UseVisualStyleBackColor = false;
            this.scannerbutton.Click += new System.EventHandler(this.scannerbutton_Click);
            // 
            // printerbutton
            // 
            this.printerbutton.BackColor = System.Drawing.Color.Transparent;
            this.printerbutton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("printerbutton.BackgroundImage")));
            this.printerbutton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.printerbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.printerbutton.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(161)));
            this.printerbutton.Location = new System.Drawing.Point(12, 275);
            this.printerbutton.Name = "printerbutton";
            this.printerbutton.Size = new System.Drawing.Size(107, 105);
            this.printerbutton.TabIndex = 1;
            this.printerbutton.UseVisualStyleBackColor = false;
            this.printerbutton.Click += new System.EventHandler(this.printerbutton_Click);
            // 
            // exitbutton
            // 
            this.exitbutton.BackColor = System.Drawing.Color.DarkRed;
            this.exitbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.exitbutton.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(161)));
            this.exitbutton.Location = new System.Drawing.Point(12, 556);
            this.exitbutton.Name = "exitbutton";
            this.exitbutton.Size = new System.Drawing.Size(132, 43);
            this.exitbutton.TabIndex = 2;
            this.exitbutton.Text = "Exit computer";
            this.exitbutton.UseVisualStyleBackColor = false;
            this.exitbutton.Click += new System.EventHandler(this.exitbutton_Click);
            // 
            // eshopbutton
            // 
            this.eshopbutton.BackColor = System.Drawing.Color.Transparent;
            this.eshopbutton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("eshopbutton.BackgroundImage")));
            this.eshopbutton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.eshopbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.eshopbutton.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(161)));
            this.eshopbutton.Location = new System.Drawing.Point(12, 12);
            this.eshopbutton.Name = "eshopbutton";
            this.eshopbutton.Size = new System.Drawing.Size(107, 105);
            this.eshopbutton.TabIndex = 3;
            this.eshopbutton.UseVisualStyleBackColor = false;
            this.eshopbutton.Click += new System.EventHandler(this.eshopbutton_Click);
            // 
            // Computer
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(984, 611);
            this.ControlBox = false;
            this.Controls.Add(this.eshopbutton);
            this.Controls.Add(this.exitbutton);
            this.Controls.Add(this.printerbutton);
            this.Controls.Add(this.scannerbutton);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(1000, 650);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(1000, 650);
            this.Name = "Computer";
            this.ShowIcon = false;
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Computer";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button scannerbutton;
        private System.Windows.Forms.Button printerbutton;
        private System.Windows.Forms.Button exitbutton;
        private System.Windows.Forms.Button eshopbutton;
    }
}