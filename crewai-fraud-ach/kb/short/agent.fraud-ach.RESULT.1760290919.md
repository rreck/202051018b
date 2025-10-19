```json
{
  "id": "a536020a7a894290",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290919,
  "host_pid": "9e6742732c60:1",
  "hash": "c3ec62ccffa8e760caa1dce79ad581fca0a5276a5d50ef5598f1e72cfa89ae53",
  "cid": "QmV1c3ec62ccffa8e760caa1dce79ad581fca0a5276a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290919,
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
      "evaluated_at": 1760290919
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
  "sig": "a7378ff4e121c4c9e98c2aea0f42ae8a0e5e5248989f7caa2ed71a15b1f6950f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275178719
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 26894754, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285765, 'matching_hash': '267c9e50b53a1b99'}}}