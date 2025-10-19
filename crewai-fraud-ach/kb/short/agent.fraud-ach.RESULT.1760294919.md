```json
{
  "id": "9823d6d4aba8b72b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294919,
  "host_pid": "9e6742732c60:1",
  "hash": "4c96f684db35f1f2aa286defa6b86d71318b711bc370c4ee5d267b317f88a3e8",
  "cid": "QmV14c96f684db35f1f2aa286defa6b86d71318b711b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294919,
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
      "evaluated_at": 1760294919
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
  "sig": "7fdfd41de5c59326827b9e55b6999b1d0fa73417114a4e4d0dadea38671778e8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592351032
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 247, 'threshold': 50, 'total_amount': 52082667, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 246, 'first_seen': 1760285763, 'matching_hash': '5f413645b746a025'}}}