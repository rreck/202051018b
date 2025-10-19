```json
{
  "id": "8175f2a32d6e909f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288472,
  "host_pid": "9e6742732c60:1",
  "hash": "854804c9b1534df7f89e8b9a78bb8c2b872010a53c30906abd8d02a3ea0a5e02",
  "cid": "QmV1854804c9b1534df7f89e8b9a78bb8c2b872010a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288472,
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
      "evaluated_at": 1760288472
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
  "sig": "5b853a0295d154fdc133e086ea5df868f50acc58c204f2504c9dc5a241c5f0c8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248581748
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 17971578, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285765, 'matching_hash': '6ba0c7e0a23e9d51'}}}