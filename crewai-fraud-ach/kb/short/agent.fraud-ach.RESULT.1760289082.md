```json
{
  "id": "397d9311f3d6b50b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289082,
  "host_pid": "9e6742732c60:1",
  "hash": "ea4e0b724b94136b03cded134bdcfc2a75c2371d277a2bbe88f5cb21c47dc705",
  "cid": "QmV1ea4e0b724b94136b03cded134bdcfc2a75c2371d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289082,
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
      "evaluated_at": 1760289082
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
  "sig": "d9055470be712f6e763fcab151ce283eae9e39bb65964e583ffc091c44dd97eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469258561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 29350733, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285763, 'matching_hash': 'c5dbb685e09199e5'}}}