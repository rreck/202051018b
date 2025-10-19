```json
{
  "id": "0801ce5ccefea812",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289839,
  "host_pid": "9e6742732c60:1",
  "hash": "647bed22d7f65e3e01d6a72a0f930c672b0b7cd6bb9c5c8301e8450c6d555f22",
  "cid": "QmV1647bed22d7f65e3e01d6a72a0f930c672b0b7cd6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289839,
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
      "evaluated_at": 1760289839
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
  "sig": "9780431353ec92243d708fd755e70802af149ff6493cebc76f6e872a401b2c96"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243970709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 134, 'threshold': 50, 'total_amount': 11867576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 133, 'first_seen': 1760285765, 'matching_hash': '886d04c9297a738f'}}}