namespace bookstore
{
    partial class LabRoom
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(LabRoom));
            this.pcbutton = new System.Windows.Forms.Button();
            this.scannerbutton = new System.Windows.Forms.Button();
            this.printerbutton = new System.Windows.Forms.Button();
            this.backbutton = new System.Windows.Forms.Button();
            this.backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
            this.SuspendLayout();
            // 
            // pcbutton
            // 
            this.pcbutton.BackColor = System.Drawing.Color.Transparent;
            this.pcbutton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("pcbutton.BackgroundImage")));
            this.pcbutton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.pcbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.pcbutton.ForeColor = System.Drawing.Color.Transparent;
            this.pcbutton.Location = new System.Drawing.Point(293, 203);
            this.pcbutton.Name = "pcbutton";
            this.pcbutton.Size = new System.Drawing.Size(392, 266);
            this.pcbutton.TabIndex = 0;
            this.pcbutton.UseVisualStyleBackColor = false;
            this.pcbutton.Click += new System.EventHandler(this.pcbutton_Click);
            // 
            // scannerbutton
            // 
            this.scannerbutton.BackColor = System.Drawing.Color.Transparent;
            this.scannerbutton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("scannerbutton.BackgroundImage")));
            this.scannerbutton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.scannerbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.scannerbutton.ForeColor = System.Drawing.Color.Transparent;
            this.scannerbutton.Location = new System.Drawing.Point(36, 279);
            this.scannerbutton.Name = "scannerbutton";
            this.scannerbutton.Size = new System.Drawing.Size(251, 190);
            this.scannerbutton.TabIndex = 1;
            this.scannerbutton.UseVisualStyleBackColor = false;
            this.scannerbutton.Click += new System.EventHandler(this.scannerbutton_Click);
            // 
            // printerbutton
            // 
            this.printerbutton.BackColor = System.Drawing.Color.Transparent;
            this.printerbutton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("printerbutton.BackgroundImage")));
            this.printerbutton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.printerbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.printerbutton.ForeColor = System.Drawing.Color.Transparent;
            this.printerbutton.Location = new System.Drawing.Point(691, 221);
            this.printerbutton.Name = "printerbutton";
            this.printerbutton.Size = new System.Drawing.Size(246, 248);
            this.printerbutton.TabIndex = 2;
            this.printerbutton.UseVisualStyleBackColor = false;
            this.printerbutton.Click += new System.EventHandler(this.printerbutton_Click);
            // 
            // backbutton
            // 
            this.backbutton.BackColor = System.Drawing.Color.Transparent;
            this.backbutton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("backbutton.BackgroundImage")));
            this.backbutton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.backbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.backbutton.Location = new System.Drawing.Point(12, 12);
            this.backbutton.Name = "backbutton";
            this.backbutton.Size = new System.Drawing.Size(70, 62);
            this.backbutton.TabIndex = 3;
            this.backbutton.UseVisualStyleBackColor = false;
            this.backbutton.Click += new System.EventHandler(this.backbutton_Click);
            // 
            // LabRoom
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(984, 481);
            this.ControlBox = false;
            this.Controls.Add(this.backbutton);
            this.Controls.Add(this.printerbutton);
            this.Controls.Add(this.scannerbutton);
            this.Controls.Add(this.pcbutton);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(1000, 520);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(1000, 520);
            this.Name = "LabRoom";
            this.ShowIcon = false;
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Computer Lab";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button pcbutton;
        private System.Windows.Forms.Button scannerbutton;
        private System.Windows.Forms.Button printerbutton;
        private System.Windows.Forms.Button backbutton;
        private System.ComponentModel.BackgroundWorker backgroundWorker1;
    }
}