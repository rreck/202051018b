```json
{
  "id": "a4bd286652165003",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288965,
  "host_pid": "9e6742732c60:1",
  "hash": "d6b2455db84232e42c2f3b0298571deb5fb7ecaec2992ead18fe2e6692cf91d8",
  "cid": "QmV1d6b2455db84232e42c2f3b0298571deb5fb7ecae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288965,
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
      "evaluated_at": 1760288965
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
  "sig": "cb3b23ba5d9210b2c650f78e05fa203917bd0417a68d0e0a32a4757482b215b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027147487
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 54478636, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285765, 'matching_hash': 'f2056111b893f4fa'}}}