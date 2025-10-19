```json
{
  "id": "f26bb41a9cd98a4e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288634,
  "host_pid": "9e6742732c60:1",
  "hash": "eaa1629cb7427fb1b7b0d94c2ed75f8c6aa8dcee22d34e8290d65a83c369fa44",
  "cid": "QmV1eaa1629cb7427fb1b7b0d94c2ed75f8c6aa8dcee",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288634,
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
      "evaluated_at": 1760288634
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
  "sig": "e8f530fdc17f490bc95456e8cd80a83c0f6494b12744a78ad268e0952af5170e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596862432
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 20201544, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285764, 'matching_hash': 'ec6d2f2d96a1a77c'}}}