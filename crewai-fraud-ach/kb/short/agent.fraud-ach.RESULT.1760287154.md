```json
{
  "id": "9ef2bcd399ec00ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287154,
  "host_pid": "9e6742732c60:1",
  "hash": "be1edc4b1551885c445d1a002d8a69ec65f7cd86e96f0405df59c2b53b279619",
  "cid": "QmV1be1edc4b1551885c445d1a002d8a69ec65f7cd86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287154,
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
      "evaluated_at": 1760287154
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
  "sig": "d7824a48c7e41052c15c2829f7e099984e6ba8ec07d7aaefab6d079f59493446"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000026169646
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14901700, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285764, 'matching_hash': '09339571c5d51c89'}}}