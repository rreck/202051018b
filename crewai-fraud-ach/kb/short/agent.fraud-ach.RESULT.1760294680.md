```json
{
  "id": "cff9a216bc5b58ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294680,
  "host_pid": "9e6742732c60:1",
  "hash": "2e95c8a7c8ad19e4fc03117eb01ff78965582f2123ce540d0d47a38131b0ea0a",
  "cid": "QmV12e95c8a7c8ad19e4fc03117eb01ff78965582f21",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294680,
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
      "evaluated_at": 1760294680
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
  "sig": "8e625c4d2c8556602ddc080cabfeb06732ef5444efa284b8ccb7d8bb7c55d3f3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 21432488, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}