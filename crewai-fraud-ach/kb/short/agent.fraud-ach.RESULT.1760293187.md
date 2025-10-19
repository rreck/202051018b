```json
{
  "id": "943ee1f9fd060fdb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293187,
  "host_pid": "9e6742732c60:1",
  "hash": "b14ee9726db2867d86b2eedd6142937e67f48c2dd4234020813e9b927323a7ed",
  "cid": "QmV1b14ee9726db2867d86b2eedd6142937e67f48c2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293187,
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
      "evaluated_at": 1760293187
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
  "sig": "afeefd9dd1572d34ed7f3931a3f0903c3711efab3bd30dbffbe14ff4913ba114"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245329334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 78550566, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285765, 'matching_hash': 'de3fbc58a94e529a'}}}