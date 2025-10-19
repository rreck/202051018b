```json
{
  "id": "0f3129c43d57cd8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287392,
  "host_pid": "9e6742732c60:1",
  "hash": "17ca9dc09de042f13b4c114ba5d02fff624d3cede161f4067224a7faf0973fda",
  "cid": "QmV117ca9dc09de042f13b4c114ba5d02fff624d3ced",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287392,
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
      "evaluated_at": 1760287392
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
  "sig": "f60ac236d42183c449ea26d43718eea8cd8388a81bb32ea3c6a59c1e6f239298"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 18458384, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}