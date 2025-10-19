```json
{
  "id": "a4f8a46f004a67f1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286212,
  "host_pid": "9e6742732c60:1",
  "hash": "369ea80ade190756566334c91729fda8f0d261d2d9ede3e01c03abf7a18a81a4",
  "cid": "QmV1369ea80ade190756566334c91729fda8f0d261d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286212,
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
      "evaluated_at": 1760286212
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
  "sig": "d046c5d15dd0abc470ca8c1de8825f2e8099e4cbbb9428152368e92db6292dc1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000248764263
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': '9f14c95be52dc67f'}}}, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': '38dcdd2f540d89c1'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}