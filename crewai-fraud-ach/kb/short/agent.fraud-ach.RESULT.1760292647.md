```json
{
  "id": "15558addf74a80ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292647,
  "host_pid": "9e6742732c60:1",
  "hash": "4bcfbe05f4e34a64909ce208fc172b9159863b8bca22d37c58de326c9d5780eb",
  "cid": "QmV14bcfbe05f4e34a64909ce208fc172b9159863b8b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292647,
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
      "evaluated_at": 1760292647
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
  "sig": "f14636d9442d45463d4b10d7055e654515db758abf21bd19db497055e86070c1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244206130
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 19142530, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285764, 'matching_hash': '13fbcd8431ec0e21'}}}