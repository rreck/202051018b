```json
{
  "id": "853f0c6b2ba4bd76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288311,
  "host_pid": "9e6742732c60:1",
  "hash": "0ebbe12d2f906fff634893cf02b3af53bc0bab934e53194c7b1cdd0776decaa3",
  "cid": "QmV10ebbe12d2f906fff634893cf02b3af53bc0bab93",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288311,
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
      "evaluated_at": 1760288311
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
  "sig": "e60d1317327279e1d8402b2d3495d00c3db84fec79763c7cf20e65522eb32c2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154024479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 89, 'threshold': 50, 'total_amount': 28382189, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 88, 'first_seen': 1760285765, 'matching_hash': 'af946edf21c4a5d6'}}}