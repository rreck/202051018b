```json
{
  "id": "259c28ff5d663d26",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287012,
  "host_pid": "9e6742732c60:1",
  "hash": "13f34e56eff2c430e81c2df681db41459c3fcb90eca697cb25fbae374ca00938",
  "cid": "QmV113f34e56eff2c430e81c2df681db41459c3fcb90",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287012,
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
      "evaluated_at": 1760287012
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
  "sig": "d9f28d10be9157e5ad1d7146efd0576700adb08fc787df4b4fb02b63768922e1"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100273021249
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21701025, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285764, 'matching_hash': '8f9c0aaacb6951b9'}}}