```json
{
  "id": "bbee37e25506ef5a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288094,
  "host_pid": "9e6742732c60:1",
  "hash": "9366df860d6f802d2b60b32cef8aaf2fec73326f3f94f7614fbb19a0576e3426",
  "cid": "QmV19366df860d6f802d2b60b32cef8aaf2fec73326f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288094,
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
      "evaluated_at": 1760288094
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
  "sig": "7a72bc89fb0672fc04e5a1e7716b0bcaae1768760f7fcdcd1a52ce67125c8b94"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467876303
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 35885988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285765, 'matching_hash': 'ffdb832f59bf640d'}}}