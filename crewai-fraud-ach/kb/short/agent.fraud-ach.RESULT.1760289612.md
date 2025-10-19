```json
{
  "id": "4f19a93d4862ebed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289612,
  "host_pid": "9e6742732c60:1",
  "hash": "df6f71ba471bcfc467361abf6ce386cb750f7fe798772e8e83d3c7c3de59df35",
  "cid": "QmV1df6f71ba471bcfc467361abf6ce386cb750f7fe7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289612,
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
      "evaluated_at": 1760289612
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
  "sig": "9919155f4f4f24a89e71ab7bbe5fc9d44b84f538866668ecab8e5b3d229acca8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246662267
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 54562432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': '95edcdc5f9712ce3'}}}