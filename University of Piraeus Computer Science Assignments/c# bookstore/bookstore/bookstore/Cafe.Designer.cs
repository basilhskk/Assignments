namespace bookstore
{
    partial class Cafe
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Cafe));
            this.orderbutton = new System.Windows.Forms.Button();
            this.backbutton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // orderbutton
            // 
            this.orderbutton.BackColor = System.Drawing.Color.Transparent;
            this.orderbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.orderbutton.Font = new System.Drawing.Font("Lucida Handwriting", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.orderbutton.Location = new System.Drawing.Point(91, 418);
            this.orderbutton.Name = "orderbutton";
            this.orderbutton.Size = new System.Drawing.Size(279, 64);
            this.orderbutton.TabIndex = 0;
            this.orderbutton.Text = "Place your order and sit!";
            this.orderbutton.UseVisualStyleBackColor = false;
            this.orderbutton.Click += new System.EventHandler(this.orderbutton_Click);
            // 
            // backbutton
            // 
            this.backbutton.BackColor = System.Drawing.Color.Transparent;
            this.backbutton.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("backbutton.BackgroundImage")));
            this.backbutton.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.backbutton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.backbutton.Location = new System.Drawing.Point(12, 425);
            this.backbutton.Name = "backbutton";
            this.backbutton.Size = new System.Drawing.Size(58, 54);
            this.backbutton.TabIndex = 4;
            this.backbutton.UseVisualStyleBackColor = false;
            this.backbutton.Click += new System.EventHandler(this.backbutton_Click);
            // 
            // Cafe
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("$this.BackgroundImage")));
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(664, 491);
            this.ControlBox = false;
            this.Controls.Add(this.backbutton);
            this.Controls.Add(this.orderbutton);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(680, 530);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(680, 530);
            this.Name = "Cafe";
            this.ShowIcon = false;
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Cafe";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button orderbutton;
        private System.Windows.Forms.Button backbutton;
    }
}