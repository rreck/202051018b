```json
{
  "id": "93b7881fe263349c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291270,
  "host_pid": "9e6742732c60:1",
  "hash": "c7b788f40118b22c6ac3243131568ec87be871301cb8f7f1b693fb331e87deb2",
  "cid": "QmV1c7b788f40118b22c6ac3243131568ec87be87130",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291270,
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
      "evaluated_at": 1760291270
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
  "sig": "2529053851dc144aeddedc71042d77a00a861570c4418d7fb84047d852337340"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000020947870
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 11538054, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': '1f43c37f0aae1875'}}}