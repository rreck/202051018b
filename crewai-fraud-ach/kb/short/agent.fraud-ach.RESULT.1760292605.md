```json
{
  "id": "df1b6287209c25e5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292605,
  "host_pid": "9e6742732c60:1",
  "hash": "172370b7d46106fe94e9009d2ce20156ef1534fd01724798eb75be699b499bec",
  "cid": "QmV1172370b7d46106fe94e9009d2ce20156ef1534fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292605,
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
      "evaluated_at": 1760292605
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
  "sig": "da8abe90ba1f27086828e33d1e894006f117572cb11af2b6cbf59af6bd9b2e16"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029347324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 30945759, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '03de14fe5a3852ae'}}}