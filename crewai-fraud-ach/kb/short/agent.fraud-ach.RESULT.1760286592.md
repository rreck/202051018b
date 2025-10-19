```json
{
  "id": "931807d417841011",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286592,
  "host_pid": "9e6742732c60:1",
  "hash": "464b24bdf5fb2fb30a82547aac8741505903d4e59a9269a00d44274fdad901ff",
  "cid": "QmV1464b24bdf5fb2fb30a82547aac8741505903d4e5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286592,
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
      "evaluated_at": 1760286592
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
  "sig": "91b3ffff2df5a685b25f10b4f7bcfb9439e5b724447da84da636f1317d3bd21a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105159928324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 13190790, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285765, 'matching_hash': 'f9e49b53b0020755'}}}