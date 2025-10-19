```json
{
  "id": "ba92922d4979d719",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294828,
  "host_pid": "9e6742732c60:1",
  "hash": "4dffdf6682efb0803bfa171848ac2113567eade923ae50bcfbceec3890145c23",
  "cid": "QmV14dffdf6682efb0803bfa171848ac2113567eade9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294828,
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
      "evaluated_at": 1760294828
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
  "sig": "5e0c0090083ffec4d81826bf3565c1df69294eb593f145ae28c85a87b6cc90af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030595065
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 74448395, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '3889a0f66c8870f8'}}}}