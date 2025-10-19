```json
{
  "id": "0f730ab19169e0a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291687,
  "host_pid": "9e6742732c60:1",
  "hash": "ed1b52acfd68e0c10ff66f6aab0948797b3de2e401c5af3efe4c28979f35c7d1",
  "cid": "QmV1ed1b52acfd68e0c10ff66f6aab0948797b3de2e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291687,
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
      "evaluated_at": 1760291687
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
  "sig": "6fcba04a399d55020eaae8b54088dba0937c3d41fa03c489955df48097add81a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275498951
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 181, 'threshold': 50, 'total_amount': 34423123, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 180, 'first_seen': 1760285763, 'matching_hash': 'a1e1622f9da312c5'}}}