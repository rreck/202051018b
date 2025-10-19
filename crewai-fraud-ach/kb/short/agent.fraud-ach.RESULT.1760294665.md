```json
{
  "id": "4db2fb8a43f369e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294665,
  "host_pid": "9e6742732c60:1",
  "hash": "ffb8d20e710e5223728a4e43088f2f09c9c1b925c914bd2fafadc9f1e8ff8f1d",
  "cid": "QmV1ffb8d20e710e5223728a4e43088f2f09c9c1b925",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294665,
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
      "evaluated_at": 1760294665
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
  "sig": "da16909ab2648529068d6e33cd792f2924b3f6c2e7865407ae6d44ccc5b14dc6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599876575
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 75554336, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285764, 'matching_hash': '0131e24faef32fc6'}}}