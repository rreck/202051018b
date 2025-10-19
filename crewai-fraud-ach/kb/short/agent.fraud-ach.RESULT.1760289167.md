```json
{
  "id": "b5d51a738fbff0e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289167,
  "host_pid": "9e6742732c60:1",
  "hash": "bf0e3134fa2c77cefe262118574e925ae18d18ea4c343242c60060be6f3fb64d",
  "cid": "QmV1bf0e3134fa2c77cefe262118574e925ae18d18ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289167,
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
      "evaluated_at": 1760289167
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
  "sig": "b840bed310b4bb90b2ea6ee4677359dfd59b97c231447a9feb92bf4feab18fa9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150676701
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 54137630, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285765, 'matching_hash': 'f947c72340b5e951'}}}