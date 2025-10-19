```json
{
  "id": "37ec3c19774796a0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291180,
  "host_pid": "9e6742732c60:1",
  "hash": "edc91eddef2f8a00d492c385377aa13a8d5fcb5898579a26a49f9acce47642f7",
  "cid": "QmV1edc91eddef2f8a00d492c385377aa13a8d5fcb58",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291180,
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
      "evaluated_at": 1760291180
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
  "sig": "c708f88f249a562380fb860f7b8fe485bb14f9a49142d4bbe07f0adf8b6593ff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463831807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 30466475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': 'ac2384e4a351cc1b'}}}