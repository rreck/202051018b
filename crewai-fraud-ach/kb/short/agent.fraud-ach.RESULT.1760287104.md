```json
{
  "id": "bd8679fb82143db3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287104,
  "host_pid": "9e6742732c60:1",
  "hash": "170d81e6498f48bb6fbf9154219af43002703bfbf1759e9e1ce318febee8f8d9",
  "cid": "QmV1170d81e6498f48bb6fbf9154219af43002703bfb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287104,
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
      "evaluated_at": 1760287104
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
  "sig": "6957e3cb7f78f1c4353162610d14c552f8685dc61cc693eeb1436a80ff3dac6d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000243187094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21522960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285764, 'matching_hash': '46900333a68fa7ba'}}}