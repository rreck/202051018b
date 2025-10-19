```json
{
  "id": "d4f61be6452bbe92",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288847,
  "host_pid": "9e6742732c60:1",
  "hash": "9568c29c72865bea69c26b328941467cabd06f2f90b1dd7e415d797f854e15a6",
  "cid": "QmV19568c29c72865bea69c26b328941467cabd06f2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288847,
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
      "evaluated_at": 1760288847
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
  "sig": "ceca31f380136abfea39b0f3132a22bab04632122a6da316161eb68ace41d0b7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596004100
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 106, 'threshold': 50, 'total_amount': 16835026, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 105, 'first_seen': 1760285763, 'matching_hash': '0723803785cdf871'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}