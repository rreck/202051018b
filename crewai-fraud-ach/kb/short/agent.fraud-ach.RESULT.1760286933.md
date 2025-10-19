```json
{
  "id": "33c3e403fde40921",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286933,
  "host_pid": "9e6742732c60:1",
  "hash": "3eabe295f4eaa746090363aaf55f7a303dbc98448a19fb7960d031f15ce62d93",
  "cid": "QmV13eabe295f4eaa746090363aaf55f7a303dbc9844",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286933,
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
      "evaluated_at": 1760286933
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
  "sig": "e3767c230e39ac8183d97eef55ec754e581fbda61d31b8f3e84a493699f78f04"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156760115
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13472424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285764, 'matching_hash': '84a7174d04c2e814'}}}