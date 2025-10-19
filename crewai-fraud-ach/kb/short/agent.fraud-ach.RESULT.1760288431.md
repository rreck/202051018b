```json
{
  "id": "77e04ccfde3200de",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288431,
  "host_pid": "9e6742732c60:1",
  "hash": "06293a4201c2ad14390d9d60b58646530f7e519ee1ac3499879ed964ba05ae45",
  "cid": "QmV106293a4201c2ad14390d9d60b58646530f7e519e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288431,
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
      "evaluated_at": 1760288431
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
  "sig": "0b1f13db02136cf08727016fdfc746a1ce2e829ad5a36ab5962a958fe25cdf41"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592035169
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 79834079, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760284979, 'matching_hash': 'af51af40be20c608'}}}