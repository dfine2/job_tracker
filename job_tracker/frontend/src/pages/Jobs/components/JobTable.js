import * as React from "react";
import styled from "@emotion/styled";

import { Box, Tooltip } from "@mui/material";

import {
  GridRowModes,
  DataGrid,
  GridActionsCellItem,
  GridRowEditStopReasons,
  Toolbar,
  ToolbarButton,
} from "@mui/x-data-grid";
import { Add, Edit, Delete, Save, Cancel } from "@mui/icons-material";

function EditToolbar(props) {
  const { setRows, setRowModesModel } = props;

  const handleClick = () => {
    setRows((oldRows) => {
      const newId =
        oldRows.length > 0 ? Math.max(...oldRows.map((r) => r.id)) + 1 : 1;

      const newRows = [
        ...oldRows,
        { id: newId, name: "", age: "", role: "", isNew: true },
      ];

      setRowModesModel((oldModel) => ({
        ...oldModel,
        [newId]: { mode: GridRowModes.Edit, fieldToFocus: "name" },
      }));

      return newRows;
    });
  };

  return (
    <Toolbar>
      <Tooltip title="Add record">
        <ToolbarButton onClick={handleClick}>
          <Add fontSize="small" />
        </ToolbarButton>
      </Tooltip>
    </Toolbar>
  );
}

function format_compensation_range({ job }) {
  const compensation_low = parseFloat(job.compensation_low);
  const compensation_high = parseFloat(job.compensation_high);
  let rounded_comp_low =
    !isNaN(compensation_low) && compensation_low != "0"
      ? `${compensation_low.toLocaleString()}`
      : null;
  let rounded_comp_high =
    !isNaN(compensation_high) && compensation_high != "0"
      ? `${compensation_high.toLocaleString()}`
      : null;
  if (rounded_comp_low && rounded_comp_high) {
    return `$${rounded_comp_low} - $${rounded_comp_high}`;
  } else if (rounded_comp_low) {
    return `$${rounded_comp_low}`;
  } else if (rounded_comp_high) {
    return `$${rounded_comp_high}`;
  } else {
    return "";
  }
}

function JobsTable({ jobs }) {
  const [rows, setRows] = React.useState([]);
  const [rowModesModel, setRowModesModel] = React.useState({});
  React.useEffect(() => {
    if (jobs && jobs.length > 0) {
      const rows_from_jobs = jobs.map((job) => ({
        id: job.id,
        company: job.company_name,
        title: job.title,
        compensation: format_compensation_range({ job }),
        workModel: job.work_model,
        location: job.location,
        source: job.posting_source,
        applicationStatus: job.application_status,
      }));
      setRows(rows_from_jobs);
    }
  }, [jobs]); // re-run when `jobs` changes

  const columns = [
    { field: "id", headerName: "ID", width: 48, maxWidth: 90 },
    {
      field: "company",
      headerName: "Company",
      width: 150,
      maxWidth: 300,
      editable: true,
    },
    {
      field: "title",
      headerName: "Title",
      width: 300,
      maxWidth: 500,
      editable: true,
    },
    {
      field: "compensation",
      headerName: "Compensation",
      width: 180,
      maxWidth: 200,
      editable: true,
    },
    {
      field: "workModel",
      headerName: "Work Model",
      type: "number",
      width: 100,
      maxWidth: 150,
      editable: true,
    },
    {
      field: "location",
      headerName: "Location",
      width: 150,
      maxWidth: 300,
      editable: true,
    },
    {
      field: "source",
      headerName: "Source",
      width: 160,
      editable: true,
    },
    {
      field: "applicationStatus",
      headerName: "Application Status",
      width: 150,
      maxWidth: 170,
      editable: true,
    },
    {
      field: "resume",
      headerName: "Resume",
      width: 160,
      editable: true,
    },
    {
      field: "coverLetter",
      headerName: "Cover Letter",
      width: 160,
      editable: true,
    },
    {
      field: "actions",
      type: "actions",
      headerName: "Actions",
      width: 100,
      cellClassName: "actions",
      getActions: ({ id }) => {
        const isInEditMode = rowModesModel[id]?.mode === GridRowModes.Edit;

        if (isInEditMode) {
          return [
            <GridActionsCellItem
              icon={<Save />}
              label="Save"
              material={{
                sx: {
                  color: "primary.main",
                },
              }}
              onClick={handleSaveClick(id)}
            />,
            <GridActionsCellItem
              icon={<Cancel />}
              label="Cancel"
              className="textPrimary"
              onClick={handleCancelClick(id)}
              color="inherit"
            />,
          ];
        }

        return [
          <GridActionsCellItem
            icon={<Edit />}
            label="Edit"
            className="textPrimary"
            onClick={handleEditClick(id)}
            color="inherit"
          />,
          <GridActionsCellItem
            icon={<Delete />}
            label="Delete"
            onClick={handleDeleteClick(id)}
            color="inherit"
          />,
        ];
      },
    },
  ];

  const handleRowUpdate = async (updatedRow) => {
    console.log(updatedRow);
    try {
      let response = await fetch(`/api/jobs/${updatedRow.id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(updatedRow),
      });
      const res = await response.json();
      return res;
    } catch (error) {
      console.error("Failed to update job:", error);
      throw error;
    }
  };

  const handleRowEditStop = (params, event) => {
    if (params.reason === GridRowEditStopReasons.rowFocusOut) {
      event.defaultMuiPrevented = true;
    }
  };
  const handleEditClick = (id) => () => {
    setRowModesModel({ ...rowModesModel, [id]: { mode: GridRowModes.Edit } });
  };

  const handleSaveClick = (id) => () => {
    setRowModesModel({ ...rowModesModel, [id]: { mode: GridRowModes.View } });
  };

  const handleDeleteClick = (id) => () => {
    setRows(rows.filter((row) => row.id !== id));
  };
  const handleCancelClick = (id) => () => {
    setRowModesModel({
      ...rowModesModel,
      [id]: { mode: GridRowModes.View, ignoreModifications: true },
    });

    const editedRow = rows.find((row) => row.id === id);
    if (editedRow.isNew) {
      setRows(rows.filter((row) => row.id !== id));
    }
  };

  const handleRowModesModelChange = (newRowModesModel) => {
    setRowModesModel(newRowModesModel);
  };

  return (
    <Box container>
      <DataGrid
        rows={rows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: {
              pageSize: 5,
            },
          },
        }}
        rowModesModel={rowModesModel}
        onRowModesModelChange={handleRowModesModelChange}
        onRowEditStop={handleRowEditStop}
        processRowUpdate={handleRowUpdate}
        slots={{ toolbar: EditToolbar }}
        slotProps={{
          toolbar: { setRows, setRowModesModel },
        }}
        showToolbar
        experimentalFeatures={{ newEditingApi: true }}
        onProcessRowUpdateError={(error) => {
          console.error("Update failed:", error);
        }}
        pageSizeOptions={[5, 10]}
      />
    </Box>
  );
}

export default JobsTable