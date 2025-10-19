```json
{
  "id": "ede5f654cb343f9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293064,
  "host_pid": "9e6742732c60:1",
  "hash": "ccf60e42e0f1824d47a1f070756203b0dcc99f6ce40988ad2c2bf92c6df07334",
  "cid": "QmV1ccf60e42e0f1824d47a1f070756203b0dcc99f6c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293064,
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
      "evaluated_at": 1760293064
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
  "sig": "afc17dc398e6e01f4a5c87a8b6e4b99f6f3c846830a3953f8e3cfc08179fb9ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272156319
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 16222524, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': '6d26908715188c7a'}}}