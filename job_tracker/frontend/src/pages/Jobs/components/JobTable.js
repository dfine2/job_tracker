import * as React from "react";
import styled from "@emotion/styled";

import { Box } from "@mui/material";

import { DataGrid } from "@mui/x-data-grid";


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

function JobsTable({ jobs }) {
  console.log(jobs);
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
    },
    {
      field: "source",
      headerName: "Source",
      width: 160,
    },
    {
      field: "applicationStatus",
      headerName: "Application Status",
      width: 150,
      maxWidth: 170,
    },
    {
      field: "resume",
      headerName: "Resume",
      width: 160,
    },
    {
      field: "coverLetter",
      headerName: "Cover Letter",
      width: 160,
    },
  ];
  const rows = jobs.map((job) => {
    console.log(job);
    return {
      id: job.id,
      company: job.company_name,
      title: job.title,
      compensation: format_compensation_range({ job }),
      workModel: job.work_model,
      location: job.location,
      source: job.source,
      applicationStatus: job.application_status,
    };
  });

  return (
    <Box container sx={{ height: 400, width: 1500 }}>
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
        processRowUpdate={handleRowUpdate}
        experimentalFeatures={{ newEditingApi: true }}
        onProcessRowUpdateError={(error) => {
          console.error("Update failed:", error);
        }}
        pageSizeOptions={[5]}
        checkboxSelection
        disableRowSelectionOnClick
      />
    </Box>
  );
}

export default JobsTable