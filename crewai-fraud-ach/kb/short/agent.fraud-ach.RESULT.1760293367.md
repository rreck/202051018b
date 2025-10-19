```json
{
  "id": "7dd846fdcbea847b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293367,
  "host_pid": "9e6742732c60:1",
  "hash": "a207c660a019cb56552efcd86298458d51bcb77587ce09c55f75f8b32f85f7ab",
  "cid": "QmV1a207c660a019cb56552efcd86298458d51bcb775",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293367,
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
      "evaluated_at": 1760293367
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
  "sig": "df707c983d3c2580ad1c55efe540db9f70dedca391d9d828d4c9e310e80021f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246406835
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 50643677, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285764, 'matching_hash': '1c7c2a17ea2f241c'}}}