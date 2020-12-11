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
    public partial class LabRoom : Form
    {
        public LabRoom()
        {
            InitializeComponent();
        }

        private void scannerbutton_Click(object sender, EventArgs e)
        {
            Scanner scanner = new Scanner();
            scanner.ShowDialog();
        }

        private void pcbutton_Click(object sender, EventArgs e)
        {
            Computer computer = new Computer();
            computer.ShowDialog();
        }

        private void printerbutton_Click(object sender, EventArgs e)
        {
            Printer printer = new Printer();
            printer.ShowDialog();
        }

        private void backbutton_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
