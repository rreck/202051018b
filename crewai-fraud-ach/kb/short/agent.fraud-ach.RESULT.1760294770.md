```json
{
  "id": "2bf655b2295628ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294770,
  "host_pid": "9e6742732c60:1",
  "hash": "e7f3c4abe282ae62aff8673393bd43ffe67cbf1ada2ed4aebf81441aabf162e5",
  "cid": "QmV1e7f3c4abe282ae62aff8673393bd43ffe67cbf1a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294770,
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
      "evaluated_at": 1760294770
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
  "sig": "6671d5eeea11e02071e4bbf1c89d0f910603b718036bbb5f02d7e14438b073e2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240708140
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 26038948, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': 'e22b1a9baac54cae'}}}