```json
{
  "id": "49219c3092f508f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293392,
  "host_pid": "9e6742732c60:1",
  "hash": "604bb9e52e8b3bd8232fc8c2a7f038d1d825ba53472284144836826b0d0d2ee4",
  "cid": "QmV1604bb9e52e8b3bd8232fc8c2a7f038d1d825ba53",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293392,
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
      "evaluated_at": 1760293392
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
  "sig": "454f9c1f8af0e9c51f07606bb26ee8f91858dfff893f478f14e5239fb54c2212"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 69059816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}