```json
{
  "id": "11c99986321b7f98",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288981,
  "host_pid": "9e6742732c60:1",
  "hash": "e09b0ec1553f06498269acf9ba19203b309f45ab68934dfe46f236682e6e8747",
  "cid": "QmV1e09b0ec1553f06498269acf9ba19203b309f45ab",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288981,
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
      "evaluated_at": 1760288981
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
  "sig": "5a9227f885a5a96fe6bec24f22735a7b0bec145b37901426a6e8bb46df917a94"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022696777
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 53579020, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285763, 'matching_hash': 'bb01014ea9b32f36'}}}