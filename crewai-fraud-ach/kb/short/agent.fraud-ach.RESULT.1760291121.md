```json
{
  "id": "805e4a4c4e2a6f14",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291121,
  "host_pid": "9e6742732c60:1",
  "hash": "05d4af3ad05e2dde18c41c39d43247791be896d6d3d8f724be11560c28b3cfb4",
  "cid": "QmV105d4af3ad05e2dde18c41c39d43247791be896d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291121,
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
      "evaluated_at": 1760291121
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
  "sig": "5cfc08c715689c35ce82a20029632001fcf13abb3ba98a795c071537048e5fbb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597421131
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 38971287, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285765, 'matching_hash': 'ee859bd02c19b1f0'}}}