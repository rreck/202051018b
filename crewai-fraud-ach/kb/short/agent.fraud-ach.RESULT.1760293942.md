```json
{
  "id": "a5250debf39d775e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293942,
  "host_pid": "9e6742732c60:1",
  "hash": "01e7449a42519a790328beb4dd6082d7ab96ae8418526b0be1cd05c5a0b1b689",
  "cid": "QmV101e7449a42519a790328beb4dd6082d7ab96ae84",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293942,
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
      "evaluated_at": 1760293942
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
  "sig": "52338f24841a11e6a26402f53f7af23d46a6aeaa2d904d3ad2a6dab2d1f44134"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275925775
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 44177964, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285765, 'matching_hash': 'faef3b4bfd0d33cd'}}}