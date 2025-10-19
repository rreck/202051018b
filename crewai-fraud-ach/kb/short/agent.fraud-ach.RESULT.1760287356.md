```json
{
  "id": "addd6c13d0297219",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287356,
  "host_pid": "9e6742732c60:1",
  "hash": "366cd88fbf3c1731f6cdecab1a534b670b33be497ed018590cea819c97590eeb",
  "cid": "QmV1366cd88fbf3c1731f6cdecab1a534b670b33be49",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287356,
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
      "evaluated_at": 1760287356
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
  "sig": "fe2ba863e7680f56c9e81e15fe5fb7d592357d78e3ebb292764c1680f724df80"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000021660412
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 18363747, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285764, 'matching_hash': '19be1dcf8b4c513c'}}}