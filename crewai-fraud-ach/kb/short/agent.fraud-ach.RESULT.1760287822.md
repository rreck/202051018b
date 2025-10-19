```json
{
  "id": "c3c6522f69419e36",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287822,
  "host_pid": "9e6742732c60:1",
  "hash": "a5d7e661fb5d94cfd03cb0b7837d29f061322ddd76634708055aef0924dea81d",
  "cid": "QmV1a5d7e661fb5d94cfd03cb0b7837d29f061322ddd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287822,
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
      "evaluated_at": 1760287822
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
  "sig": "60ad8ddd957aede0facb6890010dd65efac862bb0fe382c4c2ca2e065191bb8a"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 044000035430994
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 31010400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285765, 'matching_hash': '24f97a880bb92d0e'}}}