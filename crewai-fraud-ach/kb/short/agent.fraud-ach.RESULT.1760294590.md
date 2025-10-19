```json
{
  "id": "5ce9fd995e47a7db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294590,
  "host_pid": "9e6742732c60:1",
  "hash": "72cb1116c9d7d2ef6d90c7d206a798be9fa254600bc1748bfe4675fd32c89001",
  "cid": "QmV172cb1116c9d7d2ef6d90c7d206a798be9fa25460",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294590,
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
      "evaluated_at": 1760294590
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
  "sig": "90f36cf9eb8f4f1cfb95e89d69369cafaa46e9f5af94cc1366debb40b3231fda"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272419137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 62294162, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': '38281b9a763b4bf2'}}}