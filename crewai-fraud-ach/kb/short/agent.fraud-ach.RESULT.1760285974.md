```json
{
  "id": "ddd814fd6ea7ed23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285974,
  "host_pid": "9e6742732c60:1",
  "hash": "108126eda868edeb846ff0fbe32ae7d39f3620efb4e5ddcdec2fc8549bcda13c",
  "cid": "QmV1108126eda868edeb846ff0fbe32ae7d39f3620ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285974,
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
      "evaluated_at": 1760285974
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
  "sig": "6711baeff262032e2a610cd2b79b23a0fa126837368614e6f6ba3225c9257d0a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000035025346
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285763, 'matching_hash': 'a8a877b5861d69af'}}}: 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760284979, 'matching_hash': 'a761076f0402b0d4'}}}