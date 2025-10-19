```json
{
  "id": "82ea0e6db5628a59",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285597,
  "host_pid": "9e6742732c60:1",
  "hash": "0a56bcb10156b6bc5624cf7f1a423b7ed1ffde61619e2633a6d057940055fe18",
  "cid": "QmV10a56bcb10156b6bc5624cf7f1a423b7ed1ffde61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285597,
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
      "evaluated_at": 1760285597
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
  "sig": "945460b6f50e61a50c8ffe743da039fe649fb6bbe6eae04ddd1c0d76903a90b2"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 026009592035169
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 28815851, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760284979, 'matching_hash': 'af51af40be20c608'}}}