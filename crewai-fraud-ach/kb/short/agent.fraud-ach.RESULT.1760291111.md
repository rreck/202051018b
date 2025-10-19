```json
{
  "id": "8ad5f64c79787ffb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291111,
  "host_pid": "9e6742732c60:1",
  "hash": "a9b6c19384699993aaf4aac85f1e288d104e0826f659d6a73cc8b36a22dccdd3",
  "cid": "QmV1a9b6c19384699993aaf4aac85f1e288d104e0826",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291111,
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
      "evaluated_at": 1760291111
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
  "sig": "6f5346a2df72ae042c14071fdde2efd4fc5a0c166d5f6464e33250930c10573f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024460145
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 42352369, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': '6128e7e8f1f7694a'}}}}