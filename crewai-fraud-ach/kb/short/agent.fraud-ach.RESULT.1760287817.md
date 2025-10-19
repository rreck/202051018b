```json
{
  "id": "b1d86609d863ceb2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287817,
  "host_pid": "9e6742732c60:1",
  "hash": "27b98b32d880e9a8fbda82f9c9d283834bccb8598eb365665259f00c8daa220a",
  "cid": "QmV127b98b32d880e9a8fbda82f9c9d283834bccb859",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287817,
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
      "evaluated_at": 1760287817
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
  "sig": "c41737c8921a2bee25f79953bc0c1f011ae7e5e22074618313546fdf76084204"
}
```

Fraud detected: duplicate_transaction (score: 90)
Transaction: 122105152206156
Details: {'velocity': {'fraud_detected': True, 'risk_score': 96, 'details': {'transaction_count': 73, 'threshold': 50, 'total_amount': 17946174, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 72, 'first_seen': 1760285764, 'matching_hash': '90dfebdd1b129ec8'}}}