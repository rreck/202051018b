```json
{
  "id": "e764dc2d83d014cd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289874,
  "host_pid": "9e6742732c60:1",
  "hash": "6b4db2f72e82bd59d64a6cba37598e6b35acb57985592408ff761f27ac44bd9f",
  "cid": "QmV16b4db2f72e82bd59d64a6cba37598e6b35acb579",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289874,
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
      "evaluated_at": 1760289874
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
  "sig": "c8da43fbc081415a33c12e27c79d87dbb5feaed4810a3d50f927e79eb89340c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026725963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 27250830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285765, 'matching_hash': '729970816697b41b'}}}