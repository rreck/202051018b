```json
{
  "id": "020eeb856863876f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294253,
  "host_pid": "9e6742732c60:1",
  "hash": "d3f7d56f2b64698c3cc66725553b09a677f870ed947528ab69980270b88d51ef",
  "cid": "QmV1d3f7d56f2b64698c3cc66725553b09a677f870ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294253,
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
      "evaluated_at": 1760294253
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
  "sig": "eb394b633727ae13d41cbbf444a00e4ed2c529770535c30d63f5f4b6affd2da0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243232456
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 78100776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285765, 'matching_hash': '1b0a7dc1f650d378'}}}