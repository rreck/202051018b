```json
{
  "id": "f29ea9cae6e97cc4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288931,
  "host_pid": "9e6742732c60:1",
  "hash": "9ce1fa462a70b9d44f9ca7303affb0911832f1a947c51046fd412bad03177bd2",
  "cid": "QmV19ce1fa462a70b9d44f9ca7303affb0911832f1a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288931,
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
      "evaluated_at": 1760288931
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
  "sig": "3e327da363ae13e60e4f725a25ed859714ecb8093d53cb46e16290f2dda3e29e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025883497
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 34344432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285765, 'matching_hash': '8c29ee71720a2634'}}}