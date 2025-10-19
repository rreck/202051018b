```json
{
  "id": "adcad7204ec9c88a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289295,
  "host_pid": "9e6742732c60:1",
  "hash": "79b6f79781981a07dbcf4eea9d30a08e05057a759285deccc450ff02b2593ea8",
  "cid": "QmV179b6f79781981a07dbcf4eea9d30a08e05057a75",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289295,
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
      "evaluated_at": 1760289295
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
  "sig": "ac3ec74a5443bcce8f9744747eeced07cd4840a34f0c3d4e5ca947335abd77b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022625380
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 43041229, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285763, 'matching_hash': 'f6638b44b9180b42'}}}