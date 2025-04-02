import React, { useState, useEffect } from "react";
import DataTable from "react-data-table-component";
import axios from "axios";
import Swal from "sweetalert2";

const UserDataTable = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [showModal, setShowModal] = useState(false);
  const [selectedUser, setSelectedUser] = useState(null);
  const [editedUser, setEditedUser] = useState({ name: "", email: "", tel: "" });

  const columns = [
    { name: "Nombre", selector: (row) => row.name, sortable: true },
    { name: "Email", selector: (row) => row.email, sortable: true },
    { name: "Teléfono", selector: (row) => row.tel },
    {
      name: "Acciones",
      cell: (row) => (
        <span>
          <button className="btn btn-warning me-4" onClick={() => openEditModal(row)}>
            <i className="bi bi-pencil"></i>
          </button>
          <button className="btn btn-danger" onClick={() => confirmDelete(row.id)}>
            <i className="bi bi-trash"></i>
          </button>
        </span>
      ),
    },
  ];

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/users/api/")
      .then((response) => setData(response.data))
      .catch((error) => console.error("Error al cargar los datos:", error))
      .finally(() => setLoading(false));
  }, []);

  const confirmDelete = (id) => {
    Swal.fire({
      title: "¿Estás seguro?",
      text: "Esta acción no se puede deshacer.",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#d33",
      cancelButtonColor: "#3085d6",
      confirmButtonText: "Sí, eliminar",
      cancelButtonText: "Cancelar",
    }).then((result) => {
      if (result.isConfirmed) {
        handleDelete(id);
      }
    });
  };

  const handleDelete = (id) => {
    const token = localStorage.getItem("accessToken");
    if (!token) return alert("No estás autenticado. Por favor, inicia sesión.");

    axios
      .delete(`http://127.0.0.1:8000/users/api/${id}/`, { headers: { Authorization: `Bearer ${token}` } })
      .then(() => {
        setData((prev) => prev.filter((user) => user.id !== id));
        Swal.fire("Eliminado", "El usuario ha sido eliminado correctamente.", "success");
      })
      .catch((error) => {
        const status = error.response?.status;
        if (status === 401) alert("No autorizado. Por favor, verifica tu sesión.");
        else console.error("Error al eliminar el registro", error);
      });
  };

  const openEditModal = (user) => {
    setSelectedUser(user);
    setEditedUser({ name: user.name, email: user.email, tel: user.tel });
    setShowModal(true);
  };

  const handleEdit = () => {
    const token = localStorage.getItem("accessToken");
    if (!token) return alert("No estás autenticado. Por favor, inicia sesión.");

    const updatedUser = { ...selectedUser, ...editedUser };
    axios
      .put(`http://127.0.0.1:8000/users/api/${selectedUser.id}/`, updatedUser, {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((response) => {
        setData((prev) => prev.map((user) => (user.id === selectedUser.id ? response.data : user)));
        setShowModal(false);
        Swal.fire("Actualizado", "El usuario ha sido actualizado correctamente.", "success");
      })
      .catch((error) => {
        const status = error.response?.status;
        if (status === 400) alert("Error: Verifica los datos ingresados.");
        else if (status === 401) alert("No autorizado. Por favor, verifica tu sesión.");
        else console.error("Error al actualizar el registro", error);
      });
  };

  return (
    <div>
      <h3>Tabla de usuarios</h3>
      <DataTable columns={columns} data={data} progressPending={loading} pagination highlightOnHover pointerOnHover />
      {showModal && (
        <div className="modal" style={{ display: "block" }}>
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Editar Usuario</h5>
                <button type="button" className="btn-close" onClick={() => setShowModal(false)}></button>
              </div>
              <div className="modal-body">
                {["name", "email", "tel"].map((field) => (
                  <div className="mb-3" key={field}>
                    <label className="form-label">{field.charAt(0).toUpperCase() + field.slice(1)}</label>
                    <input
                      type={field === "email" ? "email" : "text"}
                      className="form-control"
                      value={editedUser[field]}
                      onChange={(e) => setEditedUser({ ...editedUser, [field]: e.target.value })}
                    />
                  </div>
                ))}
              </div>
              <div className="modal-footer">
                <button type="button" className="btn btn-secondary" onClick={() => setShowModal(false)}>
                  Cancelar
                </button>
                <button type="button" className="btn btn-primary" onClick={handleEdit}>
                  Guardar cambios
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default UserDataTable;
