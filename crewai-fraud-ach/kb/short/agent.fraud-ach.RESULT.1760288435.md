```json
{
  "id": "f25a27aaa77a6f27",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288435,
  "host_pid": "9e6742732c60:1",
  "hash": "c03caabc68b3152aee28d23616fef65e89ff787ce9e3278bbe6401315c7c9775",
  "cid": "QmV1c03caabc68b3152aee28d23616fef65e89ff787c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288435,
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
      "evaluated_at": 1760288435
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
  "sig": "fd6d5a4d73b6b61fdbe11a3aa7db818d53846d80eb9cadbcf3d88d79796803ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469922578
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 11412495, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285763, 'matching_hash': '96901979868c282a'}}}