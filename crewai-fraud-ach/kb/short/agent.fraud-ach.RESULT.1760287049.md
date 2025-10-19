```json
{
  "id": "fd04165935126213",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287049,
  "host_pid": "9e6742732c60:1",
  "hash": "89ad7535d62a18a8bee6ccabaf87181cbbba85165dafb72f997a3d8374e88ab3",
  "cid": "QmV189ad7535d62a18a8bee6ccabaf87181cbbba8516",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287049,
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
      "evaluated_at": 1760287049
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "599211163124381d0828118bf789b4f61df93659994c036f15e06ccb57e9a915"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000033181833
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 17206070, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 45, 'first_seen': 1760285765, 'matching_hash': '52cd22d87934f676'}}}