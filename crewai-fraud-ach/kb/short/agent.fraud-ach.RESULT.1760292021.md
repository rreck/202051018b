```json
{
  "id": "00b15d662b1660a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292021,
  "host_pid": "9e6742732c60:1",
  "hash": "4ea78981e3e9e49289bca896af6858a024f49de6f3a0e352e42374b75a747199",
  "cid": "QmV14ea78981e3e9e49289bca896af6858a024f49de6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292021,
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
      "evaluated_at": 1760292021
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
  "sig": "51456ca7fb9a5cce911248b12ed6f961f7969ee7617a3e6408b68a42d4f96198"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596502557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 20425072, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285764, 'matching_hash': 'c368684e8d9c7f24'}}}