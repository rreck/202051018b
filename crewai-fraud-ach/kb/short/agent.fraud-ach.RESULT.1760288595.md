```json
{
  "id": "0858caaf65925a50",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288595,
  "host_pid": "9e6742732c60:1",
  "hash": "0d4104d4d478453f2d70b0232d03f0cdee6cbc70104cd2d2499ccf20cb3c1011",
  "cid": "QmV10d4104d4d478453f2d70b0232d03f0cdee6cbc70",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288595,
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
      "evaluated_at": 1760288595
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
  "sig": "8900b577df23820894feae7209d1fa8f622b39be25a031ccc83969f533468a22"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244291071
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 12404938, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285763, 'matching_hash': '1f8fb3dc368ee7c3'}}}