```json
{
  "id": "5c9c600aeea5c229",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292367,
  "host_pid": "9e6742732c60:1",
  "hash": "ac4a3ed34e0952a824466e29e51a35353e4563c3ba576efe48eb2f8a08bdf4f5",
  "cid": "QmV1ac4a3ed34e0952a824466e29e51a35353e4563c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292367,
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
      "evaluated_at": 1760292367
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
  "sig": "af43a68b212721a1c0372c7922a3106d424a3dff788667aef6374fa57c89d4e3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248879476
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 37288804, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '88da1f364f410d45'}}}