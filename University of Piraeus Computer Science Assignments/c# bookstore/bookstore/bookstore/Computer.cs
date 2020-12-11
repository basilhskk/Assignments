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
    public partial class Computer : Form
    {
        public Computer()
        {
            InitializeComponent();
        }

        private void eshopbutton_Click(object sender, EventArgs e)
        {
            Eshop eshop = new Eshop();
            eshop.ShowDialog();
        }

        private void scannerbutton_Click(object sender, EventArgs e)
        {
            Scanner scanner = new Scanner();
            scanner.ShowDialog();
        }

        private void printerbutton_Click(object sender, EventArgs e)
        {
            Printer printer = new Printer();
            printer.ShowDialog();
        }

        private void exitbutton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
