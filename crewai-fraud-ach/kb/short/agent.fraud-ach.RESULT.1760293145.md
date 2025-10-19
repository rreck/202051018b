```json
{
  "id": "c3361d76d32986c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293145,
  "host_pid": "9e6742732c60:1",
  "hash": "b0ddc17a966551f225cdfdb8d1876feedba937fdd4f178ff33098bae678f8162",
  "cid": "QmV1b0ddc17a966551f225cdfdb8d1876feedba937fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293145,
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
      "evaluated_at": 1760293145
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
  "sig": "25012d4b3e787b75a594e1e8e0fed51e6ddb4e7ef457bea13475e64926a0090c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 10600000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}