```json
{
  "id": "b5b5c162eeb48117",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293500,
  "host_pid": "9e6742732c60:1",
  "hash": "ec31fba10f709a0247ce29671d918be926d07b5c9a1a5c1ecc34ef608f67a5bd",
  "cid": "QmV1ec31fba10f709a0247ce29671d918be926d07b5c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293500,
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
      "evaluated_at": 1760293500
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
  "sig": "8f8601aebe268977f39be139fd1f5fa4e5417b755e34f16da5304b7a300f31b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026803563
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 55189640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': 'cf30c88fa01e3081'}}}