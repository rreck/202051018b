```json
{
  "id": "36a631f257e0e1da",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287789,
  "host_pid": "9e6742732c60:1",
  "hash": "3d4605e47a6004c0974ba875eca7e173d01d02dfe336b5c32ea6f05b3bcfe276",
  "cid": "QmV13d4605e47a6004c0974ba875eca7e173d01d02df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287789,
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
      "evaluated_at": 1760287789
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
  "sig": "ee5693963acd147ad7ccf9711ddc4ee779019da35b1ec6c60b6770fc5c33beb5"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}