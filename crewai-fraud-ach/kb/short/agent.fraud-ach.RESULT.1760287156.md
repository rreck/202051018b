```json
{
  "id": "331cbf748d6535ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287156,
  "host_pid": "9e6742732c60:1",
  "hash": "f62fe4a28ce1ffad135145626bc3a3a13b88a9adb8ef73ea8db99fcd6202b6e4",
  "cid": "QmV1f62fe4a28ce1ffad135145626bc3a3a13b88a9ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287156,
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
      "evaluated_at": 1760287156
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "0c3d01bff523b0956ae8c41698eadb28e53f6b3144f237ddd0f76f10f9a3eba9"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000023367694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 20969750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285763, 'matching_hash': '23afc27b7b9a7115'}}}