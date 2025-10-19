```json
{
  "id": "39bb3194542ea0b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291794,
  "host_pid": "9e6742732c60:1",
  "hash": "db73cb67296c2598ca9509f5b66b75f0e5eed7c48c1ceeb310b5da422efda30a",
  "cid": "QmV1db73cb67296c2598ca9509f5b66b75f0e5eed7c4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291794,
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
      "evaluated_at": 1760291794
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
  "sig": "6344817506974bd8339cbd5b0642830bbf5b49b43614ce254b888281dea3491a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030798175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 259, 'threshold': 50, 'total_amount': 30844828, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 258, 'first_seen': 1760284979, 'matching_hash': 'fdbb68f6e232305a'}}}