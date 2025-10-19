```json
{
  "id": "4dab98a4e1092d56",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293536,
  "host_pid": "9e6742732c60:1",
  "hash": "3788447ebbbabe84d5ebad67e78a471ec03b951201666eb969a172567a90998d",
  "cid": "QmV13788447ebbbabe84d5ebad67e78a471ec03b9512",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293536,
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
      "evaluated_at": 1760293536
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
  "sig": "650355fe63f6cbd35916623ef33b922663d8b62100b3dfe428e497aaa1ad020f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273742232
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 46381940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285765, 'matching_hash': '98264f1e6b5ab805'}}}