```json
{
  "id": "3b87e404afc246ae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294006,
  "host_pid": "9e6742732c60:1",
  "hash": "baeafda293a0be211ec7cddd83fbab7c260a880885d78af47c0151eb520c5190",
  "cid": "QmV1baeafda293a0be211ec7cddd83fbab7c260a8808",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294006,
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
      "evaluated_at": 1760294006
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
  "sig": "00ebe891497dc4769813df2077a02569767ca49b63e8a516831b74cb24874523"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025444978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 12180110, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': 'f3568a0597cdbf93'}}} {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '987899137', 'validation_error': 'Invalid routing number checksum'}}}