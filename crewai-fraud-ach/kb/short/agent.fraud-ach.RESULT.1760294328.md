```json
{
  "id": "02c6520e32110a9c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294328,
  "host_pid": "9e6742732c60:1",
  "hash": "be4138aab043dc3c63dd076a08c32773e33a7c334fcbebb6c02e4a14e5564b4f",
  "cid": "QmV1be4138aab043dc3c63dd076a08c32773e33a7c33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294328,
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
      "evaluated_at": 1760294328
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
  "sig": "c77595048fa313a6993c23604ee54882addfc66f26351b85acb166dd70a7ffff"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028841300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 44116660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'f5bed59f6c250fae'}}}