```json
{
  "id": "d94371a9a075721b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292731,
  "host_pid": "9e6742732c60:1",
  "hash": "e8d5c3d9429d4a5a51028286541901ed279e968dc81f189b7fb36cf3af5c427e",
  "cid": "QmV1e8d5c3d9429d4a5a51028286541901ed279e968d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292731,
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
      "evaluated_at": 1760292731
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
  "sig": "e69107f572307d6c894c2565d867441e6a7b7fb0848a628a88d0036eae7a8041"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029877647
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 69596844, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': 'f76c4daf1b61ee5a'}}}