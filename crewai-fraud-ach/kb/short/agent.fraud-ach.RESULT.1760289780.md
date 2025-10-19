```json
{
  "id": "68ea6e4e935ca6c9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289780,
  "host_pid": "9e6742732c60:1",
  "hash": "374514975d546a3eebf5342ed754bf0ec98d9e396796e1485de37ae7b94f5f85",
  "cid": "QmV1374514975d546a3eebf5342ed754bf0ec98d9e39",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289780,
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
      "evaluated_at": 1760289780
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
  "sig": "5f2cebbac60f23fe64a4b37bfa1d7ca25b7c56302ef49f736b70a1d26ccb09e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590117216
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 12255950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': '88179e7e1f8b79c4'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}