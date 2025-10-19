```json
{
  "id": "b921a86a7c84855f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292273,
  "host_pid": "9e6742732c60:1",
  "hash": "9ff9bc6d230988905a34f7f249830fe97741794d5e18e7f6e4a7979d97044b42",
  "cid": "QmV19ff9bc6d230988905a34f7f249830fe97741794d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292273,
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
      "evaluated_at": 1760292273
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
  "sig": "5c0e881a354cb08aa29d482bc960b5412e5578d539ee630cec8936b5bba2c4fc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241053391
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 83125702, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': '6e04470f15e4fc18'}}}