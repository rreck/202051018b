```json
{
  "id": "ae635de8ff752201",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286735,
  "host_pid": "9e6742732c60:1",
  "hash": "e2eb3644692d697669716ee45ec970e8ae12e24aa0bc4b3ac8bf851bd1a1069a",
  "cid": "QmV1e2eb3644692d697669716ee45ec970e8ae12e24a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286735,
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
      "evaluated_at": 1760286735
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
  "sig": "52e380966388d7f1ce21e450198632b4f770477518079b7672e7250e6671b90c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000035733360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11489310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}