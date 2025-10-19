```json
{
  "id": "52e80b552abd076a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288439,
  "host_pid": "9e6742732c60:1",
  "hash": "f13f9c9ea3241605d92871a587406dd29ffd2959b2450056bc8321e7bfc795fe",
  "cid": "QmV1f13f9c9ea3241605d92871a587406dd29ffd2959",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288439,
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
      "evaluated_at": 1760288439
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
  "sig": "54a4d9646465cb9f922e24d67322d03ce517a83ee6324ca265f1f93da22f256c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590909791
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285765, 'matching_hash': 'dd7dbd0f0c1d6f0c'}}}