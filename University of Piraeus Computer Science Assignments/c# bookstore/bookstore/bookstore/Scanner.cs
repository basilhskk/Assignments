using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace bookstore
{
    public partial class Scanner : Form
    {
        public Scanner()
        {
            InitializeComponent();
        }

        private void scanbutton_Click(object sender, EventArgs e)
        {
            System.Threading.Thread.Sleep(700);
            MessageBox.Show("SCAN COMPLETED SUCCESSFULLY!","Success!");
            this.Close();
        }

        private void exitbutton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
