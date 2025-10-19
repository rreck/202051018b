```json
{
  "id": "6515dbf8fc082499",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290204,
  "host_pid": "9e6742732c60:1",
  "hash": "e8019405fd02d80e4645f913799375a004db320885165b17b89a73fe0d35e55f",
  "cid": "QmV1e8019405fd02d80e4645f913799375a004db3208",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290204,
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
      "evaluated_at": 1760290204
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
  "sig": "39174f81e614576b5d8331d576a023e368fe34cfd2ac53ab62bb2c55f7370c67"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593439832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 34535520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': '7b717df8c1c9c887'}}}