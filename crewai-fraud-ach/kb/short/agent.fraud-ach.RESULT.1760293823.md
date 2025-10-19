```json
{
  "id": "f251b8cc91a0b878",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293823,
  "host_pid": "9e6742732c60:1",
  "hash": "ed04757b3ffb9dad6c2dc4653365b1602c2ad68a6ac88edeab3a7cf21b307592",
  "cid": "QmV1ed04757b3ffb9dad6c2dc4653365b1602c2ad68a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293823,
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
      "evaluated_at": 1760293824
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
  "sig": "3cb7c65d7fe1084e12bc2b5f4ba62026d64688bb1ee3fbd9e41383edad3a1249"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030656036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 302, 'threshold': 50, 'total_amount': 85937422, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 301, 'first_seen': 1760284979, 'matching_hash': '54d3add09935598e'}}}