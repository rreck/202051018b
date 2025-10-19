```json
{
  "id": "e180f0a36fccd2c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288456,
  "host_pid": "9e6742732c60:1",
  "hash": "c99ae1640fcb7ebaf5f2d71798445729375bc4bc3c34db8c311689a7be357e64",
  "cid": "QmV1c99ae1640fcb7ebaf5f2d71798445729375bc4bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288456,
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
      "evaluated_at": 1760288456
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
  "sig": "d3bf8f98a57e942e2665761d7b2ddd4e5d230f2acd8bad69d0b49144ff633589"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020127754
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 17683468, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '0e6816faa7d68d85'}}}