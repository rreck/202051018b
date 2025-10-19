```json
{
  "id": "c553ec00cf170035",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291907,
  "host_pid": "9e6742732c60:1",
  "hash": "6e9f3cdf93d57f4661a1ae733332c642299f52ba8880bf0835038f0695a75e0f",
  "cid": "QmV16e9f3cdf93d57f4661a1ae733332c642299f52ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291907,
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
      "evaluated_at": 1760291907
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
  "sig": "130cf91102eb5bbc209f5b11fffaaa117b1194e240b8afdb351303784c822ff0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024511809
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 32612682, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285763, 'matching_hash': '174f6230f942e53f'}}}