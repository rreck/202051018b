```json
{
  "id": "11de42f373906845",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291806,
  "host_pid": "9e6742732c60:1",
  "hash": "f8b47d60c07245cee20acea869c4f20c7e9c88b84a4307355ab4b930f2b76312",
  "cid": "QmV1f8b47d60c07245cee20acea869c4f20c7e9c88b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291806,
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
      "evaluated_at": 1760291806
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
  "sig": "2a2f4bf6f41fc5009a0631b7e807c8df0b98a5d873eb0165366fedd9817dd7f2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592096226
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 90332826, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285765, 'matching_hash': '5e92eb8585c87013'}}}