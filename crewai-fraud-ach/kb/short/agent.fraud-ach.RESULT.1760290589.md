```json
{
  "id": "f29998cc3e9358b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290589,
  "host_pid": "9e6742732c60:1",
  "hash": "ff912dd9a3349b682a36dfd3ac71d415caad6f130e2c5509c76352a59e0729e0",
  "cid": "QmV1ff912dd9a3349b682a36dfd3ac71d415caad6f13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290589,
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
      "evaluated_at": 1760290589
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
  "sig": "700ceeeb92a8ca7ce6171f16a1e263ed2a5f11b6c9863eea4198d95d81eb4bdc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155376461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 154, 'threshold': 50, 'total_amount': 46337214, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 153, 'first_seen': 1760285765, 'matching_hash': 'ed3a1cd9da35e724'}}}