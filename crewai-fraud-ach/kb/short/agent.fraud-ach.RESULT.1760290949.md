```json
{
  "id": "0d9ac9e842c48e73",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290949,
  "host_pid": "9e6742732c60:1",
  "hash": "680f8827e706515261ad2e1e6a98a14fc22647823b150446eb6637438cb147f3",
  "cid": "QmV1680f8827e706515261ad2e1e6a98a14fc2264782",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290949,
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
      "evaluated_at": 1760290949
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
  "sig": "5d615483991cbf91eb7b31fdef36eb3c3465d050d767a62cebf543cc621ad78e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022029056
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 32062752, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285765, 'matching_hash': '0de74255bde38153'}}}