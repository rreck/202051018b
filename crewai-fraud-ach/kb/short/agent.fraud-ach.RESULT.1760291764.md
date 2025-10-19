```json
{
  "id": "903cc5f5626d2cf8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291764,
  "host_pid": "9e6742732c60:1",
  "hash": "9b59abba11fddb2579fc0128537c4ebd70f77e56fb303c39dc95b40edbe9cd04",
  "cid": "QmV19b59abba11fddb2579fc0128537c4ebd70f77e56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291764,
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
      "evaluated_at": 1760291764
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
  "sig": "54615390cfc0b65159e2b629228bc16f7686a4371b2340af252f2fb457479fe4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 57921136, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}