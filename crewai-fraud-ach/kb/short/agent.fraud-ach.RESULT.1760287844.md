```json
{
  "id": "614ba55add2bb412",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287844,
  "host_pid": "9e6742732c60:1",
  "hash": "66d2c8fed2f5e767b98da2ee5a3449f94864bcd8eec854ad164da7a7bbd1a56c",
  "cid": "QmV166d2c8fed2f5e767b98da2ee5a3449f94864bcd8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287844,
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
      "evaluated_at": 1760287844
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
  "sig": "a67168a1aaa04c3460cf4b0f30b3899d32b73091552a3b13f9125f9bd228fbe6"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 021000021395098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 26701124, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285765, 'matching_hash': '9c6ceec1730a6176'}}}