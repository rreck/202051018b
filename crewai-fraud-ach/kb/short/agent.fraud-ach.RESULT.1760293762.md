```json
{
  "id": "84d24c321d8299a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293762,
  "host_pid": "9e6742732c60:1",
  "hash": "eb199c15ee1b18d80ded5899f53331402367e694030ba79b494f9f9a422309f3",
  "cid": "QmV1eb199c15ee1b18d80ded5899f53331402367e694",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293762,
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
      "evaluated_at": 1760293762
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
  "sig": "6e42225a35632eaf55aee2ff5aeb49ab78527186c8980e09917bac30db6256e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461386979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 76421475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285764, 'matching_hash': '1569de4be841c048'}}}