```json
{
  "id": "f483616a7e851b31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289274,
  "host_pid": "9e6742732c60:1",
  "hash": "ded56923d27f0df9465dd508c7fe9a70034db7d3428a6a9321f3def6561c08a8",
  "cid": "QmV1ded56923d27f0df9465dd508c7fe9a70034db7d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289274,
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
      "evaluated_at": 1760289274
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
  "sig": "0d18e9ebed90e87fa8e4cb45a3d71d480161caac54c09ef906593ea7492f8fd1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 37553264, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}