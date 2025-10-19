```json
{
  "id": "65ac8decb3cf053e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290002,
  "host_pid": "9e6742732c60:1",
  "hash": "125aa938c0b5c52d623bbab2eec6a18d9390ffe6726f5d99574d8866c0129529",
  "cid": "QmV1125aa938c0b5c52d623bbab2eec6a18d9390ffe6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290002,
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
      "evaluated_at": 1760290002
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
  "sig": "703bfd0719f07e99f7668e93cd36fb0ae88c0af1adcec9274124acc95516d87c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033242654
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 44306250, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': '1355ad48790eb31b'}}}