```json
{
  "id": "0946ad3eb180f236",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294140,
  "host_pid": "9e6742732c60:1",
  "hash": "93afb9eddb97480d34b441f8f2ab3d80f1499f71b4c4390af534626c5a9ca895",
  "cid": "QmV193afb9eddb97480d34b441f8f2ab3d80f1499f71",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294140,
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
      "evaluated_at": 1760294140
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
  "sig": "92781dc4c660b8eb8aa55ac73fe10b5856328f705dcfdd2b56cba8bb2f86a004"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469927048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 69118136, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '982ed2d64f96a5b2'}}}