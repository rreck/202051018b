```json
{
  "id": "032fca54279cdfda",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287935,
  "host_pid": "9e6742732c60:1",
  "hash": "ce65c97c64baccf2fde8f91752014017e2cb1eb5f8641989a410c6f50457141a",
  "cid": "QmV1ce65c97c64baccf2fde8f91752014017e2cb1eb5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287935,
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
      "evaluated_at": 1760287935
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
  "sig": "8d0a9cafb49f9308f90a1fc7b6e4ed56598bb003b52b7b84dbd41b737ab5045b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021748494
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285765, 'matching_hash': '2adbcd1f80c0d3e0'}}}