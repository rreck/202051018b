```json
{
  "id": "afa38fb4347c8e39",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287847,
  "host_pid": "9e6742732c60:1",
  "hash": "c3ff49728f99bc0cf38022e244fd139c719a526fa7b8f11b542742a55766936b",
  "cid": "QmV1c3ff49728f99bc0cf38022e244fd139c719a526f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287847,
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
      "evaluated_at": 1760287847
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
  "sig": "14a8eeb0881b23729bebc70def7b3aa6afdfe7dcfca80baad3bdabb450507b74"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 026009593456245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 35651202, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285764, 'matching_hash': '5bbbd28055422217'}}}