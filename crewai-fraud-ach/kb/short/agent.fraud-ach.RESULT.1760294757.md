```json
{
  "id": "0b8f298cd489e65b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294757,
  "host_pid": "9e6742732c60:1",
  "hash": "4c86fd5496768cad498ab7615270cb9ec3219072ce87f2a7e4661cbcdbea1c83",
  "cid": "QmV14c86fd5496768cad498ab7615270cb9ec3219072",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294757,
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
      "evaluated_at": 1760294757
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
  "sig": "17d75946745b6b9d04e16f6ac62cf9a82eb4ab23d25c678d25e08b59be080000"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271403003
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 61000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': 'a8be718158b742cd'}}}