```json
{
  "id": "e8a755249b2afd78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290088,
  "host_pid": "9e6742732c60:1",
  "hash": "5a340db05b62bf0df7a5c437881517895479348fa891660ecb007221b8674bb8",
  "cid": "QmV15a340db05b62bf0df7a5c437881517895479348f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290088,
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
      "evaluated_at": 1760290088
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
  "sig": "8202080b1b65823fc2e8e6c8d7cb2a2430c5987e13b5e6296b5799eb021ff308"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154224764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 34049385, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': '73218c90107a537b'}}}