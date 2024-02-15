// Dummy data for demonstration
const complaintsData = [
    { regNumber: "REG001", name: "John Doe", email: "john@example.com", phone: "123-456-7890", message: "This is a complaint message." },
    { regNumber: "REG002", name: "Jane Doe", email: "jane@example.com", phone: "987-654-3210", message: "Another complaint message." }
];

// Function to display complaints
function displayComplaints() {
    const complaintsTable = document.getElementById('complaints-table');
    complaintsTable.innerHTML = '';

    complaintsData.forEach(complaint => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${complaint.regNumber}</td>
            <td>${complaint.name}</td>
            <td>${complaint.email}</td>
            <td>${complaint.phone}</td>
            <td>${complaint.message}</td>
            <td><button class="action-btn" onclick="deleteComplaint('${complaint.regNumber}')">Delete</button></td>
        `;
        complaintsTable.appendChild(row);
    });
}

// Function to delete a complaint
function deleteComplaint(regNumber) {
    const index = complaintsData.findIndex(complaint => complaint.regNumber === regNumber);
    if (index !== -1) {
        complaintsData.splice(index, 1);
        displayComplaints();
    }
}

// Display complaints when the page loads
window.onload = function() {
    displayComplaints();
};
