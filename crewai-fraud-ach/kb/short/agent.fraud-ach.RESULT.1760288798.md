```json
{
  "id": "19f9ff93116a894b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288798,
  "host_pid": "9e6742732c60:1",
  "hash": "43e70bb557cc116795824768b072f6750ceb2a5d75d430f0b564ed1c62d84ad5",
  "cid": "QmV143e70bb557cc116795824768b072f6750ceb2a5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288798,
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
      "evaluated_at": 1760288798
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
  "sig": "76949f82e5c66f042d49395c94ce38ed2cc96daa5d627ba85ca56078da4d3bab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242075877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 104, 'threshold': 50, 'total_amount': 13021320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 103, 'first_seen': 1760285765, 'matching_hash': '7e39a816a4a44fcc'}}}