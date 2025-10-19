```json
{
  "id": "423bf152cf24d12f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293053,
  "host_pid": "9e6742732c60:1",
  "hash": "c0b960dbeb7d62f1ec1430e9bb74e46cea7462d10c65a607b78a568efe4dc17f",
  "cid": "QmV1c0b960dbeb7d62f1ec1430e9bb74e46cea7462d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293053,
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
      "evaluated_at": 1760293053
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
  "sig": "2110d6e5ecd13e37cc1b134acc84a223c95e34b4ec1f8b92b7c4b5b501e5f217"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 66832080, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}