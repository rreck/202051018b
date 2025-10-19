```json
{
  "id": "95464926dbb41bdc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287474,
  "host_pid": "9e6742732c60:1",
  "hash": "242990d2254cae2d0c749c2b1e99169ea471dea09575f44388966dba90fdceb2",
  "cid": "QmV1242990d2254cae2d0c749c2b1e99169ea471dea0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287474,
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
      "evaluated_at": 1760287474
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "45fc545e46175245aba62ddeaf1e47b1445259caeaebf5fa1c6bd93ff8fd27fa"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 122105152240558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 25434377, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285765, 'matching_hash': '0371944fd59dbf43'}}}