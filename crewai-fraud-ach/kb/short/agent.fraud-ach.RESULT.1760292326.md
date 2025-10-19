```json
{
  "id": "b22b5e05fbc7a2c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292326,
  "host_pid": "9e6742732c60:1",
  "hash": "ed663073702d44ac5a7a08e05815b3c9fa60944959ac392cc5e7757a3cea23e9",
  "cid": "QmV1ed663073702d44ac5a7a08e05815b3c9fa609449",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292326,
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
      "evaluated_at": 1760292326
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
  "sig": "b645e55c27ac9a6132536a911277379230a5a89d756513dbab6c287a788c2e0d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151200756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 31710705, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': 'e0249734267f8906'}}}