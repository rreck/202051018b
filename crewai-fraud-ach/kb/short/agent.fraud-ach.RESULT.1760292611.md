```json
{
  "id": "66e9172f5c2b3a38",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292611,
  "host_pid": "9e6742732c60:1",
  "hash": "b9fdc5f16652e6dc37049da1f70a982eefa54b1ac98dc21d15225f527093ee26",
  "cid": "QmV1b9fdc5f16652e6dc37049da1f70a982eefa54b1a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292611,
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
      "evaluated_at": 1760292611
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
  "sig": "0fe83a6f45ef019f0712dca8a73c3aa16558a92c9319a11b7df204bcea9768af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240116635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 76342413, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': 'faa8e9f78afe3726'}}}