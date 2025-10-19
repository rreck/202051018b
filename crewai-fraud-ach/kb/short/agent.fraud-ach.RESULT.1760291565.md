```json
{
  "id": "25e21bd65d127f87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291565,
  "host_pid": "9e6742732c60:1",
  "hash": "82406f2b6079345202afa866d78ca174bfd1c8e935016a73643774f72404961f",
  "cid": "QmV182406f2b6079345202afa866d78ca174bfd1c8e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291565,
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
      "evaluated_at": 1760291565
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
  "sig": "c62e38d1dee2c0882002745c3143b24ab5ac7dea270df3c54e4b6ca1ed21a656"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025664709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 18324566, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285764, 'matching_hash': '5cc83e27ca9ca801'}}}