```json
{
  "id": "b9000bd93b73629b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287794,
  "host_pid": "9e6742732c60:1",
  "hash": "39809dc777ebcc6e0cd02f1c863ea750a69555e1bb25fd45466d8b08b2b7776c",
  "cid": "QmV139809dc777ebcc6e0cd02f1c863ea750a69555e1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287794,
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
      "evaluated_at": 1760287794
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
  "sig": "8f9c84f8046d3a13734dec4821f946233b815563c728405599a3d52778b9a193"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 22913856, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}