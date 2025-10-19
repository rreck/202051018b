```json
{
  "id": "a28afcb3da40826f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290952,
  "host_pid": "9e6742732c60:1",
  "hash": "dfa55cbd1d8115ef1a6e972892af8bc5318c379baf27bbccb20c3900bba0b850",
  "cid": "QmV1dfa55cbd1d8115ef1a6e972892af8bc5318c379b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290952,
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
      "evaluated_at": 1760290952
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
  "sig": "f6eb8e2c7f8acec2970d436b4369555b5198f8e854e137e6c471a3be033fdec4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597908242
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 18658121, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': 'd5ac49343fc3272b'}}}