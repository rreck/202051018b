```json
{
  "id": "33e27c27e7fb1f8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293995,
  "host_pid": "9e6742732c60:1",
  "hash": "9d8840453ef2cbbbf1dd349c54ca1ac249ba6ef69709fbe6c3057c4d852cd5a2",
  "cid": "QmV19d8840453ef2cbbbf1dd349c54ca1ac249ba6ef6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293995,
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
      "evaluated_at": 1760293995
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
  "sig": "a735b2a4b6fa7c8e8b73ed07795c0e584760ee81170a2f5aa1b69dc6c68bf544"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027607406
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 25371139, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285765, 'matching_hash': '504131d6dff02852'}}}