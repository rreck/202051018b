```json
{
  "id": "f1019ef914056497",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289066,
  "host_pid": "9e6742732c60:1",
  "hash": "d4fb7278763c3ce66d8b0f342a0fa2210a808b4f0ce5889d79a24d0e28b12035",
  "cid": "QmV1d4fb7278763c3ce66d8b0f342a0fa2210a808b4f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289066,
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
      "evaluated_at": 1760289066
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
  "sig": "f480956035addc966417aaa05530122a3d741813911e51bfe8596f5af13c6fd3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}