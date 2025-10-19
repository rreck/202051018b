```json
{
  "id": "e0b46dc4946ebd15",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293451,
  "host_pid": "9e6742732c60:1",
  "hash": "649d453e27e256618d83aa061654d7b6a7be2914ae57c7585b6963a5d8cdcd00",
  "cid": "QmV1649d453e27e256618d83aa061654d7b6a7be2914",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293451,
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
      "evaluated_at": 1760293451
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
  "sig": "4a7817b331b863c0a31b2ba6d9e337bafb38f2c7c3eab16524b9dfa69002f4a0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593273938
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 79779510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': '9925ef3004078e34'}}}