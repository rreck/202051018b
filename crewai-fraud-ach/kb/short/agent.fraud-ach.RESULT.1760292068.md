```json
{
  "id": "cc367a764a9354b2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292068,
  "host_pid": "9e6742732c60:1",
  "hash": "6070549ae8b2317d701956f4a59bf2bdc3c929dc1c56bfb09a215241d950c2c4",
  "cid": "QmV16070549ae8b2317d701956f4a59bf2bdc3c929dc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292068,
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
      "evaluated_at": 1760292068
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
  "sig": "a2fe47b772229bacaf288f11dc62133b047e461e0cb5263ef01ec33defa6091b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026828395
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 15614802, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285765, 'matching_hash': '40ce51f53058bb71'}}}