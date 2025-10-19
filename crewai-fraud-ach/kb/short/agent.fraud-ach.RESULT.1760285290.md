```json
{
  "id": "8e4d39871b6537a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285290,
  "host_pid": "9e6742732c60:1",
  "hash": "9efe55af88a8db137ad586217b4aa570da979e6469b8b5281dfb8984529ed3cb",
  "cid": "QmV19efe55af88a8db137ad586217b4aa570da979e64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285290,
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
      "evaluated_at": 1760285290
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
  "sig": "eb39ab3359c296b61fa8c9fc16522ed73707e15d9bf7a23d84c33a335c92f432"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13063214, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 30, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}