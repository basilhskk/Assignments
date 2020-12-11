namespace bookstore
{
    partial class Bookstore
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Bookstore));
            this.labbutton = new System.Windows.Forms.Button();
            this.coffeebutton = new System.Windows.Forms.Button();
            this.exitbutton = new System.Windows.Forms.Button();
            this.eshopbutton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // labbutton
            // 
            this.labbutton.BackColor = System.Drawing.Color.Transparent;
            this.labbutton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("labbutton.BackgroundImage")));
            this.labbutton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.labbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.labbutton.Location = new System.Drawing.Point(1011, 391);
            this.labbutton.Name = "labbutton";
            this.labbutton.Size = new System.Drawing.Size(111, 108);
            this.labbutton.TabIndex = 0;
            this.labbutton.UseVisualStyleBackColor = false;
            this.labbutton.Click += new System.EventHandler(this.labbutton_Click);
            // 
            // coffeebutton
            // 
            this.coffeebutton.BackColor = System.Drawing.Color.Transparent;
            this.coffeebutton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("coffeebutton.BackgroundImage")));
            this.coffeebutton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.coffeebutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.coffeebutton.Location = new System.Drawing.Point(12, 411);
            this.coffeebutton.Name = "coffeebutton";
            this.coffeebutton.Size = new System.Drawing.Size(122, 88);
            this.coffeebutton.TabIndex = 1;
            this.coffeebutton.UseVisualStyleBackColor = false;
            this.coffeebutton.Click += new System.EventHandler(this.coffeebutton_Click);
            // 
            // exitbutton
            // 
            this.exitbutton.BackColor = System.Drawing.Color.DarkRed;
            this.exitbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.exitbutton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(161)));
            this.exitbutton.Location = new System.Drawing.Point(640, 444);
            this.exitbutton.Name = "exitbutton";
            this.exitbutton.Size = new System.Drawing.Size(141, 55);
            this.exitbutton.TabIndex = 2;
            this.exitbutton.Text = "Exit Store";
            this.exitbutton.UseVisualStyleBackColor = false;
            this.exitbutton.Click += new System.EventHandler(this.exitbutton_Click);
            // 
            // eshopbutton
            // 
            this.eshopbutton.BackColor = System.Drawing.Color.LightYellow;
            this.eshopbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.eshopbutton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(161)));
            this.eshopbutton.Location = new System.Drawing.Point(411, 444);
            this.eshopbutton.Name = "eshopbutton";
            this.eshopbutton.Size = new System.Drawing.Size(167, 55);
            this.eshopbutton.TabIndex = 3;
            this.eshopbutton.Text = "Go to e-shop";
            this.eshopbutton.UseVisualStyleBackColor = false;
            this.eshopbutton.Click += new System.EventHandler(this.eshopbutton_Click);
            // 
            // Bookstore
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(1134, 511);
            this.ControlBox = false;
            this.Controls.Add(this.eshopbutton);
            this.Controls.Add(this.exitbutton);
            this.Controls.Add(this.coffeebutton);
            this.Controls.Add(this.labbutton);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(1150, 550);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(1150, 550);
            this.Name = "Bookstore";
            this.ShowIcon = false;
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Bookstore";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button labbutton;
        private System.Windows.Forms.Button coffeebutton;
        private System.Windows.Forms.Button exitbutton;
        private System.Windows.Forms.Button eshopbutton;
    }
}

