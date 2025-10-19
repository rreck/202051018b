```json
{
  "id": "0de15dcf5278dfaa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287271,
  "host_pid": "9e6742732c60:1",
  "hash": "afbaa334420fb7824dec5aea3d8d8320fe5bc95c706d20f10e5e4b23e63671de",
  "cid": "QmV1afbaa334420fb7824dec5aea3d8d8320fe5bc95c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287271,
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
      "evaluated_at": 1760287271
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
  "sig": "9882d9fe10cf78d2de2c10436078610406afe886e4e380a5d99c0ad4270e0c5f"
}
```

Fraud detected: duplicate_transaction (score: 71)
Transaction: 122105153385568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 58, 'details': {'transaction_count': 54, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 53, 'first_seen': 1760285763, 'matching_hash': '556aff2bced704f0'}}}