```json
{
  "id": "5bd6eafd5ef71ec0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288626,
  "host_pid": "9e6742732c60:1",
  "hash": "b0cc2e9b932762c954a7e3d1ebea56eec3d3789d7274124edc229f37956f9671",
  "cid": "QmV1b0cc2e9b932762c954a7e3d1ebea56eec3d3789d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288626,
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
      "evaluated_at": 1760288626
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
  "sig": "d2e1689267f1697fc4a594fa5e281b71e334ced5001779793e2232faebcbd003"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461912165
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 34760781, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': 'd770463353c2594b'}}}