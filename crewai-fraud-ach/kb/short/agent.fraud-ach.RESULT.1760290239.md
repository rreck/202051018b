```json
{
  "id": "347bb9639cb82ef4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290239,
  "host_pid": "9e6742732c60:1",
  "hash": "46bfd510c30cff0974395036f9514e14ecec1dca63316d665b74291d8578580b",
  "cid": "QmV146bfd510c30cff0974395036f9514e14ecec1dca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290239,
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
      "evaluated_at": 1760290239
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
  "sig": "f698e31fccb9feddd288eefcc03413a2bb2f58679aab2bb6d435e060b916425c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464030736
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 16170980, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': 'cf146634c1028d90'}}}