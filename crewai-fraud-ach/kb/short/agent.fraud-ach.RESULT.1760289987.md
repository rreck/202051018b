```json
{
  "id": "5544804632b22256",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289987,
  "host_pid": "9e6742732c60:1",
  "hash": "40919a013ec204eda071fe73414c972b471abad4d8687d9434ccd88d54e75325",
  "cid": "QmV140919a013ec204eda071fe73414c972b471abad4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289987,
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
      "evaluated_at": 1760289987
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
  "sig": "3933270f3afb02fe382a728be71adc76517772688c48fcb21f1fabd89a085eb3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274979410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285765, 'matching_hash': '00a04409f00be8e6'}}}