```json
{
  "id": "7a252de24a1cf9ec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286222,
  "host_pid": "9e6742732c60:1",
  "hash": "a539dfddac36e0de8b5223901592d84d869823ea7cc60729838d74ffc5a461db",
  "cid": "QmV1a539dfddac36e0de8b5223901592d84d869823ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286222,
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
      "evaluated_at": 1760286222
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
  "sig": "a446b973ee0c6a751fac043535870df6f189eb0b8e90f0d0c8e209c98880e76e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000031078531
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285765, 'matching_hash': '2bea5b783a868e31'}}}