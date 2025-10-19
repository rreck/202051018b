```json
{
  "id": "0e7f13d9404ff0dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292860,
  "host_pid": "9e6742732c60:1",
  "hash": "cbdfe1cadecb5590632d919ddef11ccf56faa6ce1d1a9125edaa1eae36bfcc2a",
  "cid": "QmV1cbdfe1cadecb5590632d919ddef11ccf56faa6ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292860,
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
      "evaluated_at": 1760292860
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
  "sig": "68c504a228ab736dab29cdc5043c11cea5aa9d115b856cb48ab691e3366780b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156006729
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 10477778, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285765, 'matching_hash': 'e8898c854a66ef00'}}}