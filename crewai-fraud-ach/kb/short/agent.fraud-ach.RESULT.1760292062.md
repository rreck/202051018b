```json
{
  "id": "c7813501da23546e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292062,
  "host_pid": "9e6742732c60:1",
  "hash": "0cdd737da99a22237c94c0b42dea7a265cb8a55f9aebfae7d4c195cc74518d18",
  "cid": "QmV10cdd737da99a22237c94c0b42dea7a265cb8a55f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292062,
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
      "evaluated_at": 1760292062
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
  "sig": "8e43e62b136043816b5ed2ab75a1684d01564b82eaebdcf3e0834c9ffb57fa73"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025895266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 53657100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': '9ac81502eabc8fa5'}}}