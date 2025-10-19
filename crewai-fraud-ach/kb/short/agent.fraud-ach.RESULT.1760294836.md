```json
{
  "id": "0c10348e9aa9b2bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294836,
  "host_pid": "9e6742732c60:1",
  "hash": "b80aab5f920e5a679e775233531e46064003d1d37a094265a8f80bfbd9d52b53",
  "cid": "QmV1b80aab5f920e5a679e775233531e46064003d1d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294836,
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
      "evaluated_at": 1760294836
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
  "sig": "b99331c68d057faba6980a2448e7812e712d362d0e25ec8d5ef2c8233239059a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027745016
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 117085745, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285765, 'matching_hash': '88a158c93e7cc45f'}}}