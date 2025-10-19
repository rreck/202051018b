```json
{
  "id": "700c4269fc91b078",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289729,
  "host_pid": "9e6742732c60:1",
  "hash": "953a699ee8cbf0cc5eaf4d1dcb65a5de081611ac1a295da8da8d5d6c17b69fe9",
  "cid": "QmV1953a699ee8cbf0cc5eaf4d1dcb65a5de081611ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289729,
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
      "evaluated_at": 1760289729
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
  "sig": "4fbae50ea24a25d3a71172990744a2d110e543f9bdeeffe12838941c77a5e4c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 131, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 130, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}