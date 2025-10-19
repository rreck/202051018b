```json
{
  "id": "886f3c685dbec25d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288695,
  "host_pid": "9e6742732c60:1",
  "hash": "c910f9550f42ea7cdcded6879fc701db8fb0241c3bce2db107ce6add00cc5a4b",
  "cid": "QmV1c910f9550f42ea7cdcded6879fc701db8fb0241c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288695,
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
      "evaluated_at": 1760288695
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
  "sig": "c65c3473de43e87582e1f42e98ff4ea12a2e29c8ea51f3de7cd8e2b38d8cf7b5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036830266
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285765, 'matching_hash': '1bf0c396f41926f3'}}}een': 1760285763, 'matching_hash': 'b88361d419e7152d'}}}