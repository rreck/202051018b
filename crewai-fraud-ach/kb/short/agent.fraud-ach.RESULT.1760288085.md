```json
{
  "id": "705ef33e738db89b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288085,
  "host_pid": "9e6742732c60:1",
  "hash": "4d3b58a3e1673084a04abcb18f3d23841bfa31f4284c984dd0c2450c350caaf6",
  "cid": "QmV14d3b58a3e1673084a04abcb18f3d23841bfa31f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288085,
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
      "evaluated_at": 1760288085
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
  "sig": "d2bbcf33936fe7b994d2725bfc63bd106144125d111aee9c9936e568ec2a10ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026494478
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 15540394, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285763, 'matching_hash': 'bca1271a1f86b87c'}}}}}