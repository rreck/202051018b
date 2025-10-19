```json
{
  "id": "3c69b62043da9af0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292251,
  "host_pid": "9e6742732c60:1",
  "hash": "0840d1b8cae95ea855910b3f20f039795d255545fa50457d116f73691f3f7bae",
  "cid": "QmV10840d1b8cae95ea855910b3f20f039795d255545",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292251,
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
      "evaluated_at": 1760292251
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "1d727193cd203af3cff2e38a24dc23c47441dfb7be7311347c249258a1cf2028"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 635242948975660
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 193, 'threshold': 50, 'total_amount': 82934416, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 192, 'first_seen': 1760285765, 'matching_hash': '596a6d950333709b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '635242942', 'validation_error': 'Invalid routing number checksum'}}}