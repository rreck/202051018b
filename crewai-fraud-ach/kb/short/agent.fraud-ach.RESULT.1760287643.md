```json
{
  "id": "268a0520865d7103",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287643,
  "host_pid": "9e6742732c60:1",
  "hash": "acd5e14486c1ee4f9451e2bfeb32e72ace8b2155a3871534738e163db1032e7e",
  "cid": "QmV1acd5e14486c1ee4f9451e2bfeb32e72ace8b2155",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287643,
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
      "evaluated_at": 1760287643
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
  "sig": "738e4f6e76ebd4ee1d9ec9736d260f9b1e14d47bbd52694d373d6623a92a18f1"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}