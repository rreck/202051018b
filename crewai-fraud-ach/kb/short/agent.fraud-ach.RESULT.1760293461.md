```json
{
  "id": "043833fe32db5d4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293461,
  "host_pid": "9e6742732c60:1",
  "hash": "363ef91445629f075f1fa1b8efb01ed1a9bcc15fa02fb53fc7ef7abbb5c76556",
  "cid": "QmV1363ef91445629f075f1fa1b8efb01ed1a9bcc15f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293461,
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
      "evaluated_at": 1760293461
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
  "sig": "5235e9068cf161748232a98a7202dfc527345a698f3c0e6aff32a252c01d083d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241330040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 58378830, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': '556aef048193b362'}}}