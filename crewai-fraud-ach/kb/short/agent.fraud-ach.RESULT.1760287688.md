```json
{
  "id": "eaa70cab1a805f96",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287688,
  "host_pid": "9e6742732c60:1",
  "hash": "114b5587644d7ddd0058ba3294c52e55705a07bffd13cf47c588d7537f5f752c",
  "cid": "QmV1114b5587644d7ddd0058ba3294c52e55705a07bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287688,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760287688
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "98199b7b1f4fe5635f4a80bd67280646dbc67cf7286bec86c5016620bd622a73"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 044000032341010
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285763, 'matching_hash': 'f26a81694d784881'}}} 'matching_hash': '91e9478c27780a65'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -2106683.5, 'upper': 4084502.5}, 'amount': 6875376}}}