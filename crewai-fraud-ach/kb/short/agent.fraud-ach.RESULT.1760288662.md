```json
{
  "id": "f37e06565e17d0a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288662,
  "host_pid": "9e6742732c60:1",
  "hash": "719b9e9640a930ca692e7a2a6b8d6b6a68bfe383338d48e8ee7c0f30c0d5964f",
  "cid": "QmV1719b9e9640a930ca692e7a2a6b8d6b6a68bfe383",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288662,
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
      "evaluated_at": 1760288662
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "aa7c279cdf244462bd1db4c4bf4b2f194f7204fddaea29ea912d6d70a3af29b0"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000027783297
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 50000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285765, 'matching_hash': '92df9dc264d0d07b'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}