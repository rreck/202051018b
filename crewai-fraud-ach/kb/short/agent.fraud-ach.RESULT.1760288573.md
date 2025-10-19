```json
{
  "id": "eb8d646dd7342a1f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288573,
  "host_pid": "9e6742732c60:1",
  "hash": "c5b32a10c284cf4d3b385e6ecf4a79f8c989fce59641485a5107b1ef266e16d6",
  "cid": "QmV1c5b32a10c284cf4d3b385e6ecf4a79f8c989fce5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288573,
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
      "evaluated_at": 1760288573
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
  "sig": "324c6c074ece427870122a59f3511bd11371b0b661e4d9465e383d662fff306d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150171825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 97, 'threshold': 50, 'total_amount': 18232993, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 96, 'first_seen': 1760285765, 'matching_hash': 'da3473f59eec3040'}}}