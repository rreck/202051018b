```json
{
  "id": "bdfd07c6d7f7b6bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294517,
  "host_pid": "9e6742732c60:1",
  "hash": "f84d72379e14892c57a7c0b41c6cdc2ac923bf7fcce8aea27a55da343d09ef64",
  "cid": "QmV1f84d72379e14892c57a7c0b41c6cdc2ac923bf7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294517,
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
      "evaluated_at": 1760294517
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
  "sig": "2829780f9e48c93302ecdedf4546d0060d1d7acb42891abb1f976d29f93a21b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279221197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 106718280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285765, 'matching_hash': '706f719d80b46657'}}}