```json
{
  "id": "96c47af6cadc82db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289927,
  "host_pid": "9e6742732c60:1",
  "hash": "1914f3f666377e6b27b385f060eaaab0212d82cb9efed64f7a134ce30132d96b",
  "cid": "QmV11914f3f666377e6b27b385f060eaaab0212d82cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289927,
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
      "evaluated_at": 1760289927
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
  "sig": "3d43ed7caffdd2837022ee3c68a09bf359adae7550c6750f397492a5ffb38a7b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468983209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 39104869, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': 'c1a39c32a70f5fe9'}}}